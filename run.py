import json

from flask import Flask
import requests

app = Flask(__name__)


def api_parser(url):
    response = requests.get(url)
    if response.status_code == 200 and response.headers['Content-Type'] == 'application/json; charset=utf-8':
        return response, response.json()
    return response, ''


if __name__ == '__main__':
    app.run(debug=True)
