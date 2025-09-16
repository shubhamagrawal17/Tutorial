**Run the Demo**
Run Helm template command: The helm template command is used to render Helm chart templates locally and output the Kubernetes manifests (YAML files) without installing anything on a cluster.
**Render with default values (dev):**
helm template myapp .
**Switch environments:**
helm template myapp . --set env=staging
helm template myapp . --set env=prod
helm template myapp . --set env=test

