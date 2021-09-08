from flask import Flask
import logging

from opencensus.ext.azure.log_exporter import AzureEventHandler

logger = logging.getLogger(__name__)
logger.addHandler(AzureEventHandler(connection_string='InstrumentationKey=f4427b7f-a37c-4e89-a629-1c270edea42c'))
logger.setLevel(logging.INFO)


app = Flask(__name__)

@app.route('/')
def index():
    logger.info('Hello World!')
    return 'Hello World!'

# Needed only for local testing - gunicorn (Python Process Manager) takes care for it in real-time
#app.run(host='localhost', port=8080)