def draw_display(player):
    """
    Prints a display to the terminal representing the resources of the player, being the player's
    money, support of the people, support of the church, and support of the army. Currently, this
    function prints a new display following each call, however, I'm researching ways to clear the
    terminal if there is already an existing display, therefore preventing the game from printing 
    dozens of displays before the player loses. Updating the display was a little tricky, so here
    is how it works... Display is converted into a list of strings, with each element of the list
    being one of the display's rows. Display is converted into a list of lists, with the internal
    lists holding a list of characters. Within the list of lists, locate the right row and column
    by storing the starting and ending indexes for printing characters, treaing the list of lists
    as if it were a two-dimensional array. As long as the game is running, this loop locates the
    positions of the resources on the display, and will insert three "█" characters representing
    a point of a certain resource.
    
    Args:
        player (Player): Instance containing the player's active amount of resources. 

    Returns:
        None

    Raises:
        None

    Side Effects:
        Prints a display to the terminal following each call. Before a display prints, it is effectively
        converted into a two-dimentional array with the inner index representing the rows and the outer
        index representing the columns. The list of lists containing the display is modified to visually
        communicate the increase and decrease of the player's resources, and then the list of lists is 
        joined back together. 
    """

    upper_bar_boundary = 10
    lower_bar_boundary = 18

    starting_location = [4, 11, 18, 25]

    resource_display = """\
████████████████████████████████
█                              █
█    █      █      █      █    █
█   ███    ███    ███     █    █
█   ███    █       █      █    █
█   █ █    ███     █     ███   █
█   █ █     █      █      █    █
█                              █
█  █████  █████  █████  █████  █
█  █   █  █   █  █   █  █   █  █
█  █   █  █   █  █   █  █   █  █
█  █   █  █   █  █   █  █   █  █
█  █   █  █   █  █   █  █   █  █
█  █   █  █   █  █   █  █   █  █
█  █   █  █   █  █   █  █   █  █
█  █   █  █   █  █   █  █   █  █
█  █   █  █   █  █   █  █   █  █
█  █   █  █   █  █   █  █   █  █
█  █   █  █   █  █   █  █   █  █
█  █████  █████  █████  █████  █
█                              █
████████████████████████████████
"""
    list_of_strings = resource_display.splitlines()

    list_of_characters = list()

    for line in list_of_strings:
        list_of_characters.append(list(line))

    player_values = [player.money, player.people, player.army, player.church]

    for bar in range(4):
        current_value = player_values[bar]

        if current_value < 0:
            current_value = 0
        if current_value > 10:
            current_value = 10

        start_location = starting_location[bar]

        for i in range(current_value):
            row = lower_bar_boundary - i

            for j in range(start_location, start_location + 3):
                list_of_characters[row][j] = "█"

    for line in list_of_characters:
        print("".join(line))

# Un-comment this code to see the function work using an instance of the "player" object...
      
# class Player:
#     def __init__(self):
#         self.money = 5
#         self.people = 5
#         self.army = 5
#         self.church = 5
#
# def main():
#     player = Player()
#
#     draw_display(player)
#
#     time.sleep(3)
#
#     player.money = 6
#     player.people = 7
#     player.army = 8
#     player.church = 9
#
#     draw_display(player)
#
# if __name__ == "__main__":
#     main()
