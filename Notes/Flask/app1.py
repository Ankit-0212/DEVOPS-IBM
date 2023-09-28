from flask import Flask
from datetime import datetime
app = Flask(__name__)

# @app.get("/welcome")
@app.route(rule="/welcome",methods=["POST"])
def welcome():
    return "This page is @"+str(datetime.now())


