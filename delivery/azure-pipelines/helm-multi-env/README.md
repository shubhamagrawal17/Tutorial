# Multi-environment Helm delivery to AKS

This example builds a container image once, then deploys the same build identifier to Dev and QA using Helm and separate values files.

## Structure
- `app/` — sample Node.js app and Dockerfile.
- `helm/my-app/` — chart and shared templates.
- `helm/my-app/values.dev.yaml` — development configuration.
- `helm/my-app/values.qa.yaml` — QA configuration.
- `azure-pipelines.yml` — build, Dev deployment, and QA deployment stages.

## Configure
Update the ACR service connection, AKS service connection, registry, cluster/resource group, Azure DevOps environments, namespaces, and values files. Configure approval/check policies on the QA environment if required.

## Production considerations
The sample currently demonstrates Dev and QA, not a complete production promotion workflow. Add an explicitly protected production stage only after defining the release approval, verification, and rollback model. Pin image tags and Helm version; review Service exposure and resource settings in the chart before deployment.
