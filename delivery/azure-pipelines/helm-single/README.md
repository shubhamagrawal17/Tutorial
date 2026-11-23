# Build and deploy a Helm chart to AKS

This sample builds a container image, packages a Helm chart as a build artifact, and deploys the packaged chart to an AKS environment using Azure Pipelines.

## Structure
- `app/` — sample Node.js app and Dockerfile.
- `helm/my-app/` — Helm chart, values, and Kubernetes templates.
- `azure-pipelines.yml` — build/push, chart packaging, artifact publishing, and Helm upgrade/install.

## Configure
Replace the ACR and AKS service connection names, resource group, cluster, namespace, image repository, and registry hostname. The chart path and Docker build context are relative to the repository checkout; confirm these paths when configuring the pipeline YAML location.

## Production considerations
- Prefer immutable image tags or digests; avoid deploying `latest`.
- Pin a tested Helm version.
- Add chart lint/template validation and application tests.
- Use a private ingress or internal Service where appropriate.
- Configure environment approvals, rollout verification, and rollback procedures.
