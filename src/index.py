import os
from flask import Flask, request, render_template, url_for, json

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/getAllTickets", methods=['GET'])
def getAllTickets():
    filename = os.path.join(app.static_folder, 'Database', 'database.json')
    with open(filename) as database:
        data = json.load(database)
    return data
    

@app.route("/sendTicket", methods=['POST'])
def sendTicket():
    print(request.form['ticketName'])
    return "<p>Hello</p>"