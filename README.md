# dokka-hello-world
Dokka Hello World is a simple API service hosted at  [devopstest.blitsman.org](https://devopstest.blitsman.org/)

## A Simple Hello World Application
Based on [Python 3.9.7-alpine3.13 - Latest at the moment](https://hub.docker.com/_/python?tab=description&page=1&ordering=last_updated) & [Flask](https://flask.palletsprojects.com/en/2.0.x/) - Micro Web-Framwork.

### Gunicorn As the Central Master Process Manager
Manages the workers, in case of child process termination - automatically restart the faild worker.<br/>
- [Gunicorn Docs](https://gunicorn.org/#docs)
- [Gunicorn Design](https://docs.gunicorn.org/en/latest/design.html)

### NGINX Web Server
Based on [NGINX - Latest](https://hub.docker.com/_/nginx) - to serve as an API Gateway.

### Certbot (Let's Encrypt) Docker Container for TLS Certificate
[Certbot](https://certbot.eff.org/) is an automated tool to create & manage the certificates needed for our API.<br/>
[Let's Encrypt](https://letsencrypt.org/) - Nonprofit Certificate Authority providing the TLS certificates.

### Certbot Implementation with Docker Compose
The Implementation of this tool is based on - [Nginx and Let’s Encrypt with Docker](https://pentacent.medium.com/nginx-and-lets-encrypt-with-docker-in-less-than-5-minutes-b4b8a60d3a71)<br/>
To get the initial certificate we had to remove the 443 block from the nginx.conf so the app won't fail on not having the certificate.<br/>
Once the certificate was issued and placed as needed - 443 block on nginx.conf was returned and the app was now reachable through HTTPS.

### Infrastructure (Microsoft Azure Cloud)
![Dokka Hello World Application](https://github.com/Arielbli/dokka-hello-world/blob/main/dokka-hello-world.png?raw=true)

### Tasks
- [] Create a monitoring metric that tracks API invocations (requests/minutes) using Azure Insights monitoring service.

## How To?
Make sure your machine has Docker Engine & Docker-Compose (Compatible with Version 3 template).<br/>
For initial Certificate issue:<br/>
remove the 443 block -> `docker-compose up` -> run `./init-letsencrypt.sh`, issue the certificates, make sure the volume mounts are correct -> `docker-compose up`
```
git clone
docker-compose up
```