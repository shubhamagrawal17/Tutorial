---

# 📘 Dependency Scan – pip-audit (Azure DevOps YAML)

**Software Composition Analysis (SCA) for Python Dependencies**

---

## 📌 Purpose of This Stage

This Azure DevOps pipeline stage performs **Software Composition Analysis (SCA)** using **pip-audit** to identify **known vulnerabilities in Python dependencies** defined in `requirements.txt`.

This stage:

1. Scans third-party Python libraries
2. Generates a **machine-readable JSON report**
3. Creates a **human-friendly pipeline summary**
4. Enforces a **security policy**
5. Fails the pipeline on **HIGH / CRITICAL / UNKNOWN** vulnerabilities
6. Publishes raw reports for **audit & compliance**

---

## 🧱 YAML Breakdown (Line-by-Line)

---

## 🔹 Stage Definition

```yaml
- stage: DependencyScan
```

* Defines a new pipeline **stage** named `DependencyScan`
* Dedicated to dependency security scanning (SCA)

```yaml
  displayName: Dependency Security Scan (pip-audit)
```

* Friendly name shown in Azure DevOps UI

```yaml
  dependsOn: SAST
```

* This stage **runs only after the SAST stage completes**
* Ensures:

  * Source code is scanned first
  * Dependency scan runs later in the DevSecOps flow

---

## 🔹 Job Definition

```yaml
  jobs:
  - job: PipAudit
```

* Defines a job named `PipAudit`
* A job is a collection of steps running on the same agent

```yaml
    displayName: Python Dependency Vulnerability Scan
```

* Human-readable job name in pipeline UI

---

## 🐍 Python Environment Setup

```yaml
    - task: UsePythonVersion@0
```

* Azure DevOps built-in task to configure Python

```yaml
      displayName: Use Python $(pythonVersion)
```

* Uses a **pipeline variable** (`pythonVersion`)
* Allows easy version change without editing YAML

```yaml
      inputs:
        versionSpec: $(pythonVersion)
```

* Dynamically installs the specified Python version

---

## 🔍 Run pip-audit (Detection Phase)

```yaml
    - script: |
```

* Starts a Bash script block

```bash
set -euo pipefail
```

* Enables strict Bash mode:

  * `-e` → exit on errors
  * `-u` → fail on undefined variables
  * `pipefail` → detect pipeline failures

---

### 📦 Tool Installation

```bash
python -m pip install --upgrade pip
```

* Upgrades `pip` to avoid dependency resolution issues

```bash
pip install pip-audit jq
```

* Installs:

  * **pip-audit** → dependency vulnerability scanner
  * **jq** → JSON processor for parsing reports

```bash
mkdir -p reports
```

* Creates directory for storing scan results

---

### 🔐 Dependency Scan Execution

```bash
pip-audit \
  -r requirements.txt \
  --timeout 30 \
  --format json \
  --output reports/pip-audit.json || true
```

| Option                | Purpose                             |       |                                     |
| --------------------- | ----------------------------------- | ----- | ----------------------------------- |
| `-r requirements.txt` | Scans project dependencies          |       |                                     |
| `--timeout 30`        | Prevents long-running network calls |       |                                     |
| `--format json`       | Outputs structured JSON             |       |                                     |
| `--output`            | Saves report to file                |       |                                     |
| `                     |                                     | true` | Prevents immediate pipeline failure |

👉 **Why `|| true`?**
`pip-audit` exits with code `1` if vulnerabilities are found.
We allow the pipeline to continue so we can:

* Generate summaries
* Enforce custom security policies later

```yaml
      displayName: Run pip-audit Dependency Scan
```

---

## 📊 Generate & Publish Pipeline Summary

```yaml
    - script: |
```

* Generates a **Markdown summary** for Azure DevOps UI

```bash
SUMMARY_FILE="$(Pipeline.Workspace)/dependency-summary.md"
```

* Location where summary file is stored

```bash
REPORT="reports/pip-audit.json"
```

* Path to pip-audit JSON output

---

### 🔢 Count Vulnerabilities

```bash
TOTAL_VULNS=$(jq '[.dependencies[].vulns[]?] | length' $REPORT)
```

* Uses `jq` to:

  * Traverse all dependencies
  * Count **all vulnerabilities**
  * Includes any severity

---

### ✅ No Vulnerabilities Case

```bash
if [ "$TOTAL_VULNS" -eq 0 ]; then
```

```bash
echo "## ✅ Dependency Scan"
echo "No vulnerable dependencies found."
```

* Displays success message in pipeline summary

---

### ⚠️ Vulnerabilities Found Case

```bash
else
```

```bash
echo "## ⚠️ Dependency Vulnerabilities Found"
echo "Total Issues: $TOTAL_VULNS"
```

* Shows total vulnerable findings

```bash
echo "| Package | Version | CVE ID | Severity |"
```

* Creates Markdown table headers

```bash
jq -r '
  .dependencies[]
  | select(.vulns != null)
  | . as $dep
  | $dep.vulns[]
  | "| \($dep.name) | \($dep.version) | \(.id) | \(.severity // "UNKNOWN") |"
'
```

This logic:

* Iterates through vulnerable dependencies
* Extracts:

  * Package name
  * Version
  * CVE ID
  * Severity (defaults to `UNKNOWN`)

---

### 📌 Publish Summary to Azure DevOps

```bash
echo "##vso[task.addattachment type=Distributedtask.Core.Summary;name=Dependency Scan]$SUMMARY_FILE"
```

* Azure DevOps logging command
* Adds summary to **Pipeline → Summary tab**

```yaml
      displayName: Publish Dependency Summary to Pipeline
```

---

## 🚦 Enforce Dependency Security Policy

```yaml
    - script: |
```

* Security **quality gate**

```bash
REPORT="reports/pip-audit.json"
```

* Reuses scan output

```bash
BLOCK_COUNT=$(jq '[.dependencies[].vulns[]? | select(.severity | ascii_upcase | . == "HIGH" or . == "CRITICAL" or . == "UNKNOWN")] | length' $REPORT)
```

### 🔍 What This Policy Does

* Converts severity to uppercase (case-safe)
* Blocks pipeline on:

  * **HIGH**
  * **CRITICAL**
  * **UNKNOWN** (best practice for compliance)

---

### ❌ Policy Violation

```bash
if [ "$BLOCK_COUNT" -gt 0 ]; then
```

```bash
exit 1
```

* Fails the pipeline

```bash
jq -r '...'
```

* Prints detailed vulnerability list for visibility

---

### ✅ Policy Passed

```bash
echo "✅ POLICY PASSED: No blocking vulnerabilities found."
```

```yaml
      displayName: Enforce Dependency Security Policy (High/Critical/Unknown)
```

---

## 📦 Publish Raw Report (Audit & Compliance)

```yaml
    - task: PublishBuildArtifacts@1
```

* Uploads files as pipeline artifacts

```yaml
      inputs:
        pathToPublish: reports/pip-audit.json
```

* Publishes raw scan output

```yaml
        artifactName: DependencyScanReports
```

* Artifact name visible in Azure DevOps

```yaml
      displayName: Publish Dependency Scan Report
```

---

## 🏁 Final Outcome

✔ Dependency vulnerabilities scanned
✔ JSON report generated
✔ Clear Markdown summary in pipeline UI
✔ Strict security policy enforced
✔ Pipeline fails on risky dependencies
✔ Reports preserved for audit & compliance

---
