variable "RESOURCE_GROUP_NAME" {
  type        = string
  description = "Resource group"
}

variable "APP_GATEWAY_NAME" {
  type        = string
  description = "Application name. Use only lowercase letters and numbers"

}

variable "LOCATION" {
  type        = string
  description = "Azure region where to create resources."
}

variable "VIRTUAL_NETWORK_NAME" {
  type        = string
  description = "Virtual network name. This service will create subnets in this network."
}

variable "APPGW_PUBLIC_IP_NAME" {
  type        = string
  description = "PUBLIC IP. This service will create subnets in this network."
}
