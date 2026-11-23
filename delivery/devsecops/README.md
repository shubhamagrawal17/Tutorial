# DevSecOps pipeline examples

The Azure DevOps project contains two pipeline variants:

- `azure-pipelines.yml` — Bandit SAST, pip-audit dependency scanning, tests/coverage, container scanning, and reporting.
- `pipeline.yaml` — an expanded flow with Bandit, pip-audit, Checkov, tests, Trivy, image push, and Dev/QA/production deployment stages.

## What to review
- The primary pipeline includes explicit Bandit HIGH-severity and dependency HIGH/CRITICAL/UNKNOWN gates. The expanded variant uses `|| true` for initial scan/report generation, so verify that each required policy is enforced by a later gate and that scanner execution errors cannot be mistaken for clean results.
- Pin Trivy and other scanner versions rather than using floating `latest` images.
- Confirm the same image digest is scanned and deployed.
- Configure production approvals/checks in Azure DevOps environments.
- Ensure variable groups contain secrets and are permission-restricted.
- Validate report schemas and scanner exit behavior against the installed tool versions.

These examples are learning material. No pipeline execution or cloud deployment is implied by this documentation.
