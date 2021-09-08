from flask import Flask
from logging import StreamHandler
import logging

from applicationinsights.flask.ext import AppInsights
from opencensus.ext.azure.log_exporter import AzureLogHandler


## Logger Format
logging.basicConfig(
    format='%(asctime)s %(levelname)-8s %(message)s',
    level=logging.INFO,
    datefmt='%Y-%m-%d %H:%M:%S')

logger = logging.getLogger(__name__)
logger.addHandler(AzureLogHandler(connection_string='InstrumentationKey=f4427b7f-a37c-4e89-a629-1c270edea42c'))

app = Flask(__name__)

# keep stdout/stderr logging using StreamHandler - for testing purposes
#streamHandler = StreamHandler()
#app.logger.addHandler(streamHandler)

@app.route('/')
def index():
    logger.warning('Hello, World!')
    return 'Hello World!'


# Needed only for local testing - gunicorn (Python Process Manager) takes care for it in real-time
#app.run(host='localhost', port=8080)
