
# Argo CD Installation — Step-by-Step

## 1. Create the `argocd` Namespace
```bash
kubectl create namespace argocd
````

## 2. Install Argo CD

```bash
kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml
```

## 3. Expose Argo CD Server (LoadBalancer)

```bash
kubectl patch svc argocd-server -n argocd -p "{\"spec\": {\"type\": \"LoadBalancer\"}}"
```

## 4. Get Argo CD Server External IP

```bash
kubectl get svc -n argocd argocd-server
```

## 5. Get Initial Admin Password

```bash
kubectl get secret argocd-initial-admin-secret -n argocd -o yaml
```

## 6. Decode the Password (PowerShell Example)

```powershell
[System.Text.Encoding]::UTF8.GetString([System.Convert]::FromBase64String("bDg0Wm5EVXlzTEE2R0NmbA=="))
```

## 7. Log in to Argo CD Server & Add Cluster

```bash
argocd login 4.213.212.101
argocd cluster add my-aks-cluster --insecure
```

## 8. Verify Cluster Contexts

```bash
kubectl config get-contexts
```

## Install Argo Rollouts

```bash
kubectl create namespace argo-rollouts
```
```bash
kubectl apply -n argo-rollouts -f https://github.com/argoproj/argo-rollouts/releases/latest/download/install.yaml
```
## . Create Namespace where Resources will be deployed.

```bash
kubectl create namespace production
```

## Install Nginx Ingress Controller

```bash
helm repo add ingress-nginx https://kubernetes.github.io/ingress-nginx
```
```bash
helm repo update
```
```bash
helm install ingress-nginx ingress-nginx/ingress-nginx --namespace ingress-nginx --create-namespace --set controller.replicaCount=2 --set controller.nodeSelector."kubernetes\.io/os"=linux  --set defaultBackend.nodeSelector."kubernetes\.io/os"=linux
```

## How to verify which service your application is pointing to

## Check the Rollout configuration

```bash
kubectl get rollout -n production
```
```bash
kubectl describe rollout <rollout-name>
```
---
```
