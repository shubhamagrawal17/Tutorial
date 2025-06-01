#See https://aka.ms/customizecontainer to learn how to customize your debug container and how Visual Studio uses this Dockerfile to build your images for faster debugging.

FROM mcr.microsoft.com/dotnet/aspnet:7.0 AS base
WORKDIR /app
EXPOSE 80
EXPOSE 443

FROM mcr.microsoft.com/dotnet/sdk:7.0 AS build
WORKDIR /src
COPY ["eTickets/eTickets.csproj", "eTickets/"]
RUN dotnet restore "eTickets/eTickets.csproj"
COPY . .
WORKDIR "/src/eTickets"
RUN dotnet build "eTickets.csproj" -c Release -o /app/build

FROM build AS publish
RUN dotnet publish "eTickets.csproj" -c Release -o /app/publish /p:UseAppHost=false

FROM base AS final
WORKDIR /app
COPY --from=publish /app/publish .
ENTRYPOINT ["dotnet", "eTickets.dll"]