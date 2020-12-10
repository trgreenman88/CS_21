# Trent Greenman
# CS 21, Fall 2018
# Program: Archery

# Import graphics
from graphics import *
# This function creates the target
def create_target_window():
    # Creates the graphics window
    win = GraphWin()
    # Set the size of the graph
    win.setCoords(-6, -6, 6, 6)
    # Set the color of the background
    win.setBackground("gray")
    # Set a point in the center so the circles are all centered
    p = Point(0, 0)
    # Create the outer white circle with radius 5
    c5 = Circle(p, 5)
    c5.setFill("white")
    c5.draw(win)
    # Create the black circle with radius 4 over the white circle
    c4 = Circle(p, 4)
    c4.setFill("black")
    c4.draw(win)
    # Create the blue circle with radius 3 over the black circle
    c3 = Circle(p, 3)
    c3.setFill("blue")
    c3.draw(win)
    # Create the red circle with radius 2 over the blue circle
    c2 = Circle(p, 2)
    c2.setFill("red")
    c2.draw(win)
    # Create the inside yellow circle with radius 1 over the red circle
    c1 = Circle(p, 1)
    c1.setFill("yellow")
    c1.draw(win)
    # return the window in which the target is drawn
    return win
# This function gives us the score of each arrow shot
def get_score(point):
    # Initialize the score to be 0
    score = 0
    # For all of these, if the value of point (given in main()) is
    # less than the radius ** 2, then add the given point values
    
    # If the arrow hits the yellow circle, add 9 points to score
    if point <= 1:
        score += 9
    # If the arrow hits the red circle, add 7 points to score
    elif point <= 4:
        score += 7
    # If the arrow hits the blue circle, add 5 points to score
    elif point <= 9:
        score += 5
    # If the arrow hits the black circle, add 3 points to score
    elif point <= 16:
        score += 3
    # If the arrow hits the white circle, add 1 point to score
    elif point <= 25:
        score += 1
    # If the arrow doesn't hit the target, add 0 points to score
    else:
        score += 0
    # Return the arrow's score as an integer
    return score
# The main function gets the mouse clicks
def main():
    # Call the first function
    win = create_target_window()
    # Initialize the total score to start at 0
    total = 0
    # Keep taking arrow shots until the player presses "q"
    while win.checkKey() != "q":
        # Have the score show up on the graphics window. Center it
        # at (0, -5.5) so it is right below the target
        t = Text(Point(0,-5.5), "Current Score: " + str(total))
        # Draw the text on the graphics window
        t.draw(win)
        # If there is a mouse click, set this point to be p1
        p1 = win.checkMouse()
        # Only execute the following code if there is actually a mouse
        # click. Without the mouse click, p1 has no value and we cannot
        # draw the points or get x and y values for a nonexistant point
        if type(p1) == Point:
            # Draw the point
            p1.draw(win)
            # Call the score function for each arrow and add it to the
            # total score. We want to have point in get_score(point) be
            # equal to x**2 + y**2 so we can use pythagorean's theorem
            # to make sure our point is inside a given radius
            total += get_score(p1.getX() ** 2 + p1.getY() ** 2)
            # Create a gray rectangle to cover up the score each time so
            # that we do not end up with a bunch of overlaped scores and
            # we can only see the most recent score
            r = Rectangle(Point(-6,-6),Point(6,-5.1))
            r.setFill("gray")
            r.setOutline("gray")
            r.draw(win)
    # If the loop is broken by typint "q", close the window    
    win.close()
# Run the main function
main()
    



