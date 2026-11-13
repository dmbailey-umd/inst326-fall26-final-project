def input_checking(user_input):
    """ Checks if a user's input is valid; keeps reprompting user until
    they input something that is valid. (Written by Kaitlyn Manuel)
    
    Args:
        user_input (str): the player's decision
        
    Returns:
        str: A valid user input, either "yes" or "no" (might change)
        
    Side effects:
        Prints an error message & prompts the user for a new input if the
        inital input is invalid
    """
    