## Once theres a match, we need to send back the correct ticket 
## loop through json file, keep a counter on, once the loop ends
## match the counter to the json id 
## return json object 
import json
  
# Opening JSON file
tickets = open('data1.json')
  
# returns JSON object as 
# a dictionary
data = json.load(tickets)
  
# Iterating through the json
# list
for i in data['emp_details']:
    print(i)
  
# Closing file
f.close()