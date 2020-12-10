# Trent Greenman
# CS 21, Fall 2018
# Program: Tennis

from random import random
def play_game(probA, verbose = False):
    # Initialize the number of points A and B has to be 0
    A = 0
    B = 0
    # Create a list that we can use to get the points for the first
    # 4 points for each player
    points = ["0","15","30","40"]
    # The first two loops display the scores and are used when
    # verbose is set to True
    # This is the loop used when the game is not in deuce mode
    while A <= 3 and B <= 3 and (A != 3 or B != 3) and verbose:
        # Use the indexes of the list, points, to show the score
        # between Players A and B based on the value of variables,
        # A and B
        print("Current Score:", points[A], "-", points[B])
        # If the random value is less than the given probA, add 1 to
        # the score of A
        if random() < probA:
            A += 1
        # Otherwise, add 1 to the score of B
        else:
            B += 1
    # This is the loop used when the game has reached deuce mode
    while (A > 3 or B > 3 or (A == 3 and B == 3)) and verbose:
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
        # return "B"
        elif B - A >= 2:
            print("Winner: Player B")
            print("")
            return "B"
        # If A is up by 2 or more, print that A won the game and
        # return "A"
        elif A - B >= 2:
            print("Winner: Player A")
            print("")
            return "A"
        # If the random value is less than the given probA, add 1 to
        # the score of A
        if random() < probA:
            A += 1
        # Otherwise, add 1 to the score of B
        else:
            B += 1
    # Play game that does not display scores (verbose is False)
    # Everything works the same as the first two loops, except that
    # nothing is printed.
    while A <= 3 and B <= 3 and (A != 3 or B != 3) and not(verbose):
        if random() < probA:
            A += 1
        else:
            B += 1
    while (A > 3 or B > 3 or (A == 3 and B == 3)) and not(verbose):
        if A - B >= 2:
            return "A"
        elif B - A >= 2:
            return "B"
        if random() < probA:
            A += 1
        else:
            B += 1

# verbose has a default value of False
def play_tiebreak(probA, verbose = False):
    # initialize the points for players A and B to be 0
    A = 0
    B = 0
    # if verbose it True, then print stuff
    if verbose == True:
        print("TIEBREAK GAME")
    # This loop is used when verbose is False and does not print the
    # game as it happens
    while not(verbose):
        # If Player A is up by at least 2 points and has at
        # least 7 points, then return 7, 6 meaning that Player A won
        # a total of 7 games and Player B won a total of 6 games
        if A - B >= 2 and A >= 7:
            return 7, 6
        # If Player B is up by at least 2 points and has at
        # least 7 points, then return 6, 7 meaning that Player A won
        # a total of 6 games and Player B won a total of 7 games
        elif B - A >= 2 and B >= 7:
            return 6, 7
        # Keep the game going until someone wins
        if random() < probA:
            A += 1
        else:
            B += 1
    # This is used when verbose is True and shows the score of the
    # game as it is being played
    while verbose:
        print("Current Score:", A, "-", B)
        if A - B >= 2 and A >= 7:
            return 7, 6
        elif B - A >= 2 and B >= 7:
            return 6, 7
        if random() < probA:
            A += 1
        else:
            B += 1
        
# play_set takes 3 parameters, probA, and tiebreak and verbose which
# are optional parameters
def play_set(probA, tiebreak = True, verbose = False):
    # initialize the number of games A has won, and the number of games
    # B has won to be zero. Also initialize the winner of each game to
    # be an empty string
    Awins = 0
    Bwins = 0
    winner = ""
    # run this loop when verbose is false so nothing is printed
    while not(verbose):
        # winner is either "A" or "B" depending on what happens in the
        # play_game function
        winner = play_game(probA, verbose)
        # if player A wins a game, then add 1 to Awins
        if winner == "A":
            Awins += 1
        # if player B wins a game, then add 1 to Bwins
        elif winner == "B":
            Bwins += 1
        # if A has won at least 6 games and is up by at least 2 points,
        # then return the total number of games A and B each won
        if Awins >= 6 and Awins - Bwins >= 2:
            return Awins, Bwins
        # if B has won at least 6 games and is up by at least 2 points,
        # then return the total number of games A and B each won
        elif Bwins >= 6 and Bwins - Awins >= 2:
            return Awins, Bwins
        # if they are tied 6-6 in games and tiebreak is True, then return
        # the tiebreak function
        if Awins == 6 and Bwins == 6 and tiebreak:
            return play_tiebreak(probA, verbose)
    # run this loop when verbose is True so that it prints the number of
    # games each player wins. It works the same way as the first loop,
    # except for the printing.
    while verbose:
        print("Set Score:", Awins, "-", Bwins)
        winner = play_game(probA, verbose)
        if winner == "A":
            Awins += 1
        elif winner == "B":
            Bwins += 1
        if Awins >= 6 and Awins - Bwins >= 2:
            return Awins, Bwins
        elif Bwins >= 6 and Bwins - Awins >= 2:
            return Awins, Bwins
        if Awins == 6 and Bwins == 6 and tiebreak:
            return play_tiebreak(probA, verbose)

# this function only takes 1 parameter, probA       
def play_match(probA):
    # we start with set number 1 and and assume that both players A and B
    # each start with 0 wins(Awins and Bwins) and we also need to initialize
    # the number of games that each has won(Asets and Bsets)
    set_num = 1
    Asets = 0
    Bsets = 0
    Awins = 0
    Bwins = 0
    # Use this loop for sets 1 and 2 so that tiebreak can be set to True
    while set_num <= 2:
        # We call the play_set function to get how many games each player won
        # in the set
        Asets, Bsets = play_set(probA, True, False)
        # If A won more games than B, add 1 to Awins which represents A
        # winning a set. Otherwise, add 1 to Bwins which represents B winning
        # a set
        if Asets > Bsets:
            Awins += 1
        else:
            Bwins += 1
        # print the info about what set it is and who won
        print("Set Number:", set_num)
        print("Player A has won", Awins, "sets")
        print("Player B has won", Bwins, "sets")
        print("")
        # add one to set_num to represent going on to the next set after we
        # have determined who the winner is
        set_num += 1
        # If A wins both sets, then return "A"
        if Awins == 2:
            return "A"
        # If B wins both sets, then return "B"
        elif Bwins == 2:
            return "B"
    # Go to this loop only when we get to set 3 and Players A and B each have
    # 1 set win
    while set_num == 3 and Awins == Bwins:
        # Do the same thing as the first loop, but set tiebreak to be False
        Asets, Bsets = play_set(probA, False, False)
        if Asets > Bsets:
            Awins += 1
            print("Set Number:", set_num)
            print("Player A has won", Awins, "sets")
            print("Player B has won", Bwins, "sets")
            print("")
            return "A"
        else:
            Bwins += 1
            print("Set Number:", set_num)
            print("Player A has won", Awins, "sets")
            print("Player B has won", Bwins, "sets")
            print("")
            return "B"

# print the introduction to the program and take no parameters
def print_intro():
    print("This program simulates a tennis match between two players,")
    print("Player A and Player B. To win a match, each player must win")
    print("2 out of the three sets. To win a set, a player must win 6")
    print("games with a 2 game advantage. For the first two sets, if both")
    print("players win 6 games, a tiebreak game is played. The tiebreak")
    print("is a game to 7 points that must be won by 2. The program will")
    print("tell you the winner based on the probability that Player A will")
    print("win an individual point. Have fun!")
    print("")

# This function gets the input for the probability that Player A will win
# each point and only takes decimals between 0 and 1
def get_inputs():
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
            print("The probability must be a real number.")
    # return the good input
    return probA

# This function takes 1 parameter and prints a message to congratulate the
# winner of the match
def print_summary(winner):
    if winner == "A":
        print("Congrats Player A! You Won!")
    elif winner == "B":
        print("Congrats Player B! You Won!")

# The main function brings it all together
def main():
    # call print_intro to introduce the program
    print_intro()
    # call get_inputs and set it to be probA
    probA = get_inputs()
    # use what we got from get_inputs() to play the match and set the result
    # equal to the variable winner
    winner = play_match(probA)
    # use winner to run the print_summary function
    print_summary(winner)
# Run the main function
main()


# Everything below here is a test case. Run these programs to ensure that
# when Player A has a 50% chance of winning, that player A wins about half
# of the games, sets, and matches
def test_play_game():
    A = 0
    B = 0
    for i in range(0, 100):
        if play_game(0.5) == "A":
            A += 1
        else:
            B += 1
    print("Player A won", A, "games")
    print("Player B won", B, "games")

def test_play_set():
    A = 0
    B = 0
    for i in range(0, 100):
        Awins, Bwins = play_set(0.5)
        if Awins > Bwins:
            A += 1
        else:
            B += 1
    print("Player A won", A, "sets")
    print("Player B won", B, "sets")

# This one takes a little extra time since it has to do the print statements   
def test_play_match():
    A = 0
    B = 0
    for i in range(0, 100):
        if play_match(0.5) == "A":
            A += 1
        else:
            B += 1
    print("Player A won", A, "matches")
    print("Player B won", B, "matches")
