

---

## 📌 Overview

This repository demonstrates how to use **Kubernetes Gateway API** with **Envoy Gateway** on **Docker Desktop Kubernetes**.

### What this demo shows:

* Installing Gateway API CRDs
* Installing Envoy Gateway
* Creating `GatewayClass`, `Gateway`, and `HTTPRoute`
* Deploying a sample application (v1 & v2)
* Splitting traffic **50% / 50%**
* Accessing the app locally via `localhost`

---

## 🧱 Architecture

```
Client (Browser / curl)
        ↓
Gateway (Envoy Load Balancer)
        ↓
HTTPRoute (50% / 50%)
        ↓
Service v1        Service v2
        ↓               ↓
Pods (v1)        Pods (v2)
```

---

## ✅ Prerequisites

* Docker Desktop
* Kubernetes enabled in Docker Desktop
* kubectl installed and configured

Verify:

```bash
kubectl get nodes
```

---

## 📂 Folder Structure

```
.
├── README.md
├── gatewayclass.yaml
├── gateway.yaml
├── httproute.yaml
└── app.yaml
```

---

## 🔹 Step 1: Install Gateway API CRDs

Gateway API resources are **not available by default** in Kubernetes.

```bash
kubectl apply -f https://github.com/kubernetes-sigs/gateway-api/releases/download/v1.0.0/standard-install.yaml
```

Verify:

```bash
kubectl get crd | grep gateway
```

---

## 🔹 Step 2: Install Envoy Gateway

Envoy Gateway is the **Gateway API controller**.

```bash
kubectl apply -f https://github.com/envoyproxy/gateway/releases/download/v1.0.2/install.yaml
```

Verify:

```bash
kubectl get pods -n envoy-gateway-system
```

Expected:

```
envoy-gateway-xxxxx   Running
```

---

## 🔹 Step 3: Create GatewayClass

### 📄 gatewayclass.yaml

```yaml
apiVersion: gateway.networking.k8s.io/v1
kind: GatewayClass
metadata:
  name: envoy
spec:
  controllerName: gateway.envoyproxy.io/gatewayclass-controller
```

Apply:

```bash
kubectl apply -f gatewayclass.yaml
```

Verify:

```bash
kubectl get gatewayclass
```

---

## 🔹 Step 4: Deploy Sample Application (v1 & v2)

We deploy **two versions** of a simple HTTP app using `hashicorp/http-echo`.

### 📄 app.yaml

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: app-v1
spec:
  replicas: 2
  selector:
    matchLabels:
      app: demo
      version: v1
  template:
    metadata:
      labels:
        app: demo
        version: v1
    spec:
      containers:
      - name: app
        image: hashicorp/http-echo
        args:
        - "-text=Hello from APP VERSION V1"
        ports:
        - containerPort: 5678
---
apiVersion: v1
kind: Service
metadata:
  name: app-v1
spec:
  selector:
    app: demo
    version: v1
  ports:
  - port: 80
    targetPort: 5678
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: app-v2
spec:
  replicas: 2
  selector:
    matchLabels:
      app: demo
      version: v2
  template:
    metadata:
      labels:
        app: demo
        version: v2
    spec:
      containers:
      - name: app
        image: hashicorp/http-echo
        args:
        - "-text=Hello from APP VERSION V2"
        ports:
        - containerPort: 5678
---
apiVersion: v1
kind: Service
metadata:
  name: app-v2
spec:
  selector:
    app: demo
    version: v2
  ports:
  - port: 80
    targetPort: 5678
```

Apply:

```bash
kubectl apply -f app.yaml
```

Verify:

```bash
kubectl get pods
kubectl get svc
```

---

## 🔹 Step 5: Create Gateway (Load Balancer)

### 📄 gateway.yaml

```yaml
apiVersion: gateway.networking.k8s.io/v1
kind: Gateway
metadata:
  name: demo-gateway
spec:
  gatewayClassName: envoy
  listeners:
  - name: http
    protocol: HTTP
    port: 80
```

Apply:

```bash
kubectl apply -f gateway.yaml
```

Verify:

```bash
kubectl get gateway
```

---

## 🔹 Step 6: Create HTTPRoute (Traffic Routing)

This route splits traffic **50% to v1 and 50% to v2**.

### 📄 httproute.yaml

```yaml
apiVersion: gateway.networking.k8s.io/v1
kind: HTTPRoute
metadata:
  name: demo-route
spec:
  parentRefs:
  - name: demo-gateway
  rules:
  - backendRefs:
    - name: app-v1
      port: 80
      weight: 50
    - name: app-v2
      port: 80
      weight: 50
```

Apply:

```bash
kubectl apply -f httproute.yaml
```

Verify:

```bash
kubectl get httproute
```

---

## 🔹 Step 7: Access Application

On **Docker Desktop**, Envoy Gateway exposes traffic on **localhost**.

```bash
curl http://localhost
```

Or open in browser:

```
http://localhost
```

---

## 🔹 Step 8: Verify Traffic Splitting

Run multiple requests:

```bash
for i in {1..20}; do curl http://localhost; done
```

Expected output (mixed):

```
Hello from APP VERSION V1
Hello from APP VERSION V2
```

> ⚠️ Traffic splitting is **statistical**, not exact per request.

---

## 🛠 Debugging Commands

```bash
kubectl logs -n envoy-gateway-system deploy/envoy-gateway
kubectl describe gateway demo-gateway
kubectl describe httproute demo-route
```

---

## 🧠 Key Learnings

* Gateway API cleanly replaces Ingress
* Envoy Gateway implements Gateway API
* Responsibilities are clearly separated:

  * `GatewayClass` → controller
  * `Gateway` → load balancer
  * `HTTPRoute` → routing logic
* Works perfectly on **local Kubernetes**

---
