# GitHub Actions tutorials

The day-based folders contain independent examples rather than one combined workflow:

- `Day-2/` and `Day-3/` — TypeScript/Node.js application, tests, and workflow examples.
- `Day-4/fastapi-app/` — FastAPI app, GitHub Actions, tests, and Azure OIDC/ACR walkthrough.
- `Day-5/` — FastAPI application and Kubernetes deployment example.
- `Day-6/` — self-hosted runner setup notes.
- `Day-7/fastapi_project/` — FastAPI application, workflow, tests, and Kubernetes manifests.

Read the README inside the selected project before running it. Review workflow permissions, third-party action pinning, secrets, OIDC subject/branch constraints, and Azure RBAC. Use `permissions: contents: read` by default and grant `id-token: write` only to jobs that need federated Azure login.

Some folders contain generated Python bytecode caches; those are not source files and should be removed in a separate cleanup change after confirming they are not intentionally used.
