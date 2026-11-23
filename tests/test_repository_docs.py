"""Dependency-free checks for repository documentation and platform migrations."""

from pathlib import Path
import re
import unittest
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
MARKDOWN_LINK = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")


def local_targets(markdown_path: Path):
    content = markdown_path.read_text(encoding="utf-8")
    for raw_target in MARKDOWN_LINK.findall(content):
        target = raw_target.strip()
        if not target or target.startswith(("#", "http://", "https://", "mailto:", "tel:")):
            continue
        target = target.split("#", 1)[0].split("?", 1)[0]
        if target:
            yield (markdown_path.parent / unquote(target)).resolve()


class RepositoryDocumentationTests(unittest.TestCase):
    def test_required_entry_points_exist(self):
        for path in [
            ROOT / "README.md", ROOT / "CONTRIBUTING.md",
            ROOT / "docs" / "PROJECT-CATALOG.md",
            ROOT / "docs" / "REPOSITORY-STRUCTURE.md",
            ROOT / "azure" / "README.md", ROOT / "aws" / "README.md", ROOT / "kubernetes" / "README.md", ROOT / "gitops" / "README.md",
        ]:
            with self.subTest(path=path):
                self.assertTrue(path.exists())

    def test_documentation_links_resolve(self):
        documents = [
            ROOT / "README.md", ROOT / "CONTRIBUTING.md",
            ROOT / "docs" / "PROJECT-CATALOG.md",
            ROOT / "docs" / "REPOSITORY-STRUCTURE.md",
            ROOT / "azure" / "README.md", ROOT / "aws" / "README.md", ROOT / "kubernetes" / "README.md",
            ROOT / "kubernetes" / "helm" / "README.md", ROOT / "kubernetes" / "gateway-api" / "README.md",
            ROOT / "gitops" / "README.md", ROOT / "gitops" / "argocd" / "README.md",
            ROOT / "gitops" / "argocd" / "flask-app" / "README.md",
            ROOT / "gitops" / "argocd" / "gitops-repo" / "README.md",
            ROOT / "gitops" / "argocd" / "blue-green-rollouts" / "README.md",
            ROOT / "aws" / "elastic-beanstalk" / "nodejs-sample" / "README.md",
        ]
        for document in documents:
            for target in local_targets(document):
                with self.subTest(document=document, target=target):
                    self.assertTrue(target.exists(), f"Broken link: {target}")

    def test_azure_projects_use_standardized_layout(self):
        expected = [
            "azure/aks/nginx-ingress", "azure/aks/keyvault-aspnet",
            "azure/key-vault/aspnet-sample", "azure/aks/cert-manager-letsencrypt",
            "azure/terraform/infra-as-code", "azure/devops-agent-vm",
            "azure/aks/troubleshooting/AKS-Deployment-Issue.yaml",
            "azure/key-vault/azure-sql-local-dotnet.md",
        ]
        for path in expected:
            with self.subTest(path=path):
                self.assertTrue((ROOT / path).exists(), f"Missing migrated path: {path}")

    def test_old_azure_root_paths_are_removed(self):
        old = [
            "AKS-Nginx", "AKS_KeyVault ASP.NET Application",
            "KeyVault with ASP.NET Application", "SSL on Aks with Lets Encrypt",
            "infra-as-code", "VM", "AKS-Deployment-Issue.yaml",
            "KeyVault+Azure SQL DB + Local Dotnet Core App.md",
        ]
        for path in old:
            with self.subTest(path=path):
                self.assertFalse((ROOT / path).exists(), f"Legacy path remains: {path}")

    def test_aws_projects_use_standardized_layout(self):
        expected = [
            "aws/README.md",
            "aws/eks/ebs/01-eks-cluster-creation.yaml",
            "aws/eks/ebs/02-ebs-storage-class.yaml",
            "aws/eks/ebs/03-pvc.yaml",
            "aws/eks/ebs/04-pod.yaml",
            "aws/eks/ebs/05-ebs-app-service.yaml",
            "aws/eks/ebs/README.md",
            "aws/elastic-beanstalk/nodejs-sample/README.md",
            "aws/elastic-beanstalk/nodejs-sample/buildspec.yml",
            "aws/elastic-beanstalk/nodejs-sample/package.json",
            "aws/elastic-beanstalk/nodejs-sample/server.js",
        ]
        for path in expected:
            with self.subTest(path=path):
                self.assertTrue((ROOT / path).exists(), f"Missing AWS tutorial path: {path}")

    def test_old_aws_root_paths_are_removed(self):
        for path in ("AWS", "AWS-EKS"):
            with self.subTest(path=path):
                self.assertFalse((ROOT / path).exists(), f"Legacy AWS path remains: {path}")

    def test_kubernetes_projects_use_standardized_layout(self):
        expected = [
            "kubernetes/README.md", "kubernetes/gateway-api/README.md",
            "kubernetes/gateway-api/app.yaml", "kubernetes/gateway-api/gateway.yaml",
            "kubernetes/gateway-api/gatewayclass.yaml", "kubernetes/gateway-api/httproute.yaml",
            "kubernetes/helm/README.md", "kubernetes/helm/built-in-objects/README.md",
            "kubernetes/helm/named-template/Chart.yaml",
            "kubernetes/helm/helm-boolean-and-demo/Chart.yaml",
            "kubernetes/helm/helm-ifelse-or-not-demo/Chart.yaml",
            "kubernetes/helm/helm-ifelse-eq-demo/Chart.yaml",
        ]
        for path in expected:
            with self.subTest(path=path):
                self.assertTrue((ROOT / path).exists(), f"Missing Kubernetes tutorial path: {path}")

    def test_old_kubernetes_root_paths_are_removed(self):
        for path in ("Kubernetes-Gateway-api", "Helm"):
            with self.subTest(path=path):
                self.assertFalse((ROOT / path).exists(), f"Legacy Kubernetes path remains: {path}")

    def test_helm_chart_metadata_exists(self):
        charts = [
            "kubernetes/helm/named-template/Chart.yaml",
            "kubernetes/helm/helm-boolean-and-demo/Chart.yaml",
            "kubernetes/helm/helm-ifelse-or-not-demo/Chart.yaml",
            "kubernetes/helm/helm-ifelse-eq-demo/Chart.yaml",
        ]
        for path in charts:
            with self.subTest(path=path):
                content = (ROOT / path).read_text(encoding="utf-8")
                self.assertIn("apiVersion: v2", content)
                self.assertIn("name:", content)
                self.assertIn("version:", content)

    def test_gitops_projects_use_standardized_layout(self):
        expected = [
            "gitops/README.md",
            "gitops/argocd/README.md",
            "gitops/argocd/flask-app/Dockerfile",
            "gitops/argocd/flask-app/azure-pipelines.yml",
            "gitops/argocd/flask-app/src/app.py",
            "gitops/argocd/gitops-repo/k8s/deployment.yaml",
            "gitops/argocd/gitops-repo/k8s/service.yaml",
            "gitops/argocd/blue-green-rollouts/README.md",
            "gitops/argocd/blue-green-rollouts/app/argo-rollout-pipeline.yaml",
            "gitops/argocd/blue-green-rollouts/manifests/rollout.yaml",
            "gitops/argocd/blue-green-rollouts/manifests/services.yaml",
            "gitops/argocd/blue-green-rollouts/manifests/ingress.yaml",
        ]
        for path in expected:
            with self.subTest(path=path):
                self.assertTrue((ROOT / path).exists(), f"Missing GitOps path: {path}")

    def test_old_argocd_root_paths_are_removed(self):
        for path in ("ArgoCD", "ArgoCD-Blue-Green-Deployment"):
            with self.subTest(path=path):
                self.assertFalse((ROOT / path).exists(), f"Legacy path remains: {path}")

    def test_gitops_catalogue_links_exist(self):
        catalogue = (ROOT / "docs" / "PROJECT-CATALOG.md").read_text(encoding="utf-8")
        for link in [
            "../gitops/README.md", "../gitops/argocd/README.md",
            "../gitops/argocd/flask-app/", "../gitops/argocd/gitops-repo/",
            "../gitops/argocd/blue-green-rollouts/",
        ]:
            with self.subTest(link=link):
                self.assertIn(f"]({link})", catalogue)

    def test_catalogue_contains_azure_aws_and_kubernetes_links(self):
        catalogue = (ROOT / "docs" / "PROJECT-CATALOG.md").read_text(encoding="utf-8")
        for link in [
            "../azure/README.md", "../azure/aks/nginx-ingress/",
            "../azure/aks/keyvault-aspnet/", "../azure/key-vault/aspnet-sample/",
            "../azure/aks/cert-manager-letsencrypt/",
            "../azure/aks/troubleshooting/AKS-Deployment-Issue.yaml",
            "../azure/terraform/infra-as-code/", "../azure/devops-agent-vm/",
            "../azure/key-vault/azure-sql-local-dotnet.md",
            "../aws/README.md", "../aws/eks/ebs/",
            "../aws/elastic-beanstalk/nodejs-sample/",
            "../kubernetes/README.md", "../kubernetes/gateway-api/", "../kubernetes/helm/",
        ]:
            with self.subTest(link=link):
                self.assertIn(f"]({link})", catalogue)

    def test_terraform_pipeline_working_directories_exist(self):
        pipeline = ROOT / "azure/terraform/infra-as-code/azure-pipelines.yml"
        content = pipeline.read_text(encoding="utf-8")
        paths = re.findall(r"workingDirectory:\s*['\"]\$\(Build\.SourcesDirectory\)/([^'\"]+)['\"]", content)
        self.assertTrue(paths)
        for path in paths:
            with self.subTest(path=path):
                self.assertTrue((ROOT / path).is_dir(), f"Missing pipeline path: {path}")

    def test_keyvault_pipeline_dockerfile_and_context_exist(self):
        pipelines = [
            ROOT / "azure/aks/keyvault-aspnet/AKS_KeyVault_ASP.NETApplication/azure-pipelines.yml",
            ROOT / "azure/key-vault/aspnet-sample/KeyVaultASP.NETApplication/azure-pipelines.yml",
        ]
        for pipeline in pipelines:
            content = pipeline.read_text(encoding="utf-8")
            for key in ("dockerfile", "buildContext"):
                match = re.search(rf"{key}:\s*['\"]\$\(Build\.SourcesDirectory\)/([^'\"]+)['\"]", content)
                self.assertIsNotNone(match, f"{key} missing from {pipeline}")
                if match:
                    target = ROOT / match.group(1)
                    self.assertTrue(target.is_file() if key == "dockerfile" else target.is_dir(), f"Invalid {key}: {target}")

    def test_elastic_beanstalk_buildspec_paths_exist(self):
        buildspec = ROOT / "aws/elastic-beanstalk/nodejs-sample/buildspec.yml"
        content = buildspec.read_text(encoding="utf-8")
        match = re.search(r"base-directory:\s*([^\s#]+)", content)
        self.assertIsNotNone(match, "Buildspec base-directory is missing")
        if match:
            self.assertTrue((ROOT / match.group(1)).is_dir(), f"Missing buildspec directory: {match.group(1)}")


if __name__ == "__main__":
    unittest.main()
