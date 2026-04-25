import express from 'express';
import path from 'path';

const app = express();

//  Works in both dev + test + production
const publicPath = path.join(process.cwd(), 'public');

app.use(express.static(publicPath));

app.get('/', (req, res) => {
  res.sendFile(path.join(publicPath, 'index.html'));
});

app.get('/about', (req, res) => {
  res.sendFile(path.join(publicPath, 'about.html'));
});

export default app;

if (require.main === module) {
  const port = process.env.PORT || 3000;

  app.listen(port, () => {
    console.log(`Server running on port ${port}`);
  });
}
