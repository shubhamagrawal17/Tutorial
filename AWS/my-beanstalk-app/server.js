const express = require('express');
const app = express();

// Elastic Beanstalk sets the PORT environment variable for you
// It defaults to 8080 if not explicitly set
const PORT = process.env.PORT || 8080;

// Define a simple route for the root URL
app.get('/', (req, res) => {
  console.log('Received a request!');
  res.send('<h1>Hello from Elastic Beanstalk app!</h1>');
});

// Start the server and listen on the specified port
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
