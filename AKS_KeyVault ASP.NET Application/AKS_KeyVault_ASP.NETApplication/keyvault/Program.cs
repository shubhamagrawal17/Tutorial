using System;
using Azure.Identity;
using Azure.Security.KeyVault.Secrets;
using Microsoft.AspNetCore.Builder;
using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Logging;

var builder = WebApplication.CreateBuilder(args);
builder.Services.AddRazorPages();
var app = builder.Build();

app.MapGet("/", async () =>
{
    // Fetch the Key Vault name from environment variables
    string keyVaultName = Environment.GetEnvironmentVariable("KEYVAULTNAME");

    // Check if the Key Vault name is null or empty
    if (string.IsNullOrEmpty(keyVaultName))
    {
        return "Key Vault name not found.";
    }

    // Key Vault URL
    string keyVaultUrl = $"https://{keyVaultName}.vault.azure.net/";

    // Log the Key Vault URL
    Console.WriteLine($"Key Vault URL: {keyVaultUrl}");

    // Use DefaultAzureCredential, which picks up the User-Assigned Managed Identity details from environment variables
    var client = new SecretClient(new Uri(keyVaultUrl), new DefaultAzureCredential());

    // Fetch the secret name from environment variables
    string secretName = Environment.GetEnvironmentVariable("SECRET");

    if (string.IsNullOrEmpty(secretName))
    {
        return "Secret name not found in environment variables.";
    }

    try
    {
        // Fetch the secret value from Key Vault
        KeyVaultSecret secret = await client.GetSecretAsync(secretName);
        return $"Secret Value: {secret.Value}";
    }
    catch (Exception ex)
    {
        // Handle errors (e.g., secret not found, access issues)
        return $"Error fetching secret: {ex.Message}";
    }
});

app.Run();
