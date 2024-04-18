provider "azurerm" {
  features {}
  skip_provider_registration = true
}
terraform {
  backend "azurerm" {
    
  }
}