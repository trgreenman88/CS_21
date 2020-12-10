# Trent Greenman
#CS 21, Fall 2018
#Program: Tennis

# Import random 
from random import random
# This function plays out each game between A and B
def play_game(probA):
    # Initialize the number of games A wins to be 0
    Awins = 0
    # Initialize the number of points A and B has to be 0
    A = 0
    B = 0
    # Create a list that we can use to get the points for the first
    # 4 points for each player
    points = ["0","15","30","40"]
    # This is the loop used when the game is not in deuce mode
    while A <= 3 and B <= 3 and (A != 3 or B != 3):
        # Use the indexes of the list, points, to show the score
        # between Players A and B based on the value of variables,
        # A and B
        print("Current Score:", points[B], "-", points[A])
        # If the random value is less than the given probA, add 1 to
        # the score of A
        if random() < probA:
            A += 1
        # Otherwise, add 1 to the score of B
        else:
            B += 1
    # This is the loop used when the game has reached deuce mode
    while A > 3 or B > 3 or (A == 3 and B == 3):
        # If the scores are equal, print deuce
        if A == B:
            print("Current Score: deuce")
        # If A is up by 1, print advantage Player A
        elif A - B == 1:
            print("Current Score: advantage Player A")
        # If B is up by 1, print advantage Player B
        elif B - A == 1:
            print("Current Score: advantagr Player B")
        # If B is up by 2 or more, print that B won the game and
        # do nothing to Awins. Then return Awins
        elif B - A >= 2:
            print("Winner: Player B")
            print("")
            return Awins
        # If A is up by 2 or more, print that A won the game and
        # add 1 to Awins. Then return Awins
        elif A - B >= 2:
            print("Winner: Player A")
            print("")
            Awins += 1
            return Awins
        # If the random value is less than the given probA, add 1 to
        # the score of A
        if random() < probA:
            A += 1
        # Otherwise, add 1 to the score of B
        else:
            B += 1
# This function takes 2 parameters. The first is the total number of
# games of tennis that will be simulated. The second is the probability
# that Player A will win each point.
def play_games(num_games, probA):
    # A is the number of games that A wins
    A = 0
    # Play a total of num_games games and call the play_game function
    # in order to play each game. If A wins, add 1 to A each game, 
    # and do nothing if B wins.
    for i in range(0, num_games):
        A += play_game(probA)
    # Return the number of games that each player wins as an integer. 
    # A is the number of games Player A won and num_games - A is the
    # number of games Player B won
    return A, num_games - A
# Print statements that introduce the program
def print_intro():
    print("This program simulates a tennis game between two players,")
    print("Player A and Player B. It will tell you the scores and how")
    print("many games each player wins. Have fun!")
    print("")
# This function gets the inputs for the number of games that will be
# played and the probability that Player A will win each point
def get_inputs():
    # Initialize num_games to be -1 so we automatically enter the loop
    num_games = -1
    # This loop tests whether num_games is a positive integer and keeps
    # goint until a positive integer is given for num_games
    while type(num_games) != int or num_games <= 0:
        # exception handling
        try:
            # Take a user input for num_games
            num_games = int(input("Enter the number of games you"
                                  " would like to play: "))
            # If num_games is negative, execute the print statement and 
            # keep the loop going
            if num_games < 0:
                print("The number of games must be positive.")
            # If num_games is 0, execute the print statement and keep the
            # loop going
            elif num_games == 0:
                print("The number of games can't be 0.")
        # If we get a ValueError, meaning that we did not enter an integer
        # for num_games, execute the print statement and keep the loop
        # going
        except ValueError:
            print("The number of games must be an integer.")
    # Initialize probA to be 2 so we will automatically enter the loop
    probA = 2
    # This loop tests whether probA is a float between 0 and 1 and keeps
    # going until a float between 0 and 1 is given for probA
    while type(probA) != float or probA < 0 or probA > 1:
        # exception handling
        try:
            # Take a user input for probA
            probA = float(input("Enter the probability that A will"
                                " win each point: "))
            # If probA is bigger than 1, execute the print statement and
            # keep the loop going
            if probA > 1:
                print("The probability must be between 0 and 1.")
            # If probA is negative, execute the print statement and keep
            # the loop going
            if probA < 0:
                print("The probability must be between 0 and 1.")
        # If we get a ValueError, meaning that we did not enter a float for
        # probA, execute the print statement and keep the loop going
        except ValueError:
            print("The number of games must be a real number.")
    # Return the two good inputs, num_games and probA
    return num_games, probA
# This function takes 2 parameters, Awins and B wins and it prints out the
# number of games each player won, and the percentage of games that Player
# A won
def print_summary(Awins, Bwins):
    print("Here are the results: ")
    print("Player A won", Awins, "games.")
    print("Player B won", Bwins, "games.")
    # Use this equation to calculate the percentage of games that Player A
    # won
    print("Player A won", 100 * (Awins / (Awins + Bwins)), "% of"
          " the games")
# This function calls print_intro, get_inputs, play_games, and
# print_summary
def main():
    print_intro()
    # Get these two variables from the get_inputs function and enter
    # them into the play_games function
    num_games, probA = get_inputs()
    # Get these two variables from the play_games function and enter
    # them into the print_summary function
    Awins, Bwins = play_games(num_games, probA)
    print_summary(Awins, Bwins)
# Run the main function
main()

    
