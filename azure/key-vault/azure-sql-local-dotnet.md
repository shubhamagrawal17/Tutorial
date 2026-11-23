In this Files we are going to follow the steps which is required to connect dotnet core application connection string with Azure Key Vault.
Step-1 
1.	First create the app registration in Azure portal and generate the secret.
   ![image](https://github.com/shubhamagrawal17/Tutorial/assets/24695227/9269bb60-ae0e-44db-937a-308136795eb0)

   ![image](https://github.com/shubhamagrawal17/Tutorial/assets/24695227/b5dafad2-bf5f-424f-a13c-2ce0ae8dd1a8)
   2. Then create the secret.
   ![image](https://github.com/shubhamagrawal17/Tutorial/assets/24695227/60a097d4-4286-49d4-80fc-5c7be60273b9)

   ![image](https://github.com/shubhamagrawal17/Tutorial/assets/24695227/780bb1dd-3e74-44a2-866e-92bf5a05ff74)




3.	Create the Azure Key Vault .
4.	Create the secret in Azure key vault and use Access configuration as Azure role-based access control .
5.	If you see below error and If you are creating the Key vault with RBAC role from scratch then Please assign Key vault Administrator to your name for creating/ managing the secrets, certificates and keys.
   ![image](https://github.com/shubhamagrawal17/Tutorial/assets/24695227/6f87fd76-dbc8-4b05-b049-13beb9cf6128)

   ![image](https://github.com/shubhamagrawal17/Tutorial/assets/24695227/edcf2af7-bbb8-4f03-8940-3e0341daf39f)

6. Once you add the IAM Role then you can create the secret.
   ![image](https://github.com/shubhamagrawal17/Tutorial/assets/24695227/81722ca5-6cfc-4828-b84c-61705873a711)

   ![image](https://github.com/shubhamagrawal17/Tutorial/assets/24695227/aad3770f-7dfc-48b1-8d78-c4db8c101bd4)




8.	Now add IAM Role and select role Key Vault Contributor and select member as a service principle which we have created in step1.
   
Step-2
1.	If you are testing the application from visual studio and retrieving the app setting from Azure key vault then first you have environment variable for the Authentication .
 
![image](https://github.com/shubhamagrawal17/Tutorial/assets/24695227/779b1588-05bb-4b78-97d7-792b4ef2bac1)

2.	Next you have to install nuget package in your application.
Azure.Identity;
Azure.Security.KeyVault.Secrets;
3.	Add below code in your startup.cs file.
![image](https://github.com/shubhamagrawal17/Tutorial/assets/24695227/df0de739-2eec-4d42-a76e-a6dfa28692f3)

 

// Create a SecretClient using the managed identity for authentication
            var keyVaultUri = new Uri("https://testkeyvault4345.vault.azure.net/");
            var secretClient = new SecretClient(keyVaultUri, new DefaultAzureCredential());
  // Retrieve a secret by name
   KeyVaultSecret secret = secretClient.GetSecret("appsetting");
  // Access the secret value
   string DefaultConnectionString = secret.Value;
  // Now, you can use 'secretValue' in your application
services.AddDbContext<AppDbContext>(options => options.UseSqlServer(DefaultConnectionString));

Here appsetting – is the secret name which you have created in key vault.
4.	Next your appsetting.json file will be like this.
 ![image](https://github.com/shubhamagrawal17/Tutorial/assets/24695227/eaa67a3e-67f2-4acd-80b2-f414d0b1e4ff)

Here appsetting – is the secret name which you have created in key vault.


