# dokka-hello-world
Dokka Hello World is a simple API service hosted at  [devopstest.blitsman.org](https://devopstest.blitsman.org/)
## A Simple Hello World Application
Based on [Python 3.9.7-alpine3.13 - Latest at the moment](https://hub.docker.com/_/python?tab=description&page=1&ordering=last_updated) & [Flask](https://flask.palletsprojects.com/en/2.0.x/)
### Gunicorn as the central master process manager
Manages the workers, in case of some failure - restart the faild worker. 
[Gunicorn Docs](https://gunicorn.org/#docs) | [Gunicorn Design](https://docs.gunicorn.org/en/latest/design.html)




