from flask import Flask
from opencensus.ext.azure.common import INSTRUMENTATION_KEY
from opencensus.ext.azure.trace_exporter import AzureExporter
from opencensus.ext.azure.log_exporter import AzureLogHandler
from opencensus.ext.flask.flask_middleware import FlaskMiddleware
from opencensus.trace.samplers import ProbabilitySampler
import logging

INSTRUMENTATION_KEY='f4427b7f-a37c-4e89-a629-1c270edea42c'


## Logger Format
logging.basicConfig(
    format='%(asctime)s %(levelname)-8s %(message)s',
    level=logging.INFO,
    datefmt='%Y-%m-%d %H:%M:%S')

logger = logging.getLogger(__name__)
logger.addHandler(AzureLogHandler(connection_string=f'InstrumentationKey={INSTRUMENTATION_KEY}'))

app = Flask(__name__)
middleware = FlaskMiddleware(
    app,
    exporter=AzureExporter(connection_string=f"InstrumentationKey={INSTRUMENTATION_KEY}"),
    sampler=ProbabilitySampler(rate=1.0),
)

# keep stdout/stderr logging using StreamHandler - for testing purposes
#streamHandler = StreamHandler()
#app.logger.addHandler(streamHandler)

@app.route('/')
def index():
    logger.warning('Hello, World!')
    return 'Hello World!'


# Needed only for local testing - gunicorn (Python Process Manager) takes care for it in real-time
#app.run(host='localhost', port=8080)
