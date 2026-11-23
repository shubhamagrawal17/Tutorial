# Project catalogue

This catalogue links to the existing project locations. The first structure-improvement change intentionally does not move tutorial directories, so existing scripts, pipeline paths, and links continue to work.

## Azure, AKS, and networking

| Project | What it covers |
|---|---|
| [AKS NGINX ingress](../AKS-Nginx/) | NGINX ingress controller installation and sample routing |
| [AKS with ASP.NET Key Vault](../AKS_KeyVault%20ASP.NET%20Application/) | ASP.NET application and AKS deployment example using Azure Key Vault |
| [Key Vault with ASP.NET](../KeyVault%20with%20ASP.NET%20Application/) | Related ASP.NET and Key Vault sample |
| [AKS blue-green CI/CD](../CICD%20For%20AKS%20with%20Blue-Green%20Deployment/) | .NET application build and Kubernetes blue-green manifests |
| [AKS Helm deployment](../aks-helm-deploy/) | Application packaging and Helm deployment |
| [AKS multi-environment Helm](../aks-helm-multi-env/) | Separate development and QA Helm values and pipeline stages |
| [Kubernetes Gateway API](../Kubernetes-Gateway-api/) | GatewayClass, Gateway, HTTPRoute, and application resources |
| [Let's Encrypt on AKS](../SSL%20on%20Aks%20with%20Lets%20Encrypt/) | cert-manager and certificate resources |
| [Azure infrastructure as code](../infra-as-code/) | Terraform for networking, AKS, ACR, VMs, databases, and related infrastructure |
| [Self-hosted agent VM](../VM/) | Terraform and shell automation for an Azure DevOps agent VM |
| [Key Vault and Azure SQL notes](../KeyVault%2BAzure%20SQL%20DB%20%2B%20Local%20Dotnet%20Core%20App.md) | Local .NET, Key Vault, and Azure SQL walkthrough |

## AWS

| Project | What it covers |
|---|---|
| [AWS EKS and EBS](../AWS-EKS/) | EKS cluster notes, EBS CSI storage, StorageClass, PVC, and Pod |
| [AWS Elastic Beanstalk sample](../AWS/) | Node.js application and buildspec example |

## Kubernetes, GitOps, and release strategies

| Project | What it covers |
|---|---|
| [Argo CD and Flask](../ArgoCD/) | Flask application pipeline and GitOps repository example |
| [Argo CD blue-green deployment](../ArgoCD-Blue-Green-Deployment/) | Argo CD, Argo Rollouts, preview and active services, and promotion pipeline |
| [Kubernetes deployment troubleshooting](../AKS-Deployment-Issue.yaml) | Deliberately problematic workload manifest for debugging exercises |
| [Helm tutorials](../Helm/) | Helm charts, values, built-in objects, and template examples |

## CI/CD and DevSecOps

| Project | What it covers |
|---|---|
| [GitHub Actions tutorials](../GitHub%20Actions/) | Day-based workflow examples and application tests |
| [Python application CI/CD](../CICD%20for%20Python%20App/) | Python app, pipeline stages, and tests |
| [DevSecOps Azure project](../devsecops-azure-project/) | SAST, dependency audit, IaC scanning, tests, coverage, and container pipeline |
| [Checkly sample](../Checkly/) | Sample web application and browser-based checks |

## Application examples

| Project | What it covers |
|---|---|
| [Java application](../Java-app/) | Maven sample and Azure Pipelines/SonarCloud configuration |
| [eTicket application](../eticket-App/) | .NET application, Dockerfile, and deployment assets |
| [Python Docker application](../python-app-docker/) | Python application, Docker, Azure Pipelines, and Terraform |

## Notes about the collection

- Some topics have multiple generations of examples. Compare their README files and pipeline definitions before choosing one.
- A directory's presence in this catalogue does not certify that it is secure, current, or production-ready.
- Archived ZIP/7z bundles and generated IDE/build artifacts are retained for now. Their cleanup should be handled separately after checking whether they are still needed.
- If a project is missing from this catalogue, add a row under the closest topic and keep the link relative to this file.
