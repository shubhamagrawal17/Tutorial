## we are going to create 3 virtual network one for AKS , second for ACR and other Resource and third for selfhosted agents#

resource "azurerm_virtual_network" "aks-vnet" {
  name                = var.AKS_VNET_NAME
  location            = var.LOCATION
  resource_group_name = var.RESOURCE_GROUP_NAME
  address_space       = [var.AKS_ADDRESS_SPACE]
}

resource "azurerm_subnet" "aks-subnet" {
  name                 = var.AKS_SUBNET_NAME
  resource_group_name  = var.RESOURCE_GROUP_NAME
  virtual_network_name = azurerm_virtual_network.aks-vnet.name
  address_prefixes     = [var.AKS_SUBNET_ADDRESS_PREFIX]

  service_endpoints = ["Microsoft.Sql"]
}

resource "azurerm_subnet" "appgw-subnet" {
  name                 = var.APPGW_SUBNET_NAME
  resource_group_name  = var.RESOURCE_GROUP_NAME
  virtual_network_name = azurerm_virtual_network.aks-vnet.name
  address_prefixes     = [var.APPGW_SUBNET_ADDRESS_PREFIX]
}
resource "azurerm_virtual_network" "acr-vnet" {
  name                = var.ACR_VNET_NAME
  location            = var.LOCATION
  resource_group_name = var.RESOURCE_GROUP_NAME
  address_space       = [var.ACR_ADDRESS_SPACE]

  subnet {
    name           = var.ACR_SUBNET_NAME
    address_prefix = var.ACR_SUBNET_ADDRESS_PREFIX
  }
  
}
resource "azurerm_virtual_network" "agent-vnet" {
  name                = var.AGENT_VNET_NAME
  location            = var.LOCATION
  resource_group_name = var.RESOURCE_GROUP_NAME
  address_space       = [var.AGENT_ADDRESS_SPACE]

  subnet {
    name           = var.AGENT_SUBNET_NAME
    address_prefix = var.AGENT_SUBNET_ADDRESS_PREFIX
  }
}

resource "azurerm_virtual_network_peering" "aks-acr" {
  name                      = "akstoacr"
  resource_group_name       = var.RESOURCE_GROUP_NAME
  virtual_network_name      = azurerm_virtual_network.aks-vnet.name
  remote_virtual_network_id = azurerm_virtual_network.acr-vnet.id
  allow_virtual_network_access = true
  allow_forwarded_traffic      = true
  allow_gateway_transit        = true
}
resource "azurerm_virtual_network_peering" "acr-aks" {
  name                      = "acrtoaks"
  resource_group_name       = var.RESOURCE_GROUP_NAME
  virtual_network_name      = azurerm_virtual_network.acr-vnet.name
  remote_virtual_network_id = azurerm_virtual_network.aks-vnet.id
  allow_virtual_network_access = true
  allow_forwarded_traffic      = true
  allow_gateway_transit        = true
}
resource "azurerm_virtual_network_peering" "acr-agent" {
  name                      = "acrtoagnet"
  resource_group_name       = var.RESOURCE_GROUP_NAME
  virtual_network_name      = azurerm_virtual_network.acr-vnet.name
  remote_virtual_network_id = azurerm_virtual_network.agent-vnet.id
  allow_virtual_network_access = true
  allow_forwarded_traffic      = true
  allow_gateway_transit        = true
}
resource "azurerm_virtual_network_peering" "agent-acr" {
  name                      = "agnettoacr"
  resource_group_name       = var.RESOURCE_GROUP_NAME
  virtual_network_name      = azurerm_virtual_network.agent-vnet.name
  remote_virtual_network_id = azurerm_virtual_network.acr-vnet.id
  allow_virtual_network_access = true
  allow_forwarded_traffic      = true
  allow_gateway_transit        = true
}
resource "azurerm_virtual_network_peering" "aks-agent" {
  name                      = "akstoagnet"
  resource_group_name       = var.RESOURCE_GROUP_NAME
  virtual_network_name      = azurerm_virtual_network.aks-vnet.name
  remote_virtual_network_id = azurerm_virtual_network.agent-vnet.id
  allow_virtual_network_access = true
  allow_forwarded_traffic      = true
  allow_gateway_transit        = true
}
resource "azurerm_virtual_network_peering" "agent-aks" {
  name                      = "agnettoaks"
  resource_group_name       = var.RESOURCE_GROUP_NAME
  virtual_network_name      = azurerm_virtual_network.agent-vnet.name
  remote_virtual_network_id = azurerm_virtual_network.aks-vnet.id
  allow_virtual_network_access = true
  allow_forwarded_traffic      = true
  allow_gateway_transit        = true
}