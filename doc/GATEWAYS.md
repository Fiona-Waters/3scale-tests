# Known Capabilities
* `PRODUCTION_GATEWAY`: Gateway contains production gateway and can be used for calls to production.
* `APICAST`: Gateway is of type Apicast (so far all the gateways are Apicast).
* `CUSTOM_ENVIRONMENT`: You can set or read environmental variables for gateway.
* `SAME_CLUSTER`: Gateway is always located on the same cluster as 3scale, so it has access to internal services.

# Gateway type configuration
## Standard Apicast
*Description*: Default apicasts that are deployed by 3scale

*Has production gateway*: Yes

*Has implemented reload*: Yes

*Capabilities*: "PRODUCTION_GATEWAY, APICAST, CUSTOM_ENVIRONMENT, SAME_CLUSTER" 
```
gateway:
  type: "apicast"
  configuration:
    staging_deployment: "apicast-staging"              # Name of the staging apicast deployment in the Openshift
    production_deployment: "apicast-production"        # Name of the production apicast deployment in the Openshift
```
## Self-managed Apicast
*Description*: Self-managed apicast that is deployed somewhere else and we only know their address

*Has production gateway*: Yes

*Has implemented reload*: Yes

*Capabilities*: "APICAST, PRODUCTION_GATEWAY" 
```
gateway:
  type: "apicast-selfmanaged"
  configuration:
    sandbox_endpoint: "http://%s-staging.localhost:8080"             # Wildcard address for staging address for service
    production_endpoint: "http://%s-production.localhost:8080"       # Wildcard address for production address for service
    deployment:                                                      # DeploymentConfigs
        staging: "selfmanaged-staging"
        production: "selfmanaged-production"
    project: "threescale"                                            # OpenShift project containing the apicasts
    server: "server"                                                 # OpenShift server containing the apicasts
```
## Container Apicast
*Description*: Self-managed apicast that is deployed somewhere else and we only know their address

*Has production gateway*: No

*Has implemented reload*: No

*Capabilities*: "APICAST" 
```
gateway:
  type: "apicast-containerized"
  configuration:
    sandbox_endpoint: "http://%s-staging.localhost:8080"             # Wildcard address for staging address for service
    production_endpoint: "http://%s-production.localhost:8080"       # Wildcard address for production address for service
```
## Apicast Operator
*Description*: Self-managed apicast deployed by operator

*Has production gateway*: Yes

*Has implemented reload*: Yes

*Capabilities*: "APICAST, PRODUCTION_GATEWAY" 
```
gateway:
  type: "apicast-selfmanaged"
  configuration:
    sandbox_endpoint: "http://%s-staging.localhost:8080"             # Wildcard address for staging address for service
    production_endpoint: "http://%s-production.localhost:8080"       # Wildcard address for production address for service
    deployments:
        staging: "selfmanaged-staging"
        production: "selfmanaged-production"
    project: "threescale"
    server: "server"
    services:                                                         # Services that apicasts are available on
        staging: "apicast-staging"
        production: "apicast-production"                                   
```

## Template Apicast
*Description*: Self-managed template-based apicast that is deployed somewhere else and we only know their address

*Has production gateway*: Yes

*Has implemented reload*: Yes

*Capabilities*: "PRODUCTION_GATEWAY, APICAST, CUSTOM_ENVIRONMENT, SAME_CLUSTER"
```
gateway:
  type: "apicast-template"
  configuration:
    template: "https://www.xxxxxx.com.br/apicast.yml"                                    # Either URL or loca path to the apicast template yaml
    image: "docker-registry.default.svc:5000/<project name>/amp-apicast:latest"          # Registry endpoint to apicast image
    deployments:
        staging: "template-apicast-staging"                                              # Staging deployment name
        production: "template-apicast-production"                                        # Production deployment name
    sandbox_endpoint: "http://%s-staging.localhost:8080"                                 # Wildcard address for staging address for service
    production_endpoint: "http://%s-production.localhost:8080"                           # Wildcard address for production address for service
    apicast_configuration_url_secret: "https://<admin access token>@<3scale admin URL>"  # Optional: Apicast config. URL
```
## TLS Apicast
*Description*: Self-managed apicast that is deployed with ssl certificates somewhere else and we only know their address

*Has production gateway*: Yes

*Has implemented reload*: No

*Capabilities*: "PRODUCTION_GATEWAY, APICAST, CUSTOM_ENVIRONMENT, SAME_CLUSTER"
```
gateway:
  type: "apicast-tls"
  configuration:
    template: "https://www.xxxxxx.com.br/apicast.yml"                                    # Either URL or loca path to the apicast template yaml
    image: "docker-registry.default.svc:5000/<project name>/amp-apicast:latest"          # Registry endpoint to apicast image
    deployments:
        staging: "tls-apicast-staging"                                                   # Staging deployment name
        production: "tls-apicast-production"                                             # Production deployment name
    sandbox_endpoint: "https://%s.localhost:8080"                                        # Wildcard address for staging address for service
    production_endpoint: "https://%s.localhost:8080"                                     # Wildcard address for production address for service
    apicast_configuration_url_secret: "https://<admin access token>@<3scale admin URL>"  # Optional: Apicast config. URL
    cfssl:
      host: 0.0.0.0     # CFSSL server api URL
      port: 8888        # CFSSL server api port
```