## 💾 Writing to EBS Volume from a Pod

### ✅ Create a File on the Mounted EBS Volume

Use the following command to create a file inside the `ebs-app` pod:

```bash
kubectl exec -it ebs-app -- sh -c "echo 'This is a test from the nginx pod!' > /data/demo.txt"
```

### ✅ Verify the File Exists

```bash
kubectl exec -it ebs-app -- cat /data/demo.txt
```

**Expected Output:**

```
This is a test from the nginx pod!
```

---

### 📂 List Contents of the `/data/` Directory

```bash
kubectl exec -it ebs-app -- ls -l /data/
```

---

## 🔄 Migrate to Pod Identity (EKS)

To migrate your EKS cluster to use Pod Identity:

```bash
eksctl utils migrate-to-pod-identity --cluster my-eks-cluster --region ap-south-1 --approve
```

### 🛠️ What This Command Does:

* Installs the `eks-pod-identity-agent` addon (if not already present).
* Updates IAM trust policies for:

  * `aws-ebs-csi-driver`
  * `vpc-cni` (if detected using IRSA)
* Simplifies trust policies by removing tight coupling with OIDC provider URL.
* Reconfigures the addons to use **Pod Identity Associations**.

---
