from flask import Flask, request

app = Flask(__name__)


@app.route('/headers')
def headers():
    h = request.headers
    if headers:
        print("HEADERS:")
        print(h)
        return ""
