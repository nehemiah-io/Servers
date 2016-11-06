# Milestone 1: Tasks
# Features
# Tasks can be created, listed, and destroyed.
# Completed tasks are destroyed instead of stored.
#
#
# Data Models
# Tasks have 2 fields: id and text
#
#
# Routes and Actions
# Create unit tests for and then implement the following new routes:
# POST   /tasks
# create new task with text field from request body
# GET    /tasks
# list all tasks
# GET    /tasks/<id>
# show task with id
# DELETE /tasks/<id>
# destroy task with id
#
from flask import Flask, request, jsonify, json

app = Flask(__name__)
tasks = [""]

@app.route("/")
def home():
    return "This is the home page"

@app.route("/tasks",methods=['GET','POST'])
def gettasks():
    if request.method == 'POST':
        print (request.args.to_dict())
        return jsonify({"job"})

    elif request.method == 'GET':
        return json.dumps(tasks)

@app.route("/tasks/<ids>")
def task_name():
    return "okay"

@app.route("/tasks/<ids>", methods = ['DELETE'])
def task_delete():
    if request.method == 'DELETE':
        return tasks

if __name__ == '__main__':
    app.run()
