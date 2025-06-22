Here is the content converted into a proper `README.md` file format:

````markdown
# EBS Volume Test on EKS Pod

This guide demonstrates how to interact with an AWS EBS volume mounted inside a Kubernetes Pod running on EKS.

## 1. Create a File Inside the Pod

Execute the following command to create a test file on the mounted EBS volume:

```bash
kubectl exec -it ebs-app -- sh -c "echo 'This is a test from the nginx pod!' > /data/demo.txt"
````

> **Note:** We use `sh -c` because the `nginx` container image typically does not include `bash`.

---

## 2. Verify the File Exists

Read the contents of the created file to confirm that the write operation was successful:

```bash
kubectl exec -it ebs-app -- cat /data/demo.txt
```

**Expected Output:**

```
This is a test from the nginx pod!
```

---

## 3. List the Contents of the Directory

To list all files in the mounted `/data` directory:

```bash
kubectl exec -it ebs-app -- ls -l /data/
```

This verifies that the file `demo.txt` exists and that the volume is functioning correctly.

---

## Summary

You've now:

* Created a file on an EBS volume from inside a pod.
* Verified data persistence.
* Explored the contents of the mounted volume.

```

Let me know if you'd like me to save this into an actual `README.md` file or export it as a PDF.
```
