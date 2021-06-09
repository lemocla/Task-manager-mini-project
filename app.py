import os
# import flask 
from flask import (
    Flask, flash, render_template, redirect, 
    request, session, url_for)


from flask_pymongo import PyMongo
from bson.objectid import ObjectId
# import environment 
if os.path.exists("env.py"):
    import env


# create an instance of flask 
app = Flask(__name__)


app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")


mongo = PyMongo(app)


# test function to make sure app is properly configured
@app.route("/")
@app.route("/get_tasks")
def get_tasks():
    tasks = mongo.db.tasks.find()
    return render_template("tasks.html", tasks=tasks)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)