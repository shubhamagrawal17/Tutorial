# Helm tutorials

This directory contains small Helm charts and template reference examples.

## Tutorials

| Directory | Topic |
|---|---|
| [built-in-objects](built-in-objects/) | Helm root, Release, Chart, Values, Capabilities, and Files objects |
| [named-template](named-template/) | Reusable named template and Deployment |
| [helm-boolean-and-demo](helm-boolean-and-demo/) | Boolean condition combined with environment matching |
| [helm-ifelse-or-not-demo](helm-ifelse-or-not-demo/) | `if`, `or`, and `not` template functions |
| [helm-ifelse-eq-demo](helm-ifelse-eq-demo/) | Environment selection using `eq` |

## Validate and render
Run from each chart directory:

```bash
helm lint .
helm template demo-release .
```

For the environment-driven examples:

```bash
helm template demo-release ./helm-ifelse-eq-demo --set env=staging
helm template demo-release ./helm-boolean-and-demo --set env=staging
helm template demo-release ./helm-ifelse-or-not-demo --set environment=prod
```

Render output is YAML; inspect it before installing. These charts are teaching examples and may intentionally omit production requirements such as probes, resource limits, security contexts, pinned image digests, and configurable names.

## Chart conventions
- Each deployable chart has a `Chart.yaml`, `values.yaml`, and `templates/` directory.
- Keep values configurable instead of hardcoding environment-specific settings.
- Run `helm lint` and render representative values for each conditional branch.
- Use schema validation and CI chart tests when charts become operationally important.
