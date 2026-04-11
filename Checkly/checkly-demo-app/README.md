# Checkly Demo App

## Run locally
docker build -t checkly-demo .
docker run -p 3000:3000 checkly-demo

## Login
username: admin
password: password

## Checkly agent 
docker run -d --name checkly-agent -e API_KEY="pl_cd7066690d464253b2d6a89cf576ac40" -e LOCATION_ID="mylocation" checkly/agent:latest
