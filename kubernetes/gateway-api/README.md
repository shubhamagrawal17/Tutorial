# Kubernetes Gateway API with Envoy Gateway

This tutorial demonstrates Gateway API using Envoy Gateway on a local Kubernetes cluster. It creates two versions of a sample HTTP application and splits traffic between them using HTTPRoute backend weights.

## Prerequisites
- Docker Desktop Kubernetes or another disposable Kubernetes cluster.
- kubectl configured for the intended cluster.
- Gateway API CRDs and an Envoy Gateway controller version compatible with the manifests.

## Files
- `gatewayclass.yaml` — registers Envoy Gateway as a Gateway API controller.
- `gateway.yaml` — defines an HTTP listener.
- `app.yaml` — deploys v1/v2 sample applications and their Services.
- `httproute.yaml` — configures weighted backend routing.

## Install the controller
The original tutorial uses fixed Gateway API and Envoy Gateway release URLs. Review the versions and compatibility matrix before installing; update them together as a separate tested maintenance change.

The original installation examples are retained in the tutorial history. Install CRDs and the controller using the official instructions for the versions selected for your cluster.

## Apply the example
From this directory, after the CRDs and controller are ready:

```bash
kubectl apply -f gatewayclass.yaml
kubectl apply -f app.yaml
kubectl apply -f gateway.yaml
kubectl apply -f httproute.yaml
```

Inspect status and events:

```bash
kubectl get gatewayclass
kubectl get gateway
kubectl get httproute
kubectl get deployments,services,pods
kubectl describe gateway demo-gateway
kubectl describe httproute demo-route
```

Wait for the Gateway and its listener to report programmed/accepted conditions before testing traffic. The local endpoint depends on the Envoy Gateway installation and the local cluster's service exposure; do not assume every environment binds it to `localhost:80`.

## Weighted routing
The HTTPRoute declares weights of 50 and 50 for the v1 and v2 Services. This expresses a relative traffic split; it is not a guarantee that every finite batch of requests will be exactly half-and-half.

## Cleanup
```bash
kubectl delete -f httproute.yaml
kubectl delete -f gateway.yaml
kubectl delete -f app.yaml
kubectl delete -f gatewayclass.yaml
```

Remove the controller and CRDs only if they were installed solely for this exercise and no other workloads use them.

## Production considerations
Use a supported Gateway API/controller version pair, explicit namespaces and policies, TLS where appropriate, health/readiness probes, resource requests/limits, pinned application image versions, and an appropriate exposure model. The manifests are demonstration resources, not production defaults.
