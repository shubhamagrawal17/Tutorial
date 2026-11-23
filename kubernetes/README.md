# Kubernetes tutorials

Kubernetes-focused tutorials are grouped here. Cloud-provider-specific projects remain under `azure/` and `aws/`; GitOps delivery projects such as Argo CD remain separate.

## Gateway API
- [Gateway API with Envoy Gateway](gateway-api/) — install the Gateway API CRDs and Envoy Gateway, deploy two application versions, and route traffic with weighted HTTPRoute backends.

## Helm
- [Helm tutorials and charts](helm/) — built-in template objects, named templates, boolean conditions, and environment-based conditionals.

## General workflow
1. Confirm your Kubernetes cluster context with `kubectl config current-context`.
2. Review each tutorial's README and manifests before applying anything.
3. Validate YAML and API availability against the target Kubernetes/controller versions.
4. Render Helm charts locally before installing them.
5. Use a disposable namespace or local cluster for experiments; avoid applying learning examples to production clusters.

These are independent learning exercises, not a single application or production-certified platform.
