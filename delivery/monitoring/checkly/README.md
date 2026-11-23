# Monitoring and browser testing

- [Checkly demo app](checkly/) — sample Node.js web application and browser login check.

Use a dedicated Checkly project/API key and store it in a secret manager or CI secret variable. Never put API keys in Docker commands, README files, or source control. Use disposable test credentials for sample login flows.
