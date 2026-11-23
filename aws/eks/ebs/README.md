# Amazon EKS with EBS CSI storage

This tutorial provisions an EKS cluster with eksctl and demonstrates dynamic EBS-backed persistent storage using the Amazon EBS CSI driver.

## Prerequisites
- AWS CLI configured for the intended account and region.
- eksctl, kubectl, and an EKS-compatible Kubernetes client.
- IAM permissions to create EKS, EC2, networking, and EBS resources.
- A supported EKS version and the EBS CSI driver with its required IAM permissions.

## Apply the example
Review the cluster name, region, node size, SSH settings, and IAM policy in each manifest before running it.

```bash
eksctl create cluster -f 01-eks-cluster-creation.yaml
kubectl apply -f 02-ebs-storage-class.yaml
kubectl apply -f 03-pvc.yaml
kubectl apply -f 04-pod.yaml
kubectl apply -f 05-ebs-app-service.yaml
```

Check provisioning and scheduling:

```bash
kubectl get nodes
kubectl get storageclass
kubectl get pvc
kubectl get pv
kubectl get pods -o wide
kubectl get svc ebs-app-service
```

The EBS CSI driver provisions EBS volumes in an Availability Zone compatible with the scheduled workload. EBS volumes are zonal; plan pod scheduling and recovery accordingly.

## Persistence exercise
Use the commands in this folder's README to write a test file under `/data`, delete/recreate the Pod, and confirm the file remains while the PVC is retained.

## Important safety notes
- The sample node group enables SSH. Restrict access to a trusted source CIDR or disable SSH if it is not required.
- The Service is `LoadBalancer` and can provision a public-facing AWS load balancer depending on cluster/network configuration. Use a private/internal service for private workloads.
- The StorageClass uses `reclaimPolicy: Delete`. Deleting the PVC may delete the EBS volume and its data. Use `Retain` for data that must survive PVC removal and define a backup/restore plan.
- Replace `nginx:latest` with a tested immutable image tag or digest for repeatable deployments.
- Review all AWS costs and clean up the cluster and related resources when finished. Verify retained EBS volumes separately before deleting anything.
