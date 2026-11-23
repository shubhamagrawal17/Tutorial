# 🚀 FastAPI Project – Push to GitHub (Step-by-Step Guide)

This guide explains how to push a local FastAPI project to GitHub from scratch.

---

## 📁 Prerequisites

Make sure you have:

* Git installed → [https://git-scm.com/](https://git-scm.com/)
* GitHub account → GitHub
* Your project folder ready (e.g., `fastapi_project`)

---

## 📂 Step 1: Navigate to Project Folder

Open terminal / PowerShell:

```bash
cd path/to/your-project
```

Example:

```bash
cd fastapi_project
```

---

## 🔧 Step 2: Initialize Git Repository

```bash
git init
```

---

## 📦 Step 3: Add Files to Git

```bash
git add .
```

---

## 📝 Step 4: Commit Your Code

```bash
git commit -m "Initial commit"
```

---

## 🌐 Step 5: Create Repository on GitHub

1. Go to GitHub
2. Click **New Repository**
3. Enter repository name (e.g., `fastapi-app`)
4. Click **Create Repository**

⚠️ Important:

* Do **NOT** select "Initialize with README"

---

## 🔗 Step 6: Add Remote Repository

Copy your GitHub repo URL and run:

```bash
git remote add origin https://github.com/<username>/<repo-name>.git
```

Example:

```bash
git remote add origin https://github.com/shubhamagrawal17/fastapi-app.git
```

---

## 🔄 Step 7: Rename Branch to Main

```bash
git branch -M main
```

---

## 🚀 Step 8: Push Code to GitHub

```bash
git push -u origin main
```

---

## ✅ Step 9: Verify

* Open your repository on GitHub
* You should see your project files uploaded 🎉

---

## ⚠️ Common Errors & Fixes

### ❌ Error: `src refspec main does not match any`

✔️ Fix:

```bash
git add .
git commit -m "Initial commit"
git branch -M main
git push -u origin main
```

---

# 🔐 Goal

Let GitHub Actions authenticate to Azure **without passwords** and push images to your **Azure Container Registry (ACR)**.

---

# 🧭 1) Create App Registration (Service Principal)

1. Go to **Azure Portal → Azure Active Directory**
2. Open **App registrations → New registration**
3. Name: `github-actions-acr`
4. Click **Register**

👉 After creation, copy:

* **Application (client) ID**
* **Directory (tenant) ID**

---

# 🔗 2) Add Federated Credential (OIDC)

1. Open your new App Registration
2. Go to **Certificates & secrets → Federated credentials**
3. Click **Add credential**
4. Choose **GitHub Actions deploying Azure resources**
5. Fill:

   * **Organization** → your GitHub username/org
   * **Repository** → your repo name
   * **Branch** → `main` (or your branch)
6. Click **Add**

👉 This links GitHub → Azure securely (no secrets)

---

# 🛡️ 3) Grant ACR Push Permission

1. Go to your **Container Registry**
2. Open **Access control (IAM)**
3. Click **Add role assignment**
4. Role: **AcrPush**
5. Assign access to: **User, group, or service principal**
6. Select your app: `github-actions-acr`
7. Save

---

# 🔑 4) Add GitHub Secrets (only 3, no passwords)

In your GitHub repo → **Settings → Secrets → Actions**

Add:

```text
AZURE_CLIENT_ID
AZURE_TENANT_ID
AZURE_SUBSCRIPTION_ID
```

👉 Values come from:

* App Registration (client + tenant)
* Azure subscription page (subscription ID)

---

# 🚀 5) Use in GitHub Actions

```yaml
- name: Azure Login (OIDC)
  uses: azure/login@v2
  with:
    client-id: ${{ secrets.AZURE_CLIENT_ID }}
    tenant-id: ${{ secrets.AZURE_TENANT_ID }}
    subscription-id: ${{ secrets.AZURE_SUBSCRIPTION_ID }}

- name: Login to ACR
  run: az acr login --name <ACR_NAME>

- name: Build Image
  run: docker build -t <ACR_NAME>.azurecr.io/fastapi-app:${{ github.sha }} .

- name: Push Image
  run: docker push <ACR_NAME>.azurecr.io/fastapi-app:${{ github.sha }}
```

---

# 💡 Example

If your registry is:

```text
myacr123.azurecr.io
```

Then:

```bash
docker build -t myacr123.azurecr.io/fastapi-app:latest .
docker push myacr123.azurecr.io/fastapi-app:latest
```

---

# ⚠️ Common mistakes

* Using wrong repo/branch in federated credential
* Forgetting **AcrPush role**
* Using `myacr123` instead of `myacr123.azurecr.io`
* Not granting permission to correct subscription

---

# 💯 Final Result

You now have:

* ❌ No passwords stored
* ✅ Secure OIDC authentication
* ✅ CI/CD pushing images to ACR

