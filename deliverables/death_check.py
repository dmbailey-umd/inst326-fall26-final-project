def death_check(resources):
    """Checks to see if a player is dead by having 0 of a specific resource or
    having a huge disparity between resources. Game ends if player has a 
    resource that doesn't meet the lower threshold and another that exceeds 
    the upper threshold.
    Args:
        resources (list): A list containing the amount of resources 
        the player(king/queen) has
    Side Effects:
        None
    Returns:
        True: if the player meets the requirements to continue the game
        False: If the players resource value isn't enough to 
        continue the game
    """
    min_threshold = 5
    max_threshold = 25
    continue_game = True
    upper = True
    lower = True
    for total in resources:
        if total == 0:
            return False
        if total < min_threshold:
            lower = False #Doesn't meet lower threshold
        if  total>max_threshold:
                upper = False #Exceeds the max threshold
        if lower == False and upper == False:
                continue_game = False 
    if continue_game ==False:
        return False
    return True

#Uncomment Lines 35 and 36 to test function and values
#sample_resources = [26,10,3,14]
#print(death_check(sample_resources))

#Index Positioning
# 0 = Money
# 1 = People
# 2 = Army
# 3 = Church