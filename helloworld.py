from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello World!'

# Needed only for local testing - gunicorn (Python Process Manager) takes care for it in real-time
#app.run(host='localhost', port=8080)