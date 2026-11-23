# Repository structure

Azure, AWS, Kubernetes, and GitOps tutorials are grouped under `azure/`, `aws/`, `kubernetes/`, and `gitops/`. Cross-cutting CI/CD examples remain at their previous locations until a separate migration pull request.

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
├── aws/
│   ├── README.md
│   ├── eks/ebs/
│   └── elastic-beanstalk/nodejs-sample/
├── kubernetes/
│   ├── README.md
│   ├── gateway-api/
│   └── helm/
│       ├── README.md
│       ├── built-in-objects/
│       ├── named-template/
│       ├── helm-boolean-and-demo/
│       ├── helm-ifelse-or-not-demo/
│       └── helm-ifelse-eq-demo/
├── gitops/
│   ├── README.md
│   └── argocd/
│       ├── README.md
│       ├── flask-app/
│       ├── gitops-repo/
│       └── blue-green-rollouts/
├── CI/CD and DevSecOps examples
└── Application examples
```

The remaining root-level labels are descriptive placeholders, not literal directory names. Use the [project catalogue](PROJECT-CATALOG.md) for exact paths.

## GitOps and Argo CD migration mapping
| Previous path | New path |
|---|---|
| `ArgoCD/README.md` | `gitops/argocd/README.md` |
| `ArgoCD/Python-Flask/` | `gitops/argocd/flask-app/` |
| `ArgoCD/gitops-repo/` | `gitops/argocd/gitops-repo/` |
| `ArgoCD-Blue-Green-Deployment/README.md` | `gitops/argocd/blue-green-rollouts/README.md` |
| `ArgoCD-Blue-Green-Deployment/argocd-blue-green-app/` | `gitops/argocd/blue-green-rollouts/app/` |
| `ArgoCD-Blue-Green-Deployment/argocd-blue-green-manifests/` | `gitops/argocd/blue-green-rollouts/manifests/` |

## Kubernetes migration mapping
| Previous path | New path |
|---|---|
| `Kubernetes-Gateway-api/` | `kubernetes/gateway-api/` |
| `Helm/Built-in Objects/` | `kubernetes/helm/built-in-objects/` |
| `Helm/Named Template/` | `kubernetes/helm/named-template/` |
| `Helm/helm-boolean-and-demo/` | `kubernetes/helm/helm-boolean-and-demo/` |
| `Helm/helm-ifelse-OR-NOT-demo/` | `kubernetes/helm/helm-ifelse-or-not-demo/` |
| `Helm/helm-ifelse-eq-demo/` | `kubernetes/helm/helm-ifelse-eq-demo/` |

## AWS migration mapping
| Previous path | New path |
|---|---|
| `AWS-EKS/EBS/` | `aws/eks/ebs/` |
| `AWS/my-beanstalk-app/` | `aws/elastic-beanstalk/nodejs-sample/` |

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
