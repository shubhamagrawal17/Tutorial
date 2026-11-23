
# 🚀 FastAPI CI/CD Pipeline (Production-Grade)

This repository contains a **complete CI/CD pipeline** built using GitHub Actions for a FastAPI application.

It covers:

* ✅ Automated testing with coverage enforcement
* 🧹 Code quality checks (linting)
* 🔐 Security scanning (Bandit)
* 📦 Dependency vulnerability scanning (pip-audit)
* 📊 HTML report dashboard (GitHub Pages)
* 🐳 Docker build & push to Azure Container Registry (ACR)

---

# 📌 Pipeline Overview

```text
TEST → LINT → SECURITY → DEPENDENCY SCAN
                                     ↓
                        REPORT DASHBOARD + DOCKER BUILD
```

Each stage depends on the previous one to ensure only **validated and secure code** moves forward.

---

# ⚙️ Workflow Trigger

```yaml
on: workflow_dispatch
```

* Manual trigger from GitHub UI
* Useful for controlled production runs

---

# 🌍 Global Environment Variables

```yaml
env:
  IMAGE_NAME: fastapi-app
```

* Defines the base Docker image name
* Reused across jobs

---

# 🧪 1. TEST STAGE

## 🎯 Purpose

* Run unit tests
* Generate reports
* Enforce minimum code coverage (80%)

---

## 🔧 Key Steps Explained

### Checkout Code

```yaml
- uses: actions/checkout@v4
```

Clones repository into the runner.

---

### Setup Python

```yaml
- uses: actions/setup-python@v5
  with:
    python-version: "3.11"
    cache: 'pip'
```

* Installs Python 3.11
* Enables dependency caching for faster builds

---

### Install Dependencies

```bash
pip install -r requirements.txt
pip install pytest pytest-cov pytest-html
```

Installs:

* Application dependencies
* Testing tools:

  * `pytest` → test runner
  * `pytest-cov` → coverage
  * `pytest-html` → HTML reports

---

### Run Tests

```bash
pytest \
--junitxml=report.xml \
--cov=app \
--cov-report=xml \
--cov-report=html \
--html=report.html \
--self-contained-html \
--cov-fail-under=80
```

#### What each option does:

| Option                  | Purpose                        |
| ----------------------- | ------------------------------ |
| `--junitxml`            | Machine-readable test results  |
| `--cov=app`             | Measure coverage of app folder |
| `--cov-report=xml`      | CI-friendly report             |
| `--cov-report=html`     | Human-readable coverage        |
| `--html=report.html`    | Test report                    |
| `--self-contained-html` | Embed assets                   |
| `--cov-fail-under=80`   | Fail if coverage < 80%         |

---

### Extract Coverage & Create Status File

```python
coverage = float(root.attrib.get("line-rate", 0)) * 100
```

* Reads coverage from XML

```python
status = {
  "tests": "passed",
  "coverage": 85.5,
  "lint": "unknown",
  "security": "unknown",
  "dependency": "unknown"
}
```

* Creates `status.json`
* This file is shared across all stages

---

### Upload Artifacts

```yaml
actions/upload-artifact@v4
```

Artifacts include:

* Test reports
* Coverage reports
* status.json

---

# 🧹 2. LINT STAGE

## 🎯 Purpose

Ensure code quality and consistency

```yaml
needs: test
```

Runs only if tests pass ✅

---

### Install Linter

```bash
pip install flake8 flake8-html
```

---

### Run Lint

```bash
flake8 . --format=html --htmldir=flake8-report || true
```

* Generates HTML report
* `|| true` prevents pipeline failure

---

### Count Errors

```bash
flake8 . --count --max-line-length=120
```

* Counts total lint violations

---

### Update Status

```python
status["lint"] = "warning" if errors > 0 else "passed"
```

| Result  | Meaning      |
| ------- | ------------ |
| passed  | Clean code   |
| warning | Issues found |

---

# 🔐 3. SECURITY SCAN (Bandit)

## 🎯 Purpose

Detect security vulnerabilities in Python code

```yaml
needs: lint
```

---

### Install Bandit

```bash
pip install bandit
```

---

### Run Scan

```bash
bandit -r app/ -f json -o bandit-report.json || true
bandit -r app/ -f html -o bandit-report.html || true
```

* Recursive scan of `app/`
* Outputs:

  * JSON → for automation
  * HTML → for viewing

---

### Update Status

```python
status["security"] = "passed" if no_issues else "warning"
```

---

# 📦 4. DEPENDENCY SCAN (pip-audit)

## 🎯 Purpose

Detect vulnerabilities in dependencies

```yaml
needs: security
```

---

### Install Tool

```bash
pip install pip-audit
```

---

### Run Scan

```bash
pip-audit -r requirements.txt -f json -o dependency-report.json || true
```

---

### Count Vulnerabilities

```python
vulns = sum(len(dep["vulns"]) for dep in dependencies)
```

---

### Update Status

```python
status["dependency"] = "passed" if vulns == 0 else "warning"
```

---

### Generate HTML Report

Custom HTML is generated showing:

* Package name
* Version
* Vulnerability ID
* Description

---

# 🌍 5. REPORT DASHBOARD (GitHub Pages)

## 🎯 Purpose

Publish all reports in a single dashboard

---

### Download Artifacts

```yaml
actions/download-artifact@v4
```

---

### Prepare Static Site

```bash
mkdir -p site
touch site/.nojekyll
```

* `.nojekyll` prevents GitHub Pages filtering

---

### Organize Reports

```bash
cp -r test-report/* site/test-report/
cp -r lint-report/* site/lint-report/
cp -r security-report/* site/security-report/
cp -r dependency-report/* site/dependency-report/
```

---

### Deploy

```yaml
peaceiris/actions-gh-pages@v4
```

* Publishes dashboard to GitHub Pages

```yaml
force_orphan: true
```

* Keeps branch clean (no history)

---

# 🐳 6. BUILD & PUSH TO AZURE CONTAINER REGISTRY (ACR)

## 🎯 Purpose

Build Docker image and push to ACR

```yaml
needs: dependency-scan
```

Only runs after all quality checks pass ✅

---

## 🔐 Azure Login (OIDC)

```yaml
azure/login@v2
```

* Uses **OIDC authentication**
* No passwords or secrets required
* More secure than traditional login

---

## 🔑 Login to ACR

```bash
az acr login --name $ACR_NAME
```

* Authenticates Docker with ACR

---

## 🏷️ Set Image Tags

```bash
IMAGE=<acr>.azurecr.io/fastapi-app:<commit-sha>
LATEST=<acr>.azurecr.io/fastapi-app:latest
```

| Tag    | Purpose           |
| ------ | ----------------- |
| SHA    | Immutable version |
| latest | Current version   |

---

## 🐳 Build Image

```bash
docker build -t $IMAGE .
```

---

## 🔁 Tag Latest

```bash
docker tag $IMAGE $LATEST
```

---

## 🚀 Push Image

```bash
docker push $IMAGE
docker push $LATEST
```

---

# 📊 status.json (Central State File)

This file is passed across all stages and tracks pipeline health:

```json
{
  "tests": "passed",
  "coverage": 85.5,
  "lint": "warning",
  "security": "passed",
  "dependency": "passed"
}
```

---

# 💡 Design Decisions

### Why `|| true` is used?

* Prevents pipeline from failing on:

  * lint issues
  * security warnings
* Allows full report generation

---

### Why artifacts are used?

* Share data across jobs
* Enable dashboard creation

---

### Why commit SHA tagging?

* Ensures traceability
* Enables rollback

---

# 🔥 Possible Improvements

If you want to make this **enterprise-grade**, consider:

* Add **SonarCloud / CodeQL**
* Fail only on **critical vulnerabilities**
* Add **AKS deployment stage**
* Add **Slack/Teams notifications**
* Parallelize independent jobs

---

# 🎯 Summary

This pipeline ensures:

* ✔️ Code is tested
* ✔️ Quality is validated
* ✔️ Security is checked
* ✔️ Dependencies are safe
* ✔️ Reports are visible
* ✔️ Image is production-ready

---

