const express = require('express');
const session = require('express-session');

const app = express();

// Middleware
app.use(express.urlencoded({ extended: true }));
app.use(express.json()); // 🔥 Needed for API POST

app.use(session({
  secret: 'test-secret',
  resave: false,
  saveUninitialized: true
}));

// =====================
// 🔗 API ROUTES
// =====================

// Health Check API
app.get('/api/health', (req, res) => {
  res.json({
    status: 'ok',
    message: 'API is working'
  });
});

// Login API (for API testing)
app.post('/api/login', (req, res) => {
  const { username, password } = req.body;

  if (username === 'admin' && password === 'password') {
    return res.json({ success: true });
  }

  return res.status(401).json({ success: false });
});

// =====================
// 🌐 UI ROUTES
// =====================

// Home
app.get('/', (req, res) => {
  if (req.session.user) {
    res.send(`<h1>Welcome ${req.session.user}</h1><a href="/logout">Logout</a>`);
  } else {
    res.redirect('/login');
  }
});

// Login page
app.get('/login', (req, res) => {
  res.send(`
    <h1>Login</h1>
    <form method="POST" action="/login">
      <input name="username" placeholder="username"/>
      <input name="password" type="password" placeholder="password"/>
      <button type="submit">Login</button>
    </form>
  `);
});

// Login (UI)
app.post('/login', (req, res) => {
  const { username, password } = req.body;

  if (username === 'admin' && password === 'password') {
    req.session.user = username;
    return res.redirect('/');
  }

  res.send('Invalid credentials');
});

// Logout
app.get('/logout', (req, res) => {
  req.session.destroy(() => {
    res.redirect('/login');
  });
});

// =====================
// 🚀 START SERVER
// =====================
app.listen(3000, () => console.log('App running on port 3000'));