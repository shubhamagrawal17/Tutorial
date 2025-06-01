terraform {
  required_providers {
    azuredevops = {
      source  = "microsoft/azuredevops"
      version = ">=0.1.0"
    }
  }
}

terraform {
  backend "azurerm" {
  }
}
### To Create the Azure Webapp Plan ################
resource "azurerm_service_plan" "webplan" {
  name                = var.WEBAPP_PLAN_NAME
  location            = var.LOCATION
  resource_group_name = var.RG_NAME
  os_type             = var.OS_TYPE
  sku_name            = var.SKU_NAME
}
### To Create the Azure Webapp Service ################
resource "azurerm_app_service" "webapp" {
  name                = var.WEBAPPNAME
  location            = azurerm_service_plan.webplan.location
  resource_group_name = azurerm_service_plan.webplan.resource_group_name
  app_service_plan_id = azurerm_service_plan.webplan.id

  site_config {
    always_on        = true
    app_command_line = "python main.py"
    linux_fx_version = "DOCKER|python-flask-app:latest"
  }
  app_settings = {
    "SCM_DO_BUILD_DURING_DEPLOYMENT"      = "true"
    "WEBSITES_ENABLE_APP_SERVICE_STORAGE" = "false"
    "DOCKER_REGISTRY_SERVER_URL"          = var.DOCKER_REGISTRY_SERVER_URL
    "DOCKER_REGISTRY_SERVER_USERNAME"     = var.DOCKER_REGISTRY_SERVER_USERNAME
    "DOCKER_REGISTRY_SERVER_PASSWORD"     = var.DOCKER_REGISTRY_SERVER_PASSWORD
  }
}

output "webapp_name" {
  value = azurerm_app_service.webapp.name
}
### To Create the Azure Auto Scale based on the CPU Percentage ################
resource "azurerm_monitor_autoscale_setting" "autscale" {
  name                = var.APP_AUTOSCALE
  resource_group_name = azurerm_service_plan.webplan.resource_group_name
  location            = azurerm_service_plan.webplan.location
  target_resource_id  = azurerm_service_plan.webplan.id

  profile {
    name = "defaultProfile"
    capacity {
      default = 1
      minimum = 1
      maximum = 2
    }
    rule {
      metric_trigger {
        metric_name        = "CpuPercentage"
        metric_resource_id = azurerm_service_plan.webplan.id
        time_grain         = "PT1M"
        statistic          = "Average"
        time_window        = "PT5M"
        time_aggregation   = "Average"
        operator           = "GreaterThan"
        threshold          = 5
      }

      scale_action {
        direction = "Increase"
        type      = "ChangeCount"
        value     = "1"
        cooldown  = "PT1M"
      }
    }

    rule {
      metric_trigger {
        metric_name        = "CpuPercentage"
        metric_resource_id = azurerm_service_plan.webplan.id
        time_grain         = "PT1M"
        statistic          = "Average"
        time_window        = "PT5M"
        time_aggregation   = "Average"
        operator           = "LessThan"
        threshold          = 80
      }
      scale_action {
        direction = "Decrease"
        type      = "ChangeCount"
        value     = "1"
        cooldown  = "PT1M"
      }
    }
  }
  ### To Send the Alert ################
  notification {
    email {
      send_to_subscription_administrator    = false
      send_to_subscription_co_administrator = false
      custom_emails                         = [var.CUSTOM_EMAILS]
    }
  }
}