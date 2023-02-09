## Once theres a match, we need to send back the correct ticket 
## loop through json file, keep a counter on, once the loop ends
## match the counter to the json id of the closest ticket
## return json object 
import json
  
# Opening JSON file
tickets = open('data1.json')
  
# returns JSON object as 
# a dictionary
data = json.load(tickets)

  
# Iterating through the json
# list
counter = 0
match = False

matched_id = 4
matched = false
for obj in data:
    print(obj["acceptance_criteria"])

    counter+= 1
    
    
    
# # Closing file
print(counter)

tickets.close()
