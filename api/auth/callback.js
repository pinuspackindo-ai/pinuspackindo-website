export default async function handler(req, res) {
  const { code } = req.query;

  if (!code) {
    return res.status(400).send('Missing code parameter');
  }

  try {
    const response = await fetch('https://github.com/login/oauth/access_token', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
      },
      body: JSON.stringify({
        client_id: process.env.GITHUB_CLIENT_ID,
        client_secret: process.env.GITHUB_CLIENT_SECRET,
        code,
      }),
    });

    const data = await response.json();

    if (data.error) {
      const html = `<!DOCTYPE html><html><body><script>
        window.opener && window.opener.postMessage(
          'authorization:github:error:${JSON.stringify({ error: data.error_description })}',
          '*'
        );
        window.close();
      <\/script></body></html>`;
      res.setHeader('Content-Type', 'text/html');
      return res.status(200).send(html);
    }

    const token = data.access_token;
    const message = `authorization:github:success:${JSON.stringify({ token, provider: 'github' })}`;

    const html = `<!DOCTYPE html>
<html>
<head><title>Authorizing...</title></head>
<body>
<p>Authorizing, please wait...</p>
<script>
  (function() {
    var message = ${JSON.stringify(message)};
    function sendMessage() {
      if (window.opener) {
        window.opener.postMessage(message, '*');
        setTimeout(function() { window.close(); }, 1000);
      } else {
        setTimeout(sendMessage, 500);
      }
    }
    sendMessage();
  })();
<\/script>
</body>
</html>`;

    res.setHeader('Content-Type', 'text/html');
    return res.status(200).send(html);
  } catch (error) {
    return res.status(500).send(`Server error: ${error.message}`);
  }
}
