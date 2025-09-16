````markdown
# Helm if/else with `eq` Demo

This chart demonstrates how to use `if/else` with the `eq` function in Helm templates.

---

## Run the Demo

### 1. Helm Template Command
The `helm template` command is used to **render Helm chart templates locally** and output the **Kubernetes manifests (YAML files)** without installing anything on a cluster.

---

### 2. Render with Default Values (`dev`)
```bash
helm template myapp .
````

---

### 3. Switch Environments

Render the template with different values by overriding `env`:

```bash
helm template myapp . --set env=staging
helm template myapp . --set env=prod
helm template myapp . --set env=test
```

---

## Example Output

* With `env=dev`:

  ```yaml
  environment: |-
    Development Environment
  ```

* With `env=staging`:

  ```yaml
  environment: |-
    Staging Environment
  ```

* With `env=prod`:

  ```yaml
  environment: |-
    Production Environment
  ```

* With `env=test` (or anything else):

  ```yaml
  environment: |-
    Unknown Environment
  ```

