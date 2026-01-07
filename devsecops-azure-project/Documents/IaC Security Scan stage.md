---

# 📘 IaC Security Scan – Checkov (Azure DevOps YAML)

**Static Security Analysis for Kubernetes Manifests**

---

## 📌 Purpose of This Stage

This Azure DevOps pipeline stage performs **Infrastructure as Code (IaC) security scanning** on **Kubernetes manifests** using **Checkov**.

This stage:

1. Scans Kubernetes YAML manifests for security misconfigurations
2. Detects violations of Kubernetes security best practices
3. Generates **JUnit test reports** for Azure DevOps
4. Publishes a **human-readable security summary**
5. Enforces **IaC security policies**
6. Fails the pipeline on **critical misconfigurations**

---

## 🧱 YAML Breakdown (Line-by-Line)

---

## 🔹 Stage Definition

```yaml
- stage: IaCScan
```

* Defines a pipeline **stage** named `IaCScan`
* Dedicated to **Infrastructure as Code security checks**

```yaml
  displayName: "Security: K8s Manifest Scan"
```

* Friendly name shown in Azure DevOps UI

```yaml
  #dependsOn: ContainerPush
```

* (Currently commented)
* Can be enabled to ensure:

  * Only **scanned images** are deployed
  * IaC checks run after container push

---

## 🔹 Job Definition

```yaml
  jobs:
  - job: CheckovScan
```

* Defines a job named `CheckovScan`
* Runs all Checkov steps on a single agent

```yaml
    displayName: "Checkov Static Analysis"
```

* Job name displayed in the pipeline UI

---

## 🧰 Install Checkov

```yaml
    - script: |
```

* Starts a shell script block

```bash
pip install checkov
```

* Installs **Checkov** via pip
* Checkov supports:

  * Kubernetes
  * Terraform
  * Helm
  * CloudFormation
  * ARM/Bicep

```yaml
      displayName: "Install Checkov"
```

---

## 🔍 Run Checkov Scan (Report Generation)

```yaml
    - script: |
```

```bash
mkdir -p reports
```

* Creates a directory to store scan outputs

---

### 🔐 Checkov Scan Execution

```bash
checkov -d k8s/ --output junitxml > reports/checkov-report.xml || true
```

| Flag                | Purpose                             |       |                             |
| ------------------- | ----------------------------------- | ----- | --------------------------- |
| `-d k8s/`           | Scans Kubernetes manifest directory |       |                             |
| `--output junitxml` | Generates JUnit report              |       |                             |
| `                   |                                     | true` | Allows pipeline to continue |

👉 **Why `|| true`?**
Ensures reports & summaries are generated even when violations exist.

```yaml
      displayName: "Run Checkov Scan"
```

---

## 📊 Generate & Publish IaC Summary

```yaml
    - script: |
```

```bash
SUMMARY_FILE="$(Pipeline.Workspace)/iac-summary.md"
```

* File used for Azure DevOps pipeline summary

---

### 🔁 Secondary Scan for Summary Extraction

```bash
checkov -d k8s/ --quiet --no-guide > $(Pipeline.Workspace)/checkov_raw.txt || true
```

* Runs Checkov again in CLI mode
* Produces **plain-text output** for easy parsing
* `--no-guide` removes verbose remediation text

---

### 📄 Markdown Summary Creation

```bash
echo "## 🏗️ Infrastructure as Code Scan (Checkov)" > "$SUMMARY_FILE"
```

* Summary header

```bash
echo "Reviewing Kubernetes Manifests for security misconfigurations..."
```

* Context for reviewers

```bash
grep -A 5 "Passed checks:" checkov_raw.txt
```

* Extracts:

  * Number of passed checks
  * High-level scan status

```bash
echo "##vso[task.addattachment type=Distributedtask.Core.Summary;name=IaC Security Results]$SUMMARY_FILE"
```

* Publishes summary to **Pipeline → Summary tab**

```yaml
      displayName: "Publish IaC Summary"
```

---

## 📊 Publish Results to Tests Tab

```yaml
    - task: PublishTestResults@2
```

* Publishes JUnit results to Azure DevOps

```yaml
      inputs:
        testResultsFormat: 'JUnit'
```

* Specifies JUnit format

```yaml
        testResultsFiles: 'reports/checkov-report.xml'
```

* Path to Checkov JUnit report

```yaml
        testRunTitle: 'Checkov IaC Scan'
```

* Friendly name shown in **Tests** tab

```yaml
      displayName: "Display IaC Results in Tests Tab"
```

📌 **Result:**
IaC violations appear as **test failures** in Azure DevOps.

---

## 🚦 Enforce IaC Security Policy (Quality Gate)

```yaml
    - script: |
```

```bash
checkov -d k8s/ --check CKV_K8S_1,CKV_K8S_2
```

### 🔐 What This Gate Does

* Runs Checkov **without soft-fail**
* Enforces **specific critical checks**
* Fails pipeline if violations are found

| Example Check | Description                     |
| ------------- | ------------------------------- |
| `CKV_K8S_1`   | Containers must not run as root |
| `CKV_K8S_2`   | Missing security context        |

👉 These checks can be customized per organization policy.

```yaml
      displayName: "Enforce IaC Policy"
```

---

## 🏁 Final Outcome

✔ Kubernetes manifests scanned
✔ Security misconfigurations detected early
✔ Results visible in **Tests** tab
✔ Clear summary in pipeline UI
✔ Pipeline fails on critical violations
✔ IaC security enforced before deployment

---


