# See https://aka.ms/customizecontainer to learn how to customize your debug container 
# and how Visual Studio uses this Dockerfile to build your images for faster debugging.

# Stage 1: Base image for runtime
FROM mcr.microsoft.com/dotnet/aspnet:6.0 AS base
WORKDIR /app
EXPOSE 80
EXPOSE 443

# Stage 2: Build the application
FROM mcr.microsoft.com/dotnet/sdk:6.0 AS build
WORKDIR /src

# Copy the project file and restore dependencies
COPY ["keyvault.csproj", "."]
RUN dotnet restore "./keyvault.csproj"

# Copy the remaining files and build the application
COPY . .
RUN dotnet build "keyvault.csproj" -c Release -o /app/build

# Stage 3: Publish the application
FROM build AS publish
RUN dotnet publish "keyvault.csproj" -c Release -o /app/publish /p:UseAppHost=false

# Stage 4: Final image with runtime and published application
FROM base AS final
WORKDIR /app

# Copy the published files from the build stage
COPY --from=publish /app/publish .

# Ensure the application listens on port 80
ENV ASPNETCORE_URLS=http://+:80

# Set the entry point for the application
ENTRYPOINT ["dotnet", "keyvault.dll"]
