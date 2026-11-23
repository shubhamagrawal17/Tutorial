# Azure infrastructure as code

This project contains independent Terraform roots for Azure infrastructure components.

| Directory | Purpose |
|---|---|
| `virtual-network/` | Virtual network and peering |
| `agent-vm/` | Azure DevOps self-hosted agent VM |
| `private-acr/` | Private Azure Container Registry |
| `private-aks/` | Private Azure Kubernetes Service |
| `application-gateway/` | Application Gateway |
| `sql-dbserver/` | Azure SQL server resources |
| `log-analytics/` | Log Analytics workspace |
| `azure Front Door/` | Azure Front Door example |

## Prerequisites
- Terraform compatible with the provider constraints in the selected module.
- Azure CLI, an authenticated subscription, and permission to create its resources.
- A protected remote state backend.
- Environment-specific variables supplied securely; do not commit populated `.tfvars` or credentials.

## Validate a module
Run from the selected module directory:

```bash
terraform init
terraform fmt -check -recursive
terraform validate
terraform plan -out=tfplan
```

Review the plan and costs before applying. Apply only after approval:

```bash
terraform apply tfplan
```

Do not destroy shared or production resources without explicit authorization and a reviewed plan.

## Azure DevOps pipeline
The pipeline demonstrates multi-stage provisioning and teardown. Its working directories are repository-root-relative and updated for this folder's new location.

**Learning example only:** the pipeline contains `-auto-approve` apply and destroy operations and references environment-specific service connections, variable groups, and backend settings. Do not run it against production as-is. A production workflow should separate plan/apply, publish plans for review, require protected approvals, and isolate destructive operations.

Use least-privilege identities, protect state, avoid secrets in logs/arguments, restrict public access, and document cleanup for billable resources.
