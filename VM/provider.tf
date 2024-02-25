provider "azurerm" {
  features {}
  skip_provider_registration = true
  client_id                  = "your client id"
  client_secret              = "your client secret"
  tenant_id                  = "your tenant id"
  subscription_id            = "your subscription_id"
}
