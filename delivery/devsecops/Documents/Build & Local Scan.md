---

# 📘 Container Build & Local Scan – Docker + Trivy (Azure DevOps YAML)

**Secure Container Build with Image Vulnerability Scanning & Quality Gate**

---

## 📌 Purpose of This Stage

This Azure DevOps pipeline stage builds a **Docker container image locally** and performs a **container vulnerability scan** using **Trivy** before the image is pushed to any registry.

This stage:

1. Builds the Docker image locally
2. Scans the image for OS & library vulnerabilities
3. Generates a **JSON vulnerability report**
4. Publishes a **human-readable summary** to the pipeline UI
5. Enforces a **security quality gate**
6. Fails the pipeline on **HIGH or CRITICAL** vulnerabilities

---

## 🧱 YAML Breakdown (Line-by-Line)

---

## 🔹 Stage Definition

```yaml
- stage: ContainerScan
```

* Defines a pipeline **stage** named `ContainerScan`
* Dedicated to **container security checks**

```yaml
  displayName: "Container: Build & Scan"
```

* Friendly name shown in Azure DevOps UI

```yaml
  dependsOn: Tests
```

* This stage runs **only after unit tests and coverage pass**
* Ensures only **tested code** is containerized

---

## 🔹 Job Definition

```yaml
  jobs:
  - job: BuildAndScan
```

* Defines a job named `BuildAndScan`
* All container steps run on the same agent

```yaml
    displayName: "Docker Build and Trivy Scan"
```

* Job name shown in pipeline UI

---

## 🐳 Docker Image Build

```yaml
    - task: Docker@2
```

* Azure DevOps built-in Docker task

```yaml
      displayName: "Build Image Locally"
```

* Friendly name in pipeline UI

```yaml
      inputs:
        command: build
```

* Executes `docker build`

```yaml
        repository: $(imageName)
```

* Image repository name (pipeline variable)

```yaml
        dockerfile: 'Dockerfile'
```

* Uses the project’s `Dockerfile`

```yaml
        tags: $(Build.BuildId)
```

* Tags image with the pipeline build ID
* Ensures **unique, traceable image versions**

```yaml
        addPipelineData: false
```

* Prevents Azure DevOps labels from being added
* Keeps image metadata clean

---

## 🔍 Run Trivy Scan (JSON Report)

```yaml
    - script: |
```

* Runs Trivy inside a container

```bash
mkdir -p $(Pipeline.Workspace)/reports
```

* Creates directory for security reports

---

### 🔐 Trivy Scan Execution

```bash
docker run --rm \
  -v /var/run/docker.sock:/var/run/docker.sock \
  -v $(Pipeline.Workspace)/reports:/root/.cache \
  aquasec/trivy:latest \
  image --format json --output /root/.cache/trivy-results.json \
  $(imageName):$(Build.BuildId)
```

| Component              | Purpose                           |
| ---------------------- | --------------------------------- |
| `aquasec/trivy:latest` | Official Trivy scanner image      |
| Docker socket mount    | Allows Trivy to scan local images |
| Reports volume mount   | Persists JSON output              |
| `--format json`        | Machine-readable output           |
| `--output`             | Saves scan results                |
| `image`                | Image scan mode                   |

👉 **Why containerized Trivy?**
No local installation required. Ensures consistent scanner version across agents.

```yaml
      displayName: "Run Trivy Scan (JSON Output)"
```

---

## 📊 Generate & Publish Container Scan Summary

```yaml
    - script: |
```

* Generates a Markdown summary for pipeline UI

```bash
REPORT="$(Pipeline.Workspace)/reports/trivy-results.json"
```

* Path to Trivy JSON report

```bash
SUMMARY_FILE="$(Pipeline.Workspace)/container-summary.md"
```

* Output summary file

---

### 🔢 Vulnerability Counting

```bash
VULNS=$(jq '[.Results[]?.Vulnerabilities[]?] | length' $REPORT)
```

* Extracts total vulnerabilities across:

  * OS packages
  * Application libraries

---

### 📄 Summary Generation

```bash
echo "## 🐳 Container Security Scan (Trivy)" > "$SUMMARY_FILE"
```

* Summary header

#### ✅ No Vulnerabilities

```bash
if [ "$VULNS" -eq 0 ]; then
```

```bash
echo "✅ No vulnerabilities found in the Docker image."
```

#### ⚠️ Vulnerabilities Found

```bash
else
```

```bash
echo "⚠️ Found **$VULNS** total vulnerabilities."
```

```bash
echo "| Severity | Library | Vulnerability ID | Fixed Version |"
```

* Markdown table headers

```bash
jq -r '.Results[]?.Vulnerabilities[]? | "| \(.Severity) | \(.PkgName) | \(.VulnerabilityID) | \(.FixedVersion // "N/A") |"' $REPORT | head -n 10
```

* Displays **top 10 vulnerabilities** to keep summary readable
* Shows:

  * Severity
  * Affected package
  * CVE ID
  * Fixed version (if available)

---

### 📌 Publish Summary to Azure DevOps

```bash
echo "##vso[task.addattachment type=Distributedtask.Core.Summary;name=Container Security]$SUMMARY_FILE"
```

* Azure DevOps logging command
* Attaches summary to **Pipeline → Summary tab**

```yaml
      displayName: "Publish Container Scan Summary"
```

---

## 🚦 Trivy Security Quality Gate

```yaml
    - script: |
```

* Final enforcement step

```bash
docker run --rm \
  -v /var/run/docker.sock:/var/run/docker.sock \
  aquasec/trivy:latest \
  image --exit-code 1 --severity HIGH,CRITICAL $(imageName):$(Build.BuildId)
```

### 🔐 What This Gate Does

* Scans image again
* Fails pipeline if **HIGH or CRITICAL** vulnerabilities exist
* Ensures **unsafe images never reach a registry**

```yaml
      displayName: "Trivy Security Gate (Fail on High/Critical)"
```

---

## 🏁 Final Outcome

✔ Docker image built locally
✔ Image scanned for vulnerabilities
✔ JSON report generated
✔ Clear security summary in pipeline UI
✔ Pipeline fails on HIGH / CRITICAL issues
✔ Only secure images proceed further

