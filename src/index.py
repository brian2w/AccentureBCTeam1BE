import os
from flask import Flask, request, render_template, url_for, json
import boto3
from bert import similar_algorithm
# import CORS from flask_cors

app = Flask(__name__)
# CORS(app)

region = "ap-southeast-2"
dynamodbTableName = "tickets"
dynamodb = boto3.resource(service_name ='dynamodb')
ticketsDB = dynamodb.Table(dynamodbTableName)

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
    # print(request.json)
    # Extract JSON from the FE.
    reqTicket = request.json

    ticketDDBRes = ticketsDB.scan()
    ticketList = ticketDDBRes['Items']
    

    print(reqTicket['description'], "frlksfjlsdjfds flksd")
    
    rankingList = similar_algorithm(reqTicket['acceptance_criteria'], ticketList)
    # print("success")
    returnObjList = []

    for val in rankingList:
        currId = val["ID"]
        currSimilarity = val["Similarity"]
        currTicket = ticketsDB.get_item(Key={'id': currId})
        currTicket['Item']['similarity'] = currSimilarity
        returnObjList.append(currTicket['Item'])
    print("before", str(returnObjList))
    return str(returnObjList)