# DevOps, Cloud & Kubernetes Tutorials

A collection of hands-on learning labs, implementation notes, sample applications, infrastructure definitions, and CI/CD examples covering Azure, AWS, Kubernetes, GitOps, Terraform, Helm, and DevSecOps.

> **Repository scope:** These are independent tutorials and experiments, not one deployable product. Each example has its own prerequisites and maturity level. Review its documentation, configuration, and security posture before using it in a real environment.

## Start here

- [Project catalogue](docs/PROJECT-CATALOG.md) — browse tutorials by technology and purpose.
- [Repository structure](docs/REPOSITORY-STRUCTURE.md) — understand how the collection is organized.
- [Contributing guide](CONTRIBUTING.md) — conventions for adding or improving a tutorial.

## Technology areas

| Area | Topics |
|---|---|
| Azure and AKS | Private AKS, ACR, Key Vault, Application Gateway, Azure networking |
| AWS | EKS, EBS, Elastic Beanstalk |
| Kubernetes | Workloads, Services, Ingress, Gateway API, storage, troubleshooting |
| Delivery and GitOps | Azure Pipelines, GitHub Actions, Helm, Argo CD, blue-green releases |
| Infrastructure as Code | Terraform-based Azure infrastructure and VM provisioning |
| DevSecOps | SAST, dependency auditing, IaC scanning, container scanning, test reporting |
| Applications | .NET, Python, Node.js, Java, and sample web applications |

## Quick start

1. Open the [project catalogue](docs/PROJECT-CATALOG.md) and choose a tutorial.
2. Read that project's README and inspect its manifests, pipeline, and variables.
3. Confirm the required CLI versions, cloud permissions, and billable resources.
4. Supply environment-specific values through secure configuration; do not commit credentials.
5. Validate locally before applying changes to a cloud account or cluster.

There is no single root-level build command because the repository contains independent projects implemented with different tools and runtimes.

## Safety and security

- Treat all examples as learning material until you have reviewed and tested them.
- Never commit passwords, access tokens, private keys, kubeconfigs, connection strings, or production secrets.
- Prefer managed identities or workload identity, least-privilege access, private networking, and short-lived credentials.
- Review Terraform plans before applying infrastructure changes. Destructive operations must require deliberate human approval.
- Pin action, tool, and container versions for repeatable workflows; avoid deploying mutable `latest` tags in production.
- Cloud resources can incur charges. Understand the cost and cleanup procedure before running a tutorial.

## Repository status

The repository is organized by topic for discoverability. Existing project directories and paths are intentionally preserved while the catalogue and contribution standards are introduced. Some older examples may contain generated IDE files, archived bundles, legacy runtime versions, or incomplete documentation; these should be reviewed in focused follow-up changes rather than assumed production-ready.

## License

No repository-wide license is currently declared. Unless a license is added, reuse and redistribution are not automatically granted. Check the license of any third-party code or assets included in an individual tutorial.
