# AWS tutorials

AWS-specific examples are grouped here. These are independent learning projects; each has its own setup requirements and AWS resource lifecycle.

## Amazon EKS
- [EKS with EBS CSI storage](eks/ebs/) — cluster configuration, EBS CSI driver, StorageClass, PVC, Pod, and Service manifests.

## AWS application hosting
- [Elastic Beanstalk Node.js sample](elastic-beanstalk/nodejs-sample/) — Express application and CodeBuild buildspec.

## Before running a tutorial
- Confirm the AWS account, region, IAM permissions, and estimated resource costs.
- Use least-privilege IAM roles and avoid long-lived access keys in source files or shell history.
- Review public load balancers, security groups, SSH access, and persistent-volume deletion policies.
- Delete billable resources when finished, taking care not to remove data that must be retained.
- Treat these examples as learning material until reviewed for production use.
