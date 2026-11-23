# Repository structure

## Organization model

The repository currently contains independent tutorials at the root level. This first improvement adds a documentation layer without moving existing project directories.

```text
Tutorial/
├── README.md                     # Repository landing page
├── CONTRIBUTING.md               # Contribution and safety standards
├── docs/
│   ├── PROJECT-CATALOG.md        # Topic-based index of existing examples
│   └── REPOSITORY-STRUCTURE.md   # This document
├── tests/
│   └── test_repository_docs.py   # Dependency-free documentation checks
├── .github/
│   └── workflows/
│       └── docs-validation.yml   # PR and main-branch documentation checks
│
├── Azure and AKS examples        # Existing directories; paths preserved
├── AWS and EKS examples          # Existing directories; paths preserved
├── Kubernetes and Helm examples  # Existing directories; paths preserved
├── Argo CD and GitOps examples   # Existing directories; paths preserved
├── CI/CD and DevSecOps examples  # Existing directories; paths preserved
├── Application examples          # Existing directories; paths preserved
└── Terraform and VM examples     # Existing directories; paths preserved
```

The labels in the tree are topic descriptions, not literal directory names. Use the [project catalogue](PROJECT-CATALOG.md) for exact paths.

## Why directories are not being moved yet

Several projects contain pipeline YAML, Docker build contexts, scripts, nested applications, and relative file references. A bulk rename can silently break these integrations. Moving projects should therefore be a separate, incremental migration with a reference audit and validation for each project.

## Repository hygiene

The root `.gitignore` prevents common generated files and local secrets from being added in future commits. It does not remove files that are already tracked. Existing IDE caches, archives, databases, and other artifacts need an explicit review before deletion.

## Future migration approach

1. Confirm ownership and purpose of each top-level project.
2. Check whether archived bundles duplicate source directories or contain unique material.
3. Remove generated IDE/build artifacts only after verifying they can be recreated.
4. Move one tutorial at a time into a stable topic directory.
5. Update pipeline paths, Docker build contexts, relative links, and documentation in the same change.
6. Run the tutorial-specific validation before merging.
7. Keep a redirect or migration note when an old path is referenced externally.
