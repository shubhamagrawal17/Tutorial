Below is a **production-quality `README.md`** you can **copy-paste directly into your Git repository**.
It is **interview-ready**, explains **each pipeline stage**, **why it exists**, and **what risk it mitigates**.

---

# 🚀 DevSecOps CI/CD Pipeline on Azure DevOps

This repository demonstrates a **job-ready DevSecOps pipeline** implemented using **Azure DevOps**, following **shift-left security** and **fail-fast principles**.

The pipeline integrates **security, quality, and delivery** into every stage of the software lifecycle.

---

## 🧠 High-Level Pipeline Flow

```
SAST (Bandit)
→ Dependency Scan (pip-audit)
→ Unit Tests & Coverage
→ Build & Push Docker Image
→ Container Security Scan (Trivy + SARIF)
```

Each stage exists to **reduce risk as early as possible**.

---

## 🔐 Stage 1: SAST – Static Application Security Testing (Bandit)

### What this stage does

* Scans **Python source code**
* Detects insecure coding patterns (e.g. hardcoded secrets, unsafe functions)

### Tool used

* **Bandit**

### Why this stage exists

* Prevents insecure code from ever entering the pipeline
* Catches issues **before dependencies, builds, or deployments**
* Implements **shift-left security**

### What happens if it fails

* Pipeline stops immediately
* No tests, builds, or deployments are executed

### Risk mitigated

* Code-level vulnerabilities
* Insecure development practices

---

## 🔗 Stage 2: Dependency Security Scan (pip-audit)

### What this stage does

* Scans `requirements.txt`
* Checks Python dependencies against known CVEs

### Tool used

* **pip-audit**

### Why this stage exists

* Most modern attacks come from **vulnerable dependencies**
* Protects against **supply-chain attacks**
* Ensures only secure libraries are allowed

### What happens if it fails

* Pipeline fails fast
* Prevents vulnerable dependencies from reaching runtime

### Risk mitigated

* Known CVEs
* End-of-life or unpatched libraries

---

## 🧪 Stage 3: Unit Tests & Code Coverage

### What this stage does

* Runs automated unit tests using `pytest`
* Generates:

  * JUnit test reports
  * Code coverage reports

### Tools used

* **pytest**
* **pytest-cov**

### Why this stage exists

* Ensures application correctness
* Prevents broken or untested code from being packaged
* Provides measurable quality metrics

### Outputs

* Test results (JUnit)
* Coverage reports (Cobertura XML)

### Risk mitigated

* Functional defects
* Regressions
* Untested code paths

---

## 🐳 Stage 4: Build & Push Docker Image (ACR)

### What this stage does

* Builds a Docker image
* Pushes the image to **Azure Container Registry (ACR)**

### Tool used

* **Docker@2 (buildAndPush)**

### Why this stage exists

* Produces a **single immutable artifact**
* Ensures the same image is used for scanning and deployment
* Avoids “works on my machine” issues

### Key design decision

* **Build and push occur in the same job**
* This avoids Azure DevOps agent isolation issues

### Risk mitigated

* Artifact drift
* Inconsistent builds

---

## 🛡️ Stage 5: Container Security Scan (Trivy + SARIF)

### What this stage does

* Scans the container image stored in ACR
* Detects OS and dependency vulnerabilities
* Generates a **SARIF security report**

### Tool used

* **Trivy**

### Why this stage exists

* Containers are the **runtime attack surface**
* Ensures only secure images are deployed
* Enforces security gates at the artifact level

### Output

* `trivy.sarif` file
* Uploaded as **CodeAnalysisLogs**

### Security integration

* SARIF is ingested by **Azure DevOps Advanced Security**
* Findings appear in:

  ```
  Pipelines → Run → Security → Code Analysis
  ```

### Risk mitigated

* Runtime vulnerabilities
* High / Critical CVEs in base images or packages

---

## 📊 SARIF & Azure DevOps Security Tab

### What is SARIF

* **Static Analysis Results Interchange Format**
* Industry-standard format for security findings

### Why SARIF is used

* Tool-agnostic
* Native support in Azure DevOps
* Enables centralized security visibility

### Important note

* Azure DevOps shows SARIF results **only if vulnerabilities exist**
* A clean scan produces **no Security tab findings**

---

## 🔒 Security Philosophy Used

| Principle           | Implementation                      |
| ------------------- | ----------------------------------- |
| Fail fast           | Pipeline stops on security failures |
| Shift left          | Security before build & deploy      |
| Least privilege     | ACR access via service connection   |
| Immutable artifacts | Same image scanned & deployed       |
| Visibility          | SARIF + Azure DevOps Security tab   |

---

## 📄 Resume-Ready Summary

> Built an enterprise-grade DevSecOps CI/CD pipeline on Azure DevOps integrating SAST, dependency scanning, automated testing, container security scanning with Trivy, SARIF reporting, and security gates using Azure Container Registry.


## ✅ Key Takeaway

This pipeline mirrors **real enterprise DevSecOps practices**, not a toy example:

* Security is enforced early
* Artifacts are immutable
* Results are visible and auditable
* Failures are intentional and meaningful

---
Yes — **you can use almost the same DevSecOps tools for Node.js**, with a few **language-specific swaps**.
This is exactly how **real multi-language pipelines** are designed.

---


## 🔁 Python → Node.js Tool Mapping

| Pipeline Stage  | Python Tool | Node.js Tool             | Same Concept? |
| --------------- | ----------- | ------------------------ | ------------- |
| SAST            | Bandit      | **ESLint** / **Semgrep** | ✅             |
| Dependency Scan | pip-audit   | **npm audit**            | ✅             |
| Unit Tests      | pytest      | **Jest** / Mocha         | ✅             |
| Coverage        | pytest-cov  | Jest coverage            | ✅             |
| Container Build | Docker      | Docker                   | ✅             |
| Container Scan  | **Trivy**   | Trivy                    | ✅             |
| SARIF Upload    | SARIF       | SARIF                    | ✅             |

👉 **Trivy stays exactly the same** (language-agnostic).

---


