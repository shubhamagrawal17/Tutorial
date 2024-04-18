# Subscription ID is required for AGIC
data "azurerm_subscription" "current" {}

data "azurerm_subnet" "appgw-subnet" {
  name                 = "appgw-subnet"
  virtual_network_name = var.VIRTUAL_NETWORK_NAME
  resource_group_name  = var.RESOURCE_GROUP_NAME
}

data "azurerm_resource_group" "rg-devops" {
  name = "rg-devops"
}
#
# Application Gateway
locals {
  backend_address_pool_name      = "${var.VIRTUAL_NETWORK_NAME}-beap"
  frontend_port_name             = "${var.VIRTUAL_NETWORK_NAME}-feport"
  frontend_ip_configuration_name = "${var.VIRTUAL_NETWORK_NAME}-feip"
  http_setting_name              = "${var.VIRTUAL_NETWORK_NAME}-be-htst"
  http_listener_name             = "${var.VIRTUAL_NETWORK_NAME}-httplstn"
  request_routing_rule_name      = "${var.VIRTUAL_NETWORK_NAME}-rqrt"
}

# Public IP
resource "azurerm_public_ip" "public_ip" {
  name                = var.APPGW_PUBLIC_IP_NAME
  resource_group_name = var.RESOURCE_GROUP_NAME
  location            = var.LOCATION
  allocation_method   = "Static"
  sku                 = "Standard"
  #domain_name_label   = var.domain_name_label # Maps to <domain_name_label>.<region>.cloudapp.azure.com
}

# Application gateway
resource "azurerm_application_gateway" "appgateway" {
  name                = var.APP_GATEWAY_NAME
  resource_group_name = var.RESOURCE_GROUP_NAME
  location            = var.LOCATION

  sku {
    name     = "Standard_v2"
    tier     = "Standard_v2"
    capacity = 1
  }

  gateway_ip_configuration {
    name      = "appgw-ip-config"
    subnet_id = data.azurerm_subnet.appgw-subnet.id
  }

  frontend_port {
    name = local.frontend_port_name
    port = 80
  }
  frontend_port {
     name = "httpsPort"
     port = 443
   }

  frontend_ip_configuration {
    name                 = local.frontend_ip_configuration_name
    public_ip_address_id = azurerm_public_ip.public_ip.id
  }

  backend_address_pool {
    name = local.backend_address_pool_name
  }

  backend_http_settings {
    name                  = local.http_setting_name
    cookie_based_affinity = "Disabled"
    port                  = 80
    protocol              = "Http"
    request_timeout       = 1
  }

  http_listener {
    name                           = local.http_listener_name
    frontend_ip_configuration_name = local.frontend_ip_configuration_name
    frontend_port_name             = local.frontend_port_name
    protocol                       = "Http"
  }

  request_routing_rule {
    name                       = local.request_routing_rule_name
    rule_type                  = "Basic"
    http_listener_name         = local.http_listener_name
    backend_address_pool_name  = local.backend_address_pool_name
    backend_http_settings_name = local.http_setting_name
    priority                   = "100"
  }
  depends_on = [azurerm_public_ip.public_ip]

  lifecycle {
    ignore_changes = [
      tags,
      backend_address_pool,
      backend_http_settings,
      probe,
      identity,
      request_routing_rule,
      url_path_map,
      frontend_port,
      http_listener,
      redirect_configuration
    ]
  }
}
