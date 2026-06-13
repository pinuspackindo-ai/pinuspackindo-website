export default function handler(req, res) {
  const clientId = process.env.GITHUB_CLIENT_ID;
  const redirectUri = `https://pinuspackindo.com/api/auth/callback`;
  const scope = 'repo,user';
  const { provider } = req.query;

  if (provider === 'github') {
    const githubAuthUrl = `https://github.com/login/oauth/authorize?client_id=${clientId}&redirect_uri=${encodeURIComponent(redirectUri)}&scope=${scope}&allow_signup=false`;
    return res.redirect(githubAuthUrl);
  }

  res.status(400).send('Unknown provider');
}
