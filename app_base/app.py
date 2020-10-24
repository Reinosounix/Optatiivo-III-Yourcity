import requests
from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    response = requests.get('http://app_users:5000/users')
    response = requests.get('http://app_municipality:5000/municipalities')

    return response.text
