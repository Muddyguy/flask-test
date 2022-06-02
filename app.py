from flash import Flask
app = FLask(__name__)


@app.route('/')
def hello_world():
    return 'This is my first API call!'
