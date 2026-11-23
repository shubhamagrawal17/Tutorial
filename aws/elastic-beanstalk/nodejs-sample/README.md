# Elastic Beanstalk Node.js sample

A minimal Express application packaged for an AWS Elastic Beanstalk deployment.

## Files
- `server.js` — Express HTTP server. It listens on the `PORT` environment variable, defaulting to 8080.
- `package.json` — application metadata and Express dependency.
- `buildspec.yml` — CodeBuild artifact packaging example.

## Run locally
Requires a supported Node.js runtime.

```bash
npm install
npm start
```

Open `http://localhost:8080/`.

## Build artifact
The CodeBuild buildspec packages files from `aws/elastic-beanstalk/nodejs-sample`. Check the CodeBuild source root and artifact configuration if using this buildspec in a project with a different source layout.

For production, commit a lockfile, pin the Node.js runtime supported by the selected Elastic Beanstalk platform, add health checks and structured logging, and configure IAM roles rather than embedding credentials.
