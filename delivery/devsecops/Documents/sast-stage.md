
---

# 📘 SAST Stage – Bandit (Azure DevOps YAML)

**Static Application Security Testing with Bandit, SARIF, Summary & Quality Gate**

---

## 📌 Purpose of This Stage

This Azure DevOps YAML stage performs **Static Application Security Testing (SAST)** on Python code using **Bandit**.
It:

1. Scans Python source code for security issues
2. Generates a **JSON report**
3. Converts the report to **SARIF** format (for security tooling)
4. Publishes a **human-readable summary** in the pipeline UI
5. **Fails the build** if HIGH severity issues are found
6. Uploads reports as pipeline artifacts

---

## 🧱 YAML Breakdown (Line-by-Line)

---

### 🔹 Stage Definition

```yaml
- stage: SAST
```

* Defines a pipeline **stage** named `SAST`
* Used for **Static Application Security Testing**

```yaml
  displayName: "Security: Static Analysis (Bandit)"
```

* Friendly name shown in Azure DevOps UI

```yaml
  dependsOn: []
```

* This stage **starts immediately**
* No dependency on build/test stages
  (You can change this to `dependsOn: Build` if needed)

---

### 🔹 Job Definition

```yaml
  jobs:
  - job: BanditScan
```

* Defines a job named `BanditScan`
* Jobs run inside stages

```yaml
    displayName: "Bandit Scan & Report"
```

* Human-readable job name

```yaml
    pool:
      vmImage: 'ubuntu-latest'
```

* Uses Microsoft-hosted **Ubuntu Linux agent**
* Required for Python, Bandit, jq

---

## 🐍 Python Environment Setup

```yaml
    - task: UsePythonVersion@0
```

* Azure DevOps built-in task to install Python

```yaml
      inputs:
        versionSpec: '3.11'
```

* Ensures **Python 3.11** is used (consistent runtime)

```yaml
      displayName: "Set up Python Environment"
```

* Task name shown in pipeline UI

---

## 🔍 Running Bandit Scan

```yaml
    - script: |
```

* Starts a Bash script block

```bash
python -m pip install --upgrade pip
```

* Upgrades `pip` to avoid dependency issues

```bash
pip install bandit jq
```

* Installs:

  * **Bandit** → Python SAST scanner
  * **jq** → JSON parser for shell scripts

```bash
mkdir -p reports
```

* Creates a folder to store security reports

---

### 🔐 Bandit Execution

```bash
bandit -r app -f json -o reports/bandit.json || true
```

| Part                     | Meaning                                |       |                                        |
| ------------------------ | -------------------------------------- | ----- | -------------------------------------- |
| `-r app`                 | Recursively scans the `app/` directory |       |                                        |
| `-f json`                | Output format is JSON                  |       |                                        |
| `-o reports/bandit.json` | Saves results to file                  |       |                                        |
| `                        |                                        | true` | Prevents pipeline failure at this step |

👉 **Why `|| true`?**
So reports & summaries are still generated even if vulnerabilities exist.

```yaml
      displayName: "Run Bandit Scan"
```

---

## 🔁 Convert Bandit JSON → SARIF

```yaml
    - script: |
```

* Starts conversion step

```bash
python scripts/bandit_to_sarif.py reports/bandit.json reports/bandit.sarif
```

* Converts Bandit JSON output to **SARIF format**
* SARIF is required by:

  * Azure DevOps **Scans**
  * GitHub Security
  * Microsoft Defender

```yaml
      displayName: "Convert Bandit JSON to SARIF"
```

---

## 📊 Create Pipeline Summary (Markdown)

```yaml
    - script: |
```

* This script builds a **Markdown summary**

```bash
set -euo pipefail
```

* Enables strict Bash mode:

  * `-e` → exit on error
  * `-u` → fail on undefined variables
  * `-o pipefail` → detect pipeline errors

---

### 📄 Summary File Setup

```bash
SUMMARY_FILE="$(Pipeline.Workspace)/sast-summary.md"
```

* Creates summary file in pipeline workspace

```bash
REPORT="reports/bandit.json"
```

* Points to Bandit JSON report

```bash
TOTAL_ISSUES=$(jq '.results | length' $REPORT)
```

* Counts total vulnerabilities using `jq`

---

### ✅ No Issues Found Case

```bash
if [ "$TOTAL_ISSUES" -eq 0 ]; then
```

```bash
echo "## ✅ SAST Scan Results: Bandit" > "$SUMMARY_FILE"
echo "No high-risk security issues were detected in the source code." >> "$SUMMARY_FILE"
```

* Displays **success message** in pipeline UI

---

### ❌ Issues Found Case

```bash
else
```

```bash
echo "## ❌ SAST Security Issues: Bandit" > "$SUMMARY_FILE"
```

* Header for failed scan

```bash
echo "Found **$TOTAL_ISSUES** issues that require attention." >> "$SUMMARY_FILE"
```

* Shows issue count

```bash
echo "| Severity | Issue | File | Line |" >> "$SUMMARY_FILE"
```

* Markdown table header

```bash
jq -r '.results[] | "| \(.issue_severity) | \(.issue_text) | \(.filename) | \(.line_number) |"' $REPORT >> "$SUMMARY_FILE"
```

* Converts JSON findings into table rows

---

### 📌 Attach Summary to Azure DevOps UI

```bash
echo "##vso[task.addattachment type=Distributedtask.Core.Summary;name=SAST Scan Results]$SUMMARY_FILE"
```

* Azure DevOps logging command
* Adds summary under **Pipeline → Summary tab**

```yaml
      displayName: "Publish SAST Summary to Dashboard"
```

---

## 🚦 Quality Gate (Fail on HIGH)

```yaml
    - script: |
```

```bash
HIGH_COUNT=$(jq '[.results[] | select(.issue_severity == "HIGH")] | length' reports/bandit.json)
```

* Counts only **HIGH severity** vulnerabilities

```bash
if [ "$HIGH_COUNT" -gt 0 ]; then
```

* If any HIGH issue exists → fail pipeline

```bash
exit 1
```

* Marks build as **FAILED**

```bash
echo "✅ SECURITY GATE PASSED: No HIGH severity issues found."
```

* Success message if clean

```yaml
      displayName: "Check Quality Gate (Fail on HIGH)"
```

---

## 📦 Publish Artifacts

```yaml
    - task: PublishBuildArtifacts@1
```

* Azure DevOps task to upload files

```yaml
      inputs:
        pathToPublish: 'reports'
```

* Uploads `reports/` directory

```yaml
        artifactName: 'CodeAnalysisLogs'
```

* Artifact name shown in pipeline

```yaml
      displayName: "Upload Security Logs"
```

---

## 🏁 Final Outcome

✔ Static security scan executed
✔ SARIF generated for security tooling
✔ Clear Markdown summary visible in UI
✔ Pipeline **fails automatically** on HIGH issues
✔ Reports archived for audit & compliance

---

