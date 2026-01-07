---

# 📘 Tests & Coverage – Pytest (Azure DevOps YAML)

**Unified Unit Testing & Code Coverage Enforcement Stage**

---

## 📌 Purpose of This Stage

This Azure DevOps pipeline stage runs **automated unit tests** using **Pytest** and enforces a **code coverage quality gate** using **pytest-cov**.

This stage:

1. Installs application dependencies
2. Executes unit tests
3. Generates **JUnit test reports**
4. Measures **code coverage**
5. Enforces **minimum coverage (80%)**
6. Publishes results to Azure DevOps **Tests** and **Code Coverage** tabs
7. Fails the pipeline if tests fail or coverage is insufficient

---

## 🧱 YAML Breakdown (Line-by-Line)

---

## 🔹 Stage Definition

```yaml
- stage: Tests
```

* Defines a pipeline **stage** named `Tests`
* Dedicated to **unit testing and coverage validation**

```yaml
  displayName: "Unit Tests & Coverage"
```

* Friendly name shown in Azure DevOps UI

```yaml
  dependsOn: DependencyScan
```

* This stage runs **only after DependencyScan completes**
* Ensures:

  * Code passes SAST
  * Dependencies are secure
  * Then tests are executed

---

## 🔹 Job Definition

```yaml
  jobs:
  - job: TestAndCover
```

* Defines a job named `TestAndCover`
* All testing steps run on the same agent

```yaml
    displayName: "Execute Pytest with Coverage"
```

* Job name shown in pipeline UI

---

## 🐍 Python Environment Setup

```yaml
    - task: UsePythonVersion@0
```

* Azure DevOps task to configure Python runtime

```yaml
      inputs:
        versionSpec: $(pythonVersion)
```

* Uses a **pipeline variable** for Python version
* Allows consistent Python version across all stages

```yaml
      displayName: "Setup Python"
```

---

## 📦 Install Application & Test Dependencies

```yaml
    - script: |
```

* Starts a shell script block

```bash
python -m pip install --upgrade pip
```

* Ensures latest `pip` version

```bash
pip install -r requirements.txt
```

* Installs application dependencies

```bash
pip install pytest pytest-cov
```

* Installs testing tools:

  * **pytest** → test framework
  * **pytest-cov** → coverage reporting plugin

```yaml
      displayName: "Install Dependencies"
```

---

## 🧪 Run Tests with Coverage Enforcement

```yaml
    - script: |
```

* Executes tests and coverage in a single command

```bash
export PYTHONPATH=$(System.DefaultWorkingDirectory)
```

* Ensures the application root is discoverable by Python imports
* Prevents `ModuleNotFoundError`

```bash
mkdir -p reports
```

* Creates directory for test reports

---

### 🔐 Pytest Execution with Coverage Gate

```bash
pytest --junitxml=reports/junit.xml \
       --cov=app \
       --cov-report=xml:coverage.xml \
       --cov-fail-under=80
```

| Option                | Purpose                                |
| --------------------- | -------------------------------------- |
| `--junitxml`          | Generates JUnit XML for Azure DevOps   |
| `--cov=app`           | Measures coverage for `app/` directory |
| `--cov-report=xml`    | Creates coverage XML file              |
| `--cov-fail-under=80` | **Fails build if coverage < 80%**      |

👉 **This is the Quality Gate for test coverage.**

```yaml
      displayName: "Run Pytest with 80% Coverage Gate"
```

---

## 📊 Publish Test Results (Azure DevOps Tests Tab)

```yaml
    - task: PublishTestResults@2
```

* Publishes test results to Azure DevOps UI

```yaml
      condition: succeededOrFailed()
```

* Ensures test results are published **even if tests fail**
* Critical for debugging failures

```yaml
      inputs:
        testResultsFormat: JUnit
```

* Specifies JUnit test report format

```yaml
        testResultsFiles: reports/junit.xml
```

* Path to test result file

```yaml
        failTaskOnFailedTests: true
```

* Marks pipeline as **failed** if tests fail

```yaml
      displayName: "Publish Test Results"
```

📌 **Result:**
The **Tests** tab appears in Azure DevOps pipeline UI.

---

## 📈 Publish Code Coverage Results

```yaml
    - task: PublishCodeCoverageResults@2
```

* Publishes coverage data to Azure DevOps

```yaml
      inputs:
        codeCoverageTool: Cobertura
```

* Azure DevOps expects **Cobertura XML** format
* `pytest-cov` generates compatible output

```yaml
        summaryFileLocation: '$(System.DefaultWorkingDirectory)/coverage.xml'
```

* Path to coverage report

```yaml
      displayName: "Publish Coverage Results"
```

📌 **Result:**
The **Code Coverage** tab appears in Azure DevOps UI.

---

## 🏁 Final Outcome

✔ Unit tests executed
✔ Coverage measured and enforced
✔ Build fails if:

* Any test fails
* Coverage < 80%
  ✔ Test results visible in **Tests** tab
  ✔ Coverage visualized in **Code Coverage** tab

---




