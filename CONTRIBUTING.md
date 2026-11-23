# Contributing

Thank you for helping improve this collection of DevOps and cloud tutorials.

## Scope

Contributions should make an example easier to understand, safer to run, more reproducible, or more accurate. Tutorials are independent projects; do not assume that a command or dependency applies repository-wide.

## Before opening a pull request

1. Identify the tutorial directory you are changing.
2. Read its existing README and inspect related manifests, scripts, and pipeline files.
3. Keep existing paths stable unless a change explicitly includes updates to every reference.
4. Remove local build output, IDE state, credentials, personal configuration, and unrelated files from the change.
5. Add or update documentation for prerequisites, configuration, deployment, validation, cleanup, and expected costs.
6. Validate syntax and behavior with the tools appropriate to the project.

## Tutorial documentation checklist

A useful project README should explain:

- **Purpose:** what the example demonstrates and what it does not cover.
- **Architecture:** the major components and how traffic or data flows.
- **Prerequisites:** required tools, supported versions, cloud services, and permissions.
- **Configuration:** required variables and safe ways to provide them.
- **Run instructions:** reproducible build, deployment, and verification steps.
- **Security:** identity, access, network exposure, secrets, and known limitations.
- **Cleanup:** how to remove resources safely and avoid ongoing charges.
- **Troubleshooting:** common errors and how to diagnose them.

## Security requirements

- Never commit credentials, access tokens, private keys, kubeconfigs, certificates containing private keys, or real connection strings.
- Use placeholders in examples and provide an `.env.example` or equivalent only when needed; never add a populated local secrets file.
- Do not print secrets in logs, pipeline output, HTTP responses, screenshots, or documentation.
- Prefer managed identities/workload identity and least-privilege permissions over long-lived credentials.
- Keep destructive Terraform or cloud operations separate from routine deployment and protected by explicit approval.
- Explain any intentionally insecure configuration when it is included for a controlled troubleshooting exercise.

## Infrastructure and pipeline changes

- Run formatters and validators where available (for example, `terraform fmt -check`, `terraform validate`, `helm lint`, and Kubernetes server-side dry runs against a suitable cluster).
- Do not assume a local YAML parse proves that a Kubernetes resource is valid for the installed API versions or controllers.
- Pin tool and action versions where practical.
- Use immutable image tags for release workflows.
- Include a safe cleanup path and call out billable resources.

## Pull request expectations

A pull request should:

- Have a focused title and explain the motivation.
- List the tutorials and paths affected.
- Summarize the changes and any behavior changes.
- Include validation commands and their results. If a test cannot be run, state why.
- Call out breaking changes, cloud costs, and security implications.
- Avoid unrelated formatting or renaming churn.

## Local documentation checks

The repository includes a dependency-free documentation test suite:

```bash
python -m unittest discover -s tests -v
```

The same check runs in GitHub Actions for pull requests and pushes to `main`.
