 ### Log Analytics workspace
resource "azurerm_log_analytics_workspace" "logs" {
  name                = "logana-01"
  location            = var.LOCATION
  resource_group_name = var.RESOURCE_GROUP_NAME
  sku                 = "PerGB2018"
  retention_in_days   = 30
}