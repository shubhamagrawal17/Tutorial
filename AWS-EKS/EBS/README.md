# EBS Volume Test on EKS Pod

This guide demonstrates how to interact with an AWS EBS volume mounted inside a Kubernetes Pod running on EKS.

## 1. Create a File Inside the Pod

Execute the following command to create a test file on the mounted EBS volume:

```bash
kubectl exec -it ebs-app -- sh -c "echo 'This is a test from the nginx pod!' > /data/demo.txt"

2. Verify the File Exists
Read the contents of the created file to confirm that the write operation was successful:
kubectl exec -it ebs-app -- cat /data/demo.txt
Expected Output:
This is a test from the nginx pod!

3. List the Contents of the Directory
To list all files in the mounted /data directory:

kubectl exec -it ebs-app -- ls -l /data/
This verifies that the file demo.txt exists and that the volume is functioning correctly.

