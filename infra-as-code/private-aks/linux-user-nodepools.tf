# Create Linux Azure AKS Node Pool
resource "azurerm_kubernetes_cluster_node_pool" "linux101" {
  kubernetes_cluster_id  = azurerm_kubernetes_cluster.akscluster.id
  name                   = var.user_linux_node_pool_name
  mode                   = var.user_node_pool_mode
  vm_size                = var.default_node_pool_vm_size
  vnet_subnet_id         = data.azurerm_subnet.aks-subnet.id
  zones                  = var.default_node_pool_availability_zones
  enable_auto_scaling    = var.default_node_pool_enable_auto_scaling
  enable_host_encryption = var.default_node_pool_enable_host_encryption
  enable_node_public_ip  = var.default_node_pool_enable_node_public_ip
  #max_pods               = var.default_node_pool_max_pods
  max_count    = "1"
  min_count    = "1"
  node_count   = var.default_node_pool_node_count
  os_disk_type = var.default_node_pool_os_disk_type
  node_labels = {
    "nodepool-type" = var.user_node_pool_mode
    "environment"   = var.environment
    "nodepoolos"    = "linux"
    "app"           = "user-apps"
  }

}