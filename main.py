from json import load, dumps
from os import environ

from flask import Flask
import requests

app = Flask(__name__)


@app.route("/")
def hello_world():
    jwks = requests.get(environ["JWKS_URL"])
    jwks = jwks.json()
    return dumps({"keys": [key for key in jwks["keys"] if key["alg"] == "RS256"]})


app.run(host=environ["HOST"])
