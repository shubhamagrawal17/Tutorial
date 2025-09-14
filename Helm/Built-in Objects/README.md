
# Helm Template Variables Reference

This document provides an overview of commonly used Helm template objects and how to reference them.

---

## Root Object
```
{{/* Root Object  */}}
Root Object: {{ . }}
```

---

## Release Object
- **Release Name:** `{{ .Release.Name }}`
- **Release Namespace:** `{{ .Release.Namespace }}`
- **Is Upgrade:** `{{ .Release.IsUpgrade }}`
- **Is Install:** `{{ .Release.IsInstall }}`
- **Release Revision:** `{{ .Release.Revision }}`
- **Release Service:** `{{ .Release.Service }}`

---

## Chart Object
- **Chart Name:** `{{ .Chart.Name }}`
- **Chart Version:** `{{ .Chart.Version }}`
- **Chart AppVersion:** `{{ .Chart.AppVersion }}`
- **Chart Type:** `{{ .Chart.Type }}`
- **Chart Name and Version:** `{{ .Chart.Name }}-{{ .Chart.Version }}`

---

## Values Object
- **Replica Count:** `{{ .Values.replicaCount }}`
- **Image Repository:** `{{ .Values.image.repository }}`
- **Service Type:** `{{ .Values.service.type }}`

---

## Capabilities Object
- **K8s Cluster Version Major:** `{{ .Capabilities.KubeVersion.Major }}`
- **K8s Cluster Version Minor:** `{{ .Capabilities.KubeVersion.Minor }}`
- **K8s Cluster Version:** `{{ .Capabilities.KubeVersion }} ({{ .Capabilities.KubeVersion.Version }})`
- **Helm Version:** `{{ .Capabilities.HelmVersion }}`
- **Helm Version (Semver):** `{{ .Capabilities.HelmVersion.Version }}`
- **Go Compiler Version:** `{{ .Capabilities.HelmVersion.GoVersion }}`

---

## File Object
- **File Get Example:**  
  ```yaml
  {{ .Files.Get "my.config" }}
  ```
