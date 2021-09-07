# dokka-hello-world
Dokka Hello World is a simple API service hosted at  [devopstest.blitsman.org](https://devopstest.blitsman.org/)

## A Simple Hello World Application
Based on [Python 3.9.7-alpine3.13 - Latest at the moment](https://hub.docker.com/_/python?tab=description&page=1&ordering=last_updated) & [Flask](https://flask.palletsprojects.com/en/2.0.x/) - Micro Web-Framwork.

### Gunicorn as the central master process manager
Manages the workers, in case of child process termination - automatically restart the faild worker.<br/>
- [Gunicorn Docs](https://gunicorn.org/#docs)
- [Gunicorn Design](https://docs.gunicorn.org/en/latest/design.html)

### Certbot (Let's Encrypt) Docker Container for TLS Certificate
[Certbot](https://certbot.eff.org/) is an automated tool to create & manage the certificates needed for our API.<br/>
[Let's Encrypt](https://letsencrypt.org/) - Nonprofit Certificate Authority providing the TLS certificates.

### Certbot Implementation with Docker Compose
The Implementation of this tool is based on - [Nginx and Let’s Encrypt with Docker](https://pentacent.medium.com/nginx-and-lets-encrypt-with-docker-in-less-than-5-minutes-b4b8a60d3a71)




