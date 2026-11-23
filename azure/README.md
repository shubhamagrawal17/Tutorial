# Azure tutorials

Azure-specific examples live under this directory. Each tutorial remains an independent project; use its local README, pipeline, manifests, and Terraform files as the source of truth.

## AKS
- [NGINX ingress](aks/nginx-ingress/)
- [ASP.NET and Key Vault deployment](aks/keyvault-aspnet/)
- [cert-manager and Let's Encrypt](aks/cert-manager-letsencrypt/)
- [Deployment troubleshooting exercise](aks/troubleshooting/AKS-Deployment-Issue.yaml)

## Azure platform services
- [ASP.NET and Key Vault sample](key-vault/aspnet-sample/)
- [Local .NET, Key Vault, and Azure SQL walkthrough](key-vault/azure-sql-local-dotnet.md)
- [Terraform infrastructure](terraform/infra-as-code/)
- [Azure DevOps self-hosted agent VM](devops-agent-vm/)

## Important
- Existing project files, archived bundles, and tracked IDE artifacts were moved without deleting or rewriting them.
- Pipeline paths affected by this move were updated.
- Some examples contain legacy runtimes or public networking and need review before production use.
- Cloud deployments can incur charges. Review plans and cleanup steps before creating resources.
