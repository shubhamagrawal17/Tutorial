# 🚀 GitHub Actions Self-Hosted Runner on AKS (Step-by-Step Guide)

* GitHub Actions job runs on **self-hosted runner**
* Runner runs as a **pod inside AKS**
* Full CI runs **inside your cluster**

---


# ⚙️ STEP 1 — Create AKS Cluster

```bash
az login
```

```bash
az group create --name aks-rg --location eastus
```

```bash
az aks create --resource-group aks-rg --name myAKSCluster --location eastus --node-count 1 --node-vm-size Standard_D2s_v3 --enable-managed-identity --generate-ssh-keys
```

---

# ⚙️ STEP 2 — Connect to Cluster

```bash
az aks get-credentials --resource-group aks-rg --name myAKSCluster --overwrite-existing
```

```bash
kubectl get nodes
```

---

# STEP 3 — Install cert-manager (MANDATORY) - ARC needs TLS certificates for secure communication inside Kubernetes

```bash
kubectl apply -f https://github.com/cert-manager/cert-manager/releases/latest/download/cert-manager.crds.yaml
```

```bash
helm repo add jetstack https://charts.jetstack.io
```

```bash
helm repo update
```

```bash
helm install cert-manager jetstack/cert-manager --namespace cert-manager --create-namespace
```

```bash
kubectl get pods -n cert-manager
```

👉 Wait until all pods are **Running**

---

---

# 🔐 STEP 4 — Create GitHub PAT

Go to GitHub:

👉 Settings → Developer Settings → **Tokens (classic)**

Permissions:

* repo
* workflow

---

# 🔐 STEP 5 — Create Kubernetes Secret

```bash
kubectl create secret generic controller-manager --namespace actions-runner-system --from-literal=github_token=YOUR_PAT_HERE
```

# ⚙️ STEP 6 — Install  Actions Runner Controller (ARC) - Actions Runner Controller is a Kubernetes operator that automatically creates and manages GitHub Actions runners as pods inside the cluster

Using Actions Runner Controller

```bash
helm repo add actions-runner-controller https://actions-runner-controller.github.io/actions-runner-controller
```

```bash
helm repo update
```

```bash
helm install arc actions-runner-controller/actions-runner-controller --namespace actions-runner-system --create-namespace
```

```bash
kubectl get pods -n actions-runner-system
```

---
---

# 🏃 STEP 7 — Create Runner Deployment

Create file: `runner.yaml`

```yaml
apiVersion: actions.summerwind.dev/v1alpha1
kind: RunnerDeployment
metadata:
  name: aks-runner
  namespace: actions-runner-system
spec:
  replicas: 1
  template:
    spec:
      repository: YOUR_USERNAME/YOUR_REPO
```

Apply:

```bash
kubectl apply -f runner.yaml
```

```bash
kubectl get pods -n actions-runner-system
```

---

# ⚙️ STEP 8 — Add GitHub Workflow

Create:

```
.github/workflows/ci.yml
```

```yaml
name: AKS Self Hosted CI

on:
  push:
    branches: [ main ]

jobs:
  build:
    runs-on: self-hosted

    steps:
      - uses: actions/checkout@v4
      - run: echo "Running inside AKS 🚀"
```

---

# 🚀 STEP 9 — Trigger Pipeline

```bash
git add .
```

```bash
git commit -m "test aks runner"
```

```bash
git push
```

👉 Go to GitHub → Actions tab
👉 You’ll see job running on **self-hosted runner**

---

# 🔍 STEP 10 — Verify Inside AKS

```bash
kubectl get pods -n actions-runner-system
```

```bash
kubectl logs -n actions-runner-system <runner-pod-name>
```

---

# 🧹 STEP 11 — CLEANUP (IMPORTANT 💸)

```bash
az group delete --name aks-rg --yes --no-wait
```
