# Argo CD platform setup

This guide covers a basic Argo CD installation and the companion Argo Rollouts controller used by the blue-green example.

## Prerequisites
- A Kubernetes cluster and a working `kubectl` context.
- Helm or the Kubernetes manifest installation method.
- Argo CD CLI if you want to use the command line.
- Administrative access only for the initial installation; use scoped RBAC afterwards.

## Install Argo CD
For a learning cluster, use the upstream installation manifest:

```bash
kubectl create namespace argocd
kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml
kubectl get pods -n argocd
```

For a repeatable or production installation, select and pin a tested Argo CD release and follow its release-specific installation and upgrade documentation. Do not rely on the moving `stable` manifest for a controlled production rollout.

## Access the API/UI locally
Prefer port-forwarding for a local learning environment rather than exposing the Argo CD server directly through a public LoadBalancer:

```bash
kubectl port-forward svc/argocd-server -n argocd 8080:443
```

Open `https://localhost:8080`. Retrieve the initial admin password from the cluster when needed:

```bash
argocd admin initial-password -n argocd
```

Change the initial password after first login and configure SSO/RBAC for shared environments. Do not copy passwords or encoded secret values into source files or documentation. Use verified TLS in normal operations; do not disable certificate verification as a permanent workaround.

## Register the current cluster
For an in-cluster deployment, Argo CD can usually deploy to its own cluster without adding another cluster. To register a separate target cluster, inspect the current context and grant only the required permissions:

```bash
kubectl config get-contexts
argocd cluster add <target-context>
```

Review the generated service account and RBAC permissions. Avoid granting broad cluster-admin access unless the installation design explicitly requires it and the risk is accepted.

## Install Argo Rollouts
The blue-green example also needs the Argo Rollouts CRDs and controller. Install a pinned release appropriate to your Kubernetes version using the upstream Argo Rollouts installation instructions, then verify:

```bash
kubectl get crd rollouts.argoproj.io
kubectl get pods -n argo-rollouts
```

## Related examples
- [Flask application and GitOps pipeline](flask-app/)
- [GitOps Kubernetes manifests](gitops-repo/)
- [Blue-green Rollouts sample](blue-green-rollouts/)

## Security notes
The old tutorial contained a static IP, a base64 password example, direct LoadBalancer exposure, and `argocd cluster add --insecure`. Those are intentionally not repeated here. Base64 is encoding, not encryption. Use private access, TLS, SSO/RBAC, least privilege, and secret-management integrations for real environments.
