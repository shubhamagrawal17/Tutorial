# Python App — Azure Pipelines templates

This sample uses reusable Azure Pipelines templates to build and test a Python application, publish an artifact, and deploy to development and production Azure App Service environments.

## Structure
- `temp-python-app/azure-pipelines.yml` — top-level pipeline that includes templates.
- `temp-python-app/pipelines/build.yml` — Python setup, dependency installation, lint, tests, Bandit, and artifact packaging.
- `temp-python-app/pipelines/deploy_dev.yml` — development App Service deployment.
- `temp-python-app/pipelines/deploy-prod.yml` — production App Service deployment.
- `temp-python-app/tests/` — unit tests.

## Configure
Replace the Azure service connection, App Service names, environments, Python runtime, and deployment settings. Configure approvals and checks on the production environment in Azure DevOps rather than relying only on YAML ordering.

The project uses Python 3.9 in its sample configuration. Check runtime support and dependency compatibility before use; update the version consistently across the pipeline, App Service runtime, and application dependencies.

## Validation
Run the unit tests locally and confirm the pipeline template paths resolve from the selected YAML entry point. This sample has not been executed as part of this folder migration.
