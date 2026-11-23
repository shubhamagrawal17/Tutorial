# DevOps, Cloud & Kubernetes Tutorials

Hands-on learning labs, implementation notes, sample applications, infrastructure definitions, and CI/CD examples covering Azure, AWS, Kubernetes, GitOps, Terraform, Helm, and DevSecOps.

> These are independent tutorials and experiments, not one deployable product. Each example has its own prerequisites and maturity level. Review its documentation, configuration, and security posture before using it in a real environment.

## Start here
- [Project catalogue](docs/PROJECT-CATALOG.md)
- [Repository structure](docs/REPOSITORY-STRUCTURE.md)
- [Contributing guide](CONTRIBUTING.md)
- [Azure tutorials](azure/README.md)
- [AWS tutorials](aws/README.md)
- [Kubernetes tutorials](kubernetes/README.md)
- [GitOps and Argo CD](gitops/README.md)

## Technology areas
| Area | Topics |
|---|---|
| Azure | AKS, ACR, Key Vault, Application Gateway, Terraform, Azure networking |
| AWS | EKS, EBS, Elastic Beanstalk |
| Kubernetes | Workloads, Services, Ingress, Gateway API, storage, troubleshooting |
| Delivery and GitOps | Azure Pipelines, GitHub Actions, Helm, Argo CD, blue-green releases |
| DevSecOps | SAST, dependency auditing, IaC scanning, container scanning, test reporting |
| Applications | .NET, Python, Node.js, Java |

## Quick start
1. Choose a tutorial from the [project catalogue](docs/PROJECT-CATALOG.md).
2. Read its README and inspect its manifests, pipeline, and variables.
3. Confirm tool versions, cloud permissions, and billable resources.
4. Supply environment-specific values securely; never commit credentials.
5. Validate locally before applying changes to a cloud account or cluster.

There is no single root-level build command because this repository contains independent projects.

## Safety
- Treat examples as learning material until reviewed and tested.
- Never commit passwords, tokens, private keys, kubeconfigs, connection strings, or production secrets.
- Prefer managed identity/workload identity, least privilege, private networking, and short-lived credentials.
- Review Terraform plans before applying infrastructure. Destructive operations require deliberate approval.
- Pin action, tool, and container versions; avoid mutable `latest` tags for production.
- Cloud resources can incur charges. Understand costs and cleanup steps before running a tutorial.

## Repository status
Azure-specific tutorials are grouped under `azure/`. AWS tutorials are grouped under `aws/`. Kubernetes and Helm tutorials are grouped under `kubernetes/`. Argo CD and GitOps tutorials are grouped under `gitops/`. Cross-cutting CI/CD examples will be migrated in a separate batch. Older examples may still contain generated IDE files, archived bundles, legacy runtimes, or incomplete documentation.

## License
No repository-wide license is currently declared. Unless a license is added, reuse and redistribution are not automatically granted.
