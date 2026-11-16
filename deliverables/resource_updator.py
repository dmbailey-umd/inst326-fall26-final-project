import json

def resource_updator(filename, issue_type, issue, decisions):
    #Read in the json file
    with open(filename, "r", encoding="UTF-8") as f:
            situations = json.load(f)
    #Establish the starting resources, will eventaully be done outside this
    #function
    resource_values = {
        "people": 10,
        "money": 10,
        "army": 10,
        "church": 10
    }
    #Get the dictionary that contains the values to update each resource by
    resource_updates = situations[issue_type][issue][decisions]
    #Loops over each resource and value pair in the retrieved dictionary
    for resource, value in resource_updates.items():
        resource_values[resource] += value
        if resource_values[resource] > 10:
            resource_values[resource] = 10
        if resource_values[resource] <= 0:
            #Ends the game if any of the resources get below 0
            return False
    return resource_values

print(resource_updator("tester.json", "people", 0, "Yes"))
            