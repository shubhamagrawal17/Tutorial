const express = require('express');
const path = require('path');
const { sum } = require('./math');

const app = express();
const PORT = 3000;

app.use(express.static(path.join(__dirname, '../public')));

app.get('/sum', (req, res) => {
  const { a, b } = req.query;
  res.json({ result: sum(Number(a), Number(b)) });
});

app.listen(PORT, () => {
  console.log(`App running on http://localhost:${PORT}`);
});
