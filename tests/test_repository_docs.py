"""Dependency-free checks for repository landing-page and catalogue links."""

from pathlib import Path
import re
import unittest
from urllib.parse import unquote


ROOT = Path(__file__).resolve().parents[1]
MARKDOWN_LINK = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")


def local_targets(markdown_path: Path):
    """Yield local Markdown link targets, excluding URLs, anchors, and mailto links."""
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
        required = [
            ROOT / "README.md",
            ROOT / "CONTRIBUTING.md",
            ROOT / "docs" / "PROJECT-CATALOG.md",
            ROOT / "docs" / "REPOSITORY-STRUCTURE.md",
        ]
        for path in required:
            with self.subTest(path=path.relative_to(ROOT)):
                self.assertTrue(path.exists(), f"Missing documentation: {path}")

    def test_readme_and_catalogue_local_links_resolve(self):
        documents = [
            ROOT / "README.md",
            ROOT / "docs" / "PROJECT-CATALOG.md",
            ROOT / "docs" / "REPOSITORY-STRUCTURE.md",
            ROOT / "CONTRIBUTING.md",
        ]
        for document in documents:
            for target in local_targets(document):
                with self.subTest(document=document.relative_to(ROOT), target=target):
                    self.assertTrue(
                        target.exists(),
                        f"Broken local link in {document.relative_to(ROOT)}: {target}",
                    )

    def test_catalogue_contains_all_current_top_level_project_directories(self):
        catalogue = (ROOT / "docs" / "PROJECT-CATALOG.md").read_text(encoding="utf-8")
        project_directories = [
            "AKS-Nginx",
            "AKS_KeyVault ASP.NET Application",
            "AWS-EKS",
            "AWS",
            "ArgoCD-Blue-Green-Deployment",
            "ArgoCD",
            "CICD For AKS with Blue-Green Deployment",
            "CICD for Python App",
            "Checkly",
            "GitHub Actions",
            "Helm",
            "Java-app",
            "KeyVault with ASP.NET Application",
            "Kubernetes-Gateway-api",
            "SSL on Aks with Lets Encrypt",
            "VM",
            "aks-helm-deploy",
            "aks-helm-multi-env",
            "devsecops-azure-project",
            "eticket-App",
            "infra-as-code",
            "python-app-docker",
        ]
        for directory in project_directories:
            with self.subTest(directory=directory):
                self.assertIn(f"../{directory.replace(' ', '%20')}", catalogue)

    def test_no_absolute_machine_paths_in_new_docs(self):
        documents = [
            ROOT / "README.md",
            ROOT / "CONTRIBUTING.md",
            ROOT / "docs" / "PROJECT-CATALOG.md",
            ROOT / "docs" / "REPOSITORY-STRUCTURE.md",
        ]
        for document in documents:
            content = document.read_text(encoding="utf-8")
            self.assertNotRegex(content, r"(?m)(?:C:\\Users\\|/Users/[^/]+/|/home/[^/]+/)")

if __name__ == "__main__":
    unittest.main()
