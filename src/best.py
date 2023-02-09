
percentages = [76,45,99]
id = 1 # id of ticket
ticket_percent = {id: percentages}

#### function to get average for specific ticket
def get_average_of_scores(ticket_percent):
    for id in ticket_percent: # loop through dictionary
        list_numbers = ticket_percent[id]


    average = 0
    average = sum(list_numbers) / len(list_numbers)
    average = round(average,2)
    print(average)


get_average_of_scores(ticket_percent) # function call









