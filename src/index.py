import os
from flask import Flask, request, render_template, url_for, json
import boto3

app = Flask(__name__)

region = "ap-southeast-2"
dynamodbTableName = "tickets"
dynamodb = boto3.resource('dynamodb')
ticketsDB = dynamodb.Table(dynamodbTableName)

response = ticketsDB.scan()
ticketList = response['Items']

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

# @app.route("/getAllTickets", methods=['GET'])
# def getAllTickets():
#     filename = os.path.join(app.static_folder, 'Database', 'database.json')
#     with open(filename) as database:
#         data = json.load(database)
#     return data
    

@app.route("/sendTicket", methods=['POST'])
def sendTicket():
    print(request.form['ticketName'])
    # put ml algo here
    return "<p>Hello</p>"