# Delivery engineering tutorials

This section groups CI/CD, Helm-based releases, GitHub Actions, DevSecOps controls, and browser/API monitoring examples. These are independent learning projects, not one shared deployment platform.

## Azure Pipelines
- [AKS blue-green deployment](azure-pipelines/aks-blue-green/) — ASP.NET Core build and AKS blue/green manifests.
- [Python application pipeline](azure-pipelines/python-app/) — reusable Azure Pipelines templates for build, tests, and App Service deployment.
- [Helm deployment to AKS](azure-pipelines/helm-single/) — package a Helm chart, publish it, and deploy it.
- [Multi-environment Helm delivery](azure-pipelines/helm-multi-env/) — Dev and QA Helm releases with environment-specific values.

## GitHub Actions
- [GitHub Actions tutorials](github-actions/README.md) — day-based examples, TypeScript/Node.js, FastAPI, Kubernetes, and Azure OIDC.

## DevSecOps
- [Azure DevOps DevSecOps pipeline](devsecops/README.md) — SAST, dependency scanning, tests, container scanning, IaC checks, and deployment examples.

## Monitoring and testing
- [Checkly demo](monitoring/checkly/) — sample web app and browser check.

## Before running
- Replace sample subscriptions, service connections, registry names, cluster names, app names, and namespaces.
- Use managed identity or OIDC where supported; never commit PATs, API keys, passwords, kubeconfigs, or service-principal secrets.
- Pin action, scanner, Helm, and container versions for repeatable builds.
- Review deployment environments and approval checks before connecting production.
- Validate each project independently; moving folders does not make its pipeline production-ready.
