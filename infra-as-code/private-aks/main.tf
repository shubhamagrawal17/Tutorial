### Retrive Vnet Ids

data "azurerm_application_gateway" "appgateway"{
  name = "ApplicationGateway1"
  resource_group_name = var.RESOURCE_GROUP_NAME
}
data "azurerm_subnet" "aks-subnet" {
  name                 = "aks-subnet"
  virtual_network_name = "aks-vnet"
  resource_group_name  = var.RESOURCE_GROUP_NAME
}
data "azurerm_virtual_network" "aks-vnet" {
  name                = "aks-vnet"
  resource_group_name = var.RESOURCE_GROUP_NAME
}
data "azurerm_virtual_network" "acr-vnet" {
  name                = "acr-vnet"
  resource_group_name = var.RESOURCE_GROUP_NAME
}
data "azurerm_virtual_network" "agent-vnet" {
  name                = "agent-vnet"
  resource_group_name = var.RESOURCE_GROUP_NAME
}
data "azurerm_container_registry" "acr" {
  name                = "myacr17911"
  resource_group_name = var.RESOURCE_GROUP_NAME
}
data "azurerm_subnet" "appgw-subnet" {
  name                 = "appgw-subnet"
  virtual_network_name = "aks-vnet"
  resource_group_name  = var.RESOURCE_GROUP_NAME
}
### DNS zone
resource "azurerm_private_dns_zone" "aks" {
  name                = "privatelink.centralindia.azmk8s.io"
  resource_group_name = var.RESOURCE_GROUP_NAME
}

resource "azurerm_private_dns_zone_virtual_network_link" "aks" {
  name                  = "pdzvnl-aks"
  resource_group_name   = var.RESOURCE_GROUP_NAME
  private_dns_zone_name = azurerm_private_dns_zone.aks.name
  virtual_network_id    = data.azurerm_virtual_network.aks-vnet.id
}

resource "azurerm_private_dns_zone_virtual_network_link" "aks-acr" {
  name                  = "pdzvnl-aksacr"
  resource_group_name   = var.RESOURCE_GROUP_NAME
  private_dns_zone_name = azurerm_private_dns_zone.aks.name
  virtual_network_id    = data.azurerm_virtual_network.acr-vnet.id
}
resource "azurerm_private_dns_zone_virtual_network_link" "aks-agent" {
  name                  = "pdzvnl-aksagent"
  resource_group_name   = var.RESOURCE_GROUP_NAME
  private_dns_zone_name = azurerm_private_dns_zone.aks.name
  virtual_network_id    = data.azurerm_virtual_network.agent-vnet.id
}

### Identity
resource "azurerm_user_assigned_identity" "aks-access" {
  name                = "aks-access"
  resource_group_name = var.RESOURCE_GROUP_NAME
  location            = var.LOCATION
}
### Identity role assignment
resource "azurerm_role_assignment" "dns_contributor" {
  scope                = azurerm_private_dns_zone.aks.id
  role_definition_name = "Private DNS Zone Contributor"
  principal_id         = azurerm_user_assigned_identity.aks-access.principal_id
}

resource "azurerm_role_assignment" "network_contributor" {
  scope                = data.azurerm_virtual_network.aks-vnet.id
  role_definition_name = "Network Contributor"
  principal_id         = azurerm_user_assigned_identity.aks-access.principal_id
}

resource "azurerm_role_assignment" "Aks-AcrPull" {
  scope                = data.azurerm_container_registry.acr.id
  role_definition_name = "AcrPull"
  principal_id         = azurerm_kubernetes_cluster.akscluster.kubelet_identity.0.object_id
}
 resource "azurerm_role_assignment" "app-gw-contributor" {
   scope                = data.azurerm_application_gateway.appgateway.id
   role_definition_name = "Contributor"
   principal_id         = azurerm_kubernetes_cluster.akscluster.ingress_application_gateway[0].ingress_application_gateway_identity[0].object_id
 }
 resource "azurerm_role_assignment" "appgw-contributor" {
   scope                = data.azurerm_subnet.appgw-subnet.id
   role_definition_name = "Network Contributor"
   principal_id         = azurerm_kubernetes_cluster.akscluster.ingress_application_gateway[0].ingress_application_gateway_identity[0].object_id
 }

### AKS cluster creation
resource "azurerm_kubernetes_cluster" "akscluster" {
  name                      = var.NAME
  location                  = var.LOCATION
  resource_group_name       = var.RESOURCE_GROUP_NAME
  kubernetes_version        = var.kubernetes_version
  dns_prefix                = var.DNS_PREFIX
  private_cluster_enabled   = var.private_cluster_enabled
  automatic_channel_upgrade = var.automatic_channel_upgrade
  sku_tier                  = var.sku_tier
  azure_policy_enabled      = var.azure_policy_enabled
  private_dns_zone_id       = azurerm_private_dns_zone.aks.id

  default_node_pool {
    name                   = var.default_node_pool_name
    vm_size                = var.default_node_pool_vm_size
    vnet_subnet_id         = data.azurerm_subnet.aks-subnet.id
    zones                  = var.default_node_pool_availability_zones
    enable_auto_scaling    = var.default_node_pool_enable_auto_scaling
    enable_host_encryption = var.default_node_pool_enable_host_encryption
    enable_node_public_ip  = var.default_node_pool_enable_node_public_ip
    max_pods               = var.default_node_pool_max_pods
    max_count              = var.default_node_pool_max_count
    min_count              = var.default_node_pool_min_count
    node_count             = var.default_node_pool_node_count
    os_disk_type           = var.default_node_pool_os_disk_type
    node_labels = {
      "nodepool-type" = "system"
      "environment"   = "dev"
      "nodepoolos"    = "linux"
      "app"           = "system-apps"
    }
  }
  linux_profile {
    admin_username = var.admin_username
    ssh_key {
      key_data = var.SSH_PUBLIC_KEY
    }
  }

identity {
    type         = "UserAssigned"
    identity_ids = [azurerm_user_assigned_identity.aks-access.id]
  }
   ingress_application_gateway {
     gateway_id = data.azurerm_application_gateway.appgateway.id
   }
   /*
    azure_active_directory_role_based_access_control {
     managed            = true
     azure_rbac_enabled = true
   }
   */
  network_profile {
    dns_service_ip    = var.network_dns_service_ip
    network_plugin    = var.network_plugin
    service_cidr      = var.network_service_cidr
    load_balancer_sku = "standard"
  }
  
  /*
  oms_agent {
    msi_auth_for_monitoring_enabled = true
    log_analytics_workspace_id      = azurerm_log_analytics_workspace.insights.id
}
*/
    depends_on = [
    azurerm_role_assignment.network_contributor,
    azurerm_role_assignment.dns_contributor
  ]
}

