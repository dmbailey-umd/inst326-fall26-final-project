def input_checking(user_input):
    """ Checks if a user's input is valid; keeps reprompting user until
    they input something that is from a list of valid inputs.
    
    Args:
        user_input (str): the player's initial decision
        
    Returns:
        str: A valid user input, from a list of valid inputs
        
    Side effects:
        Prints an error message & prompts the user for a new input if the
        inital input is invalid.
    """
    valid_input = ["yes", "no", "y", "n", "Yes", "No"]
    while True:
        if user_input in valid_input:
            return user_input
        else:
            print("Invalid input. Please try again.")
            user_input = input("What is your decision?: ")