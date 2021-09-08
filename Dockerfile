FROM python:3.9.7-alpine3.13
WORKDIR /app
COPY . .
RUN python -m pip install --upgrade pip
RUN apk add gcc && apk add musl-dev && apk add linux-headers
RUN pip install -r requirements.txt \
    && pip install virtualenv
RUN python3 -m virtualenv --python=python3 virtualenv
RUN pip install opencensus-ext-azure
EXPOSE 8080

# For local testing - un-needed once working with gunicorn
##CMD [ "python", "helloWorld.py" ]
