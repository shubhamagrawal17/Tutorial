# Project catalogue

Azure tutorials have been migrated into `azure/`. AWS, standalone Kubernetes, GitOps, and cross-cutting CI/CD projects remain at their existing paths until their own migration batches.

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
| [AWS EKS and EBS](../AWS-EKS/) | EKS and EBS CSI storage |
| [AWS Elastic Beanstalk](../AWS/) | Node.js and buildspec example |

## Kubernetes and GitOps
| Project | Description |
|---|---|
| [Kubernetes Gateway API](../Kubernetes-Gateway-api/) | GatewayClass, Gateway, HTTPRoute |
| [Helm tutorials](../Helm/) | Helm charts and templates |
| [Argo CD and Flask](../ArgoCD/) | Flask and GitOps |
| [Argo CD blue-green](../ArgoCD-Blue-Green-Deployment/) | Argo Rollouts and promotion |

## CI/CD and DevSecOps
| Project | Description |
|---|---|
| [AKS blue-green CI/CD](../CICD%20For%20AKS%20with%20Blue-Green%20Deployment/) | .NET and Kubernetes blue-green |
| [AKS Helm deployment](../aks-helm-deploy/) | Helm deployment pipeline |
| [AKS multi-environment Helm](../aks-helm-multi-env/) | Dev and QA values and pipeline |
| [GitHub Actions](../GitHub%20Actions/) | Workflow and application test examples |
| [Python CI/CD](../CICD%20for%20Python%20App/) | Python pipeline and tests |
| [DevSecOps Azure](../devsecops-azure-project/) | SAST, dependency, IaC, and container scanning |
| [Checkly](../Checkly/) | Browser checks and sample app |

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
