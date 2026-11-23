# Project catalogue

Azure, AWS, and Kubernetes tutorials are grouped under `azure/`, `aws/`, and `kubernetes/`. Argo CD and GitOps projects are grouped under `gitops/`; cross-cutting CI/CD projects remain at their existing paths until their own migration batch.

## Azure
| Project | Description |
|---|---|
| [Azure tutorials index](../azure/README.md) | Azure project overview |
| [AKS NGINX ingress](../azure/aks/nginx-ingress/) | Ingress controller and sample routing |
| [AKS ASP.NET Key Vault](../azure/aks/keyvault-aspnet/) | ASP.NET app and AKS deployment |
| [ASP.NET Key Vault sample](../azure/key-vault/aspnet-sample/) | ASP.NET and Key Vault example |
| [Let's Encrypt on AKS](../azure/aks/cert-manager-letsencrypt/) | cert-manager and certificate resources |
| [AKS troubleshooting manifest](../azure/aks/troubleshooting/AKS-Deployment-Issue.yaml) | Intentionally faulty workload exercise |
| [Azure Terraform](../azure/terraform/infra-as-code/) | Azure networking, AKS, ACR, VM, SQL, and gateway examples |
| [Azure DevOps agent VM](../azure/devops-agent-vm/) | Self-hosted agent VM example |
| [Key Vault and Azure SQL notes](../azure/key-vault/azure-sql-local-dotnet.md) | Local .NET, Key Vault, and SQL walkthrough |

## AWS
| Project | Description |
|---|---|
| [AWS tutorials index](../aws/README.md) | AWS project overview |
| [Amazon EKS and EBS](../aws/eks/ebs/) | EKS cluster configuration, EBS CSI driver, StorageClass, PVC, Pod, and Service |
| [Elastic Beanstalk Node.js sample](../aws/elastic-beanstalk/nodejs-sample/) | Node.js Express application and CodeBuild buildspec |

## Kubernetes and GitOps
| Project | Description |
|---|---|
| [Kubernetes tutorials index](../kubernetes/README.md) | Kubernetes and Helm learning examples |
| [Gateway API with Envoy Gateway](../kubernetes/gateway-api/) | GatewayClass, Gateway, HTTPRoute, weighted backend routing |
| [Helm tutorials](../kubernetes/helm/) | Helm charts, built-in objects, named templates, and conditional templates |
| [GitOps and Argo CD index](../gitops/README.md) | GitOps learning paths and Argo CD projects |
| [Argo CD platform setup](../gitops/argocd/README.md) | Argo CD installation, access, and cluster registration |
| [Argo CD Flask application](../gitops/argocd/flask-app/) | Flask sample, Azure Pipelines image build, and GitOps update |
| [Argo CD GitOps manifests](../gitops/argocd/gitops-repo/) | Kubernetes Deployment and Service watched by Argo CD |
| [Argo Rollouts blue-green](../gitops/argocd/blue-green-rollouts/) | Preview/active Services, Rollout, Ingress, and promotion pipeline |

## CI/CD and DevSecOps
| Project | Description |
|---|---|
| [Delivery tutorials index](../delivery/README.md) | CI/CD, Helm, GitHub Actions, DevSecOps, and monitoring |
| [Azure Pipelines examples](../delivery/azure-pipelines/README.md) | AKS blue-green, Python, and Helm delivery |
| [GitHub Actions tutorials](../delivery/github-actions/README.md) | Day-based CI/CD and Azure OIDC examples |
| [DevSecOps pipeline](../delivery/devsecops/README.md) | SAST, dependency, tests, Trivy, Checkov, and deployments |
| [Checkly monitoring](../delivery/monitoring/README.md) | Browser monitoring demo and test application |

## Applications
| Project | Description |
|---|---|
| [Java application](../Java-app/) | Maven and SonarCloud sample |
| [eTicket application](../eticket-App/) | .NET application and deployment assets |
| [Python Docker application](../python-app-docker/) | Python, Docker, pipeline, and Terraform |

## Migration notes
- Azure project contents and archived bundles were moved without deleting tracked files.
- Pipeline Dockerfile/build-context and Terraform working-directory paths were updated for the new Azure locations.
- The catalogue does not certify a project as secure, current, or production-ready.
- Add new projects here using links relative to this file.
