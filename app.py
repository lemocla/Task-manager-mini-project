import os
# import flask 
from flask import Flask
# import environment 
if os.path.exists("env.py"):
    import env


# create an instance of flask 
app = Flask(__name__)


# test function to make sure app is properly configured
@app.route("/")
def hello():
    return("hello world...again!")


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)