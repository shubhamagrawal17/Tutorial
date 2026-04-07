# Checkly Demo App

## Run locally
docker build -t checkly-demo .
docker run -p 3000:3000 checkly-demo

## Login
username: admin
password: password

## Run tests
npx checkly test
