# Azure Pipelines examples

| Project | Purpose | Main entry point |
|---|---|---|
| [AKS blue-green](aks-blue-green/) | ASP.NET Core build/container and blue-green AKS examples | `azure-pipelines.yml` and numbered variants |
| [Python App](python-app/) | Template-based Python build/test and App Service deployment | `temp-python-app/azure-pipelines.yml` |
| [Helm single deployment](helm-single/) | Build image, package chart, deploy to AKS | `azure-pipelines.yml` |
| [Helm multi-environment](helm-multi-env/) | Dev and QA releases with separate values files | `azure-pipelines.yml` |

Pipelines use illustrative Azure DevOps service connection names and cloud resource identifiers. Configure them in the Azure DevOps project and replace placeholders before running.

The projects are kept independent because they demonstrate different deployment patterns. Do not configure all pipelines to deploy to the same cluster or namespace without reviewing their manifests and release names.
