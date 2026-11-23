# GitOps tutorials

This section contains Argo CD examples that separate application source/build pipelines from Kubernetes deployment configuration stored in Git.

## Argo CD
- [Argo CD platform setup](argocd/README.md) — install Argo CD, access its UI/CLI securely, and register a cluster.
- [Flask application pipeline](argocd/flask-app/) — build a container and update a GitOps manifest repository.
- [GitOps manifest repository](argocd/gitops-repo/) — Kubernetes Deployment and Service watched by Argo CD.
- [Blue-green delivery with Argo Rollouts](argocd/blue-green-rollouts/) — preview and active Services, manual promotion, and an Azure Pipelines example.

## GitOps operating principles
- Treat Git as the reviewed source of truth for desired cluster state.
- Keep application source and environment manifests logically separate.
- Use immutable image tags or digests and review manifest changes before promotion.
- Scope Argo CD projects, repositories, destinations, and RBAC to least privilege.
- Avoid public exposure of the Argo CD API/UI unless protected by an approved ingress, TLS, SSO, and network policy.
- Keep credentials in a secret manager or supported secret integration; never commit tokens or kubeconfigs.

The examples are learning material and may include environment-specific placeholders. Validate every referenced repository, registry, cluster, and namespace before running them.
