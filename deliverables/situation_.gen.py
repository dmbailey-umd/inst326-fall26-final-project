import json
import random

#import random
def situation_gen(scen_path,char_path):
    """Generates and displays a random scenario based on the JSON file uploaded. The key that determines
    which resources will be affected for the situation will be stored.
    Args:
    - scen_path: JSON file that stores the different scenarios that the player can encounter
    - char_path: JSON file the stores the names of the different characters the player can encounter[titles can go in here]
    - title_path: JSON file that stores the title of the character that the player encounters[I really don't think we need this]
    Side effects:
    - Opens and reads 3 JSON files to generate the scenario
    - Prints out the situation
    Raises:
    - FileNotFoundError if any of the JSON files are incorrectly named or not in the right place.
    
    Returns: Values of the decisions made by the player
    """
    try:
        with open(scen_path,"r",encoding="utf-8") as file:
            scenario = json.load(file)
        with open(char_path,"r",encoding="utf-8") as file:
            characters = json.load(file)
        
    except FileNotFoundError:
        raise FileNotFoundError("File not found")
    select_scenarios = []
    #Weights will be added in the future regarding these choices too to add "rare" events
    current_scenario = random.choice(select_scenarios)
    for category,events in scenario.items():
        for event_name,event_data in events.items():
            #This will be the main communication source
            print(event_data["dialogue"])
    
    #if(current_scenario["effects"]) 
    #Functionality to display or show the dsplay data here will be impleented in the future
    #I'll add the option to have the characters be paired with their dialogue later
    
    

def main():
    situation_gen("../constants/scenario.json","../constants/characters.json")
if __name__ == "__main__":
    main()