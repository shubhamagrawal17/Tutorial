# Argo CD blue-green delivery with Argo Rollouts

This example combines Argo CD reconciliation with the Argo Rollouts blue-green strategy. A new ReplicaSet is made available through a preview Service, reviewed, and then promoted so the active Service switches to the new version.

## Layout
- `app/` — Flask sample, Dockerfile, and Azure Pipelines definition.
- `manifests/` — Rollout, active/preview Services, and Ingress.

## Prerequisites
- Kubernetes cluster with Argo CD installed.
- Argo Rollouts CRDs/controller installed and compatible with the cluster.
- An Ingress controller matching the `ingressClassName` in the manifest.
- Container registry and credentials accessible to the workload.
- Azure DevOps service connections and secret variables configured for the pipeline.

## Deploy manifests
Review namespace, image, registry, ingress class, and controller versions first. The manifests target the `production` namespace:

```bash
kubectl create namespace production
kubectl apply -f manifests/services.yaml
kubectl apply -f manifests/rollout.yaml
kubectl apply -f manifests/ingress.yaml
kubectl get rollout -n production
kubectl describe rollout demo-app-rollout -n production
```

If Argo CD manages these files, create an Application pointing to the `manifests/` directory and let Argo CD reconcile them. Avoid applying the same resources through multiple competing deployment mechanisms.

## Preview and promote
The Rollout uses `autoPromotionEnabled: false`, so promotion is a deliberate action after preview validation. Use the Argo Rollouts CLI:

```bash
kubectl-argo-rollouts get rollout demo-app-rollout -n production
kubectl-argo-rollouts promote demo-app-rollout -n production
kubectl-argo-rollouts undo demo-app-rollout -n production
```

Check the preview endpoint and application health before promotion. Confirm the active Service selector and traffic behavior after promotion.

## Pipeline integration
The pipeline in `app/argo-rollout-pipeline.yaml` illustrates image build/push, a GitOps manifest update, a manual approval, and an Argo Rollouts promotion. It contains environment-specific Azure DevOps service connection, registry, subscription, cluster, and external Git repository settings. Replace them with your own configuration and move deployment credentials into protected service connections/secret variables.

The current pipeline references `argo-rollout/rollout.yaml` in the separately cloned GitOps repository. Ensure that repository actually contains this path or update the pipeline to the path where you store the Rollout manifest (the local sample is under `manifests/rollout.yaml`). Do not assume this local directory is automatically the remote GitOps repository.

## Known limitations to review
- Both Services initially select `app: demo-app`; Argo Rollouts manages the active/preview Service selectors using ReplicaSet hashes during rollout. Verify controller reconciliation and endpoints rather than manually pinning these selectors.
- Ingress rewrites `/staging` to `/`; verify the Flask app and controller behavior with the chosen path handling.
- Pin image tags/digests and tool/controller versions.
- Add a dedicated analysis/health strategy, PodDisruptionBudget, NetworkPolicy, resource/security settings, and TLS as appropriate before production use.
- The pipeline's manual validation is an example; use protected environments and approval checks for production promotion.
