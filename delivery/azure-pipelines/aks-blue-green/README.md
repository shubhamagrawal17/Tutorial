# ASP.NET Core CI/CD and AKS blue-green deployment

This sample contains an ASP.NET Core application, Docker build definition, Kubernetes blue/green deployment manifests, and three Azure Pipelines variants.

## Contents
- `DemoApp.csproj`, Razor Pages, and `Program.cs` — sample application.
- `Dockerfile` — container build.
- `Kubernetes-Manifests/` — blue, green, namespace, Services, and production Ingress examples.
- `azure-pipelines.yml` — .NET build/publish artifact example.
- `azure-pipelines-1.yml` — container build and Kubernetes manifest artifact example.
- `azure-pipelines-2.yml` — alternate .NET build/publish example.

## Configure
Review the pipeline pool, registry service connection, registry hostname, image repository, AKS connection, namespaces, ingress class, and deployment names. The original YAML includes environment-specific values that are examples, not portable defaults.

## Important
The three pipeline files are separate examples, not a single chained release workflow. Select the one you intend to run and verify its build context and artifact paths. The repository contains historical .NET build output under `bin/` and `obj/`; those are generated artifacts and should not be used as build inputs. Consider removing them in a dedicated cleanup change and adding them to `.gitignore`.

The blue and green manifests illustrate traffic routing; validate Service selectors, Ingress rules, health checks, readiness, and rollback behavior in a disposable cluster before using this pattern for production.
