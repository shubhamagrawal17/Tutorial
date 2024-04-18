data "azurerm_application_gateway" "appgateway" {
  name                = "ApplicationGateway1"
  resource_group_name = var.RESOURCE_GROUP_NAME
}

data "azurerm_public_ip" "appgwpublicip" {
  name                = "appgwpublicip"
  resource_group_name = var.RESOURCE_GROUP_NAME
}

resource "random_id" "front_door_endpoint_name" {
  byte_length = 2
}

locals {
  front_door_profile_name      = "MyFrontDoor"
  front_door_endpoint_name     = "afd-${lower(random_id.front_door_endpoint_name.hex)}"
  front_door_origin_group_name = "MyOriginGroup"
  front_door_origin_name       = "MyAppServiceOrigin"
  front_door_route_name        = "MyRoute"
}

resource "azurerm_cdn_frontdoor_profile" "my_front_door" {
  name                = local.front_door_profile_name
  resource_group_name = var.RESOURCE_GROUP_NAME
  sku_name            = "Standard_AzureFrontDoor"
}

resource "azurerm_cdn_frontdoor_endpoint" "my_endpoint" {
  name                     = local.front_door_endpoint_name
  cdn_frontdoor_profile_id = azurerm_cdn_frontdoor_profile.my_front_door.id
}

resource "azurerm_cdn_frontdoor_origin_group" "my_origin_group" {
  name                     = local.front_door_origin_group_name
  cdn_frontdoor_profile_id = azurerm_cdn_frontdoor_profile.my_front_door.id
  session_affinity_enabled = false

  load_balancing {
    sample_size                 = 4
    successful_samples_required = 3
  }

  health_probe {
    path                = "/"
    request_type        = "HEAD"
    protocol            = "Https"
    interval_in_seconds = 100
  }
}

resource "azurerm_cdn_frontdoor_origin" "app_gateway_origin" {
  name                          = "my-app-gateway-origin"
  cdn_frontdoor_origin_group_id = azurerm_cdn_frontdoor_origin_group.my_origin_group.id

  enabled                        = true
  host_name                      = data.azurerm_public_ip.appgwpublicip.ip_address
  http_port                      = 80
  https_port                     = 443
  origin_host_header             = data.azurerm_public_ip.appgwpublicip.ip_address # Replace with the host header of your Application Gateway
  priority                       = 1                  # Set the priority according to your needs
  weight                         = 1000               # Adjust weight if needed
  certificate_name_check_enabled = false               # Enable/disable certificate name check as needed
}




resource "azurerm_cdn_frontdoor_route" "my_route" {
  name                          = local.front_door_route_name
  cdn_frontdoor_endpoint_id     = azurerm_cdn_frontdoor_endpoint.my_endpoint.id
  cdn_frontdoor_origin_group_id = azurerm_cdn_frontdoor_origin_group.my_origin_group.id
  cdn_frontdoor_origin_ids      = [azurerm_cdn_frontdoor_origin.app_gateway_origin.id]

  supported_protocols    = ["Http", "Https"]
  patterns_to_match      = ["/*"]
  forwarding_protocol    = "HttpOnly"
  link_to_default_domain = true
  https_redirect_enabled = false
}
