# Repository structure

Azure tutorials are now grouped under `azure/`. AWS, standalone Kubernetes, GitOps, and cross-cutting CI/CD examples remain at their previous locations until separate migration pull requests.

```text
Tutorial/
├── README.md
├── CONTRIBUTING.md
├── docs/
├── tests/
├── .github/workflows/
├── azure/
│   ├── README.md
│   ├── aks/
│   │   ├── nginx-ingress/
│   │   ├── keyvault-aspnet/
│   │   ├── cert-manager-letsencrypt/
│   │   └── troubleshooting/
│   ├── key-vault/
│   │   ├── aspnet-sample/
│   │   └── azure-sql-local-dotnet.md
│   ├── terraform/infra-as-code/
│   └── devops-agent-vm/
├── AWS and EKS examples
├── Kubernetes and Helm examples
├── Argo CD and GitOps examples
├── CI/CD and DevSecOps examples
└── Application examples
```

The remaining root-level labels are descriptive placeholders, not literal directory names. Use the [project catalogue](PROJECT-CATALOG.md) for exact paths.

## Azure migration mapping
| Previous path | New path |
|---|---|
| `AKS-Nginx/` | `azure/aks/nginx-ingress/` |
| `AKS_KeyVault ASP.NET Application/` | `azure/aks/keyvault-aspnet/` |
| `KeyVault with ASP.NET Application/` | `azure/key-vault/aspnet-sample/` |
| `SSL on Aks with Lets Encrypt/` | `azure/aks/cert-manager-letsencrypt/` |
| `infra-as-code/` | `azure/terraform/infra-as-code/` |
| `VM/` | `azure/devops-agent-vm/` |
| `AKS-Deployment-Issue.yaml` | `azure/aks/troubleshooting/AKS-Deployment-Issue.yaml` |
| `KeyVault+Azure SQL DB + Local Dotnet Core App.md` | `azure/key-vault/azure-sql-local-dotnet.md` |

## Migration rules
1. Move one technology group per branch/PR.
2. Preserve project contents unless a separate change explicitly modifies them.
3. Update pipeline working directories, Docker build contexts, relative links, and references in the same change.
4. Add automated path checks and run relevant project validation.
5. State clearly when cloud deployment or runtime validation was not performed.
6. Keep unrelated Kubernetes, GitOps, and CI/CD projects in their own migration batches.

The root `.gitignore` prevents common generated files and local secrets from being added in future commits. It does not untrack files already committed. Existing IDE caches and archives are retained pending a separate review.
