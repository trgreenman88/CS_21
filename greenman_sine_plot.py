# Trent Greenman
# CS 21, Fall 2018
# Program: sine plot

"""
    Module description:

    This program prints out 4 different representations for the graph of the sine function.
    The first requirement prints the graph sideways and shows half of a period. The second
    requirement prints the graph sideways and shows one periods. The third requirement
    prints the graph right side up and shows half of a period. The fourth requirement prints
    the graph right side up and shows one period.
"""

# Bring in libraries to get access to functions.
import math
import sys

#Define the main function.
def main():
    # Set the number of lines used to plot the sine function between 0 and pi.
    x_resolution = 32

    # Set a value that helps to determine the height of the "bump".
    y_resolution = 25

    while(True):
        # Ask the user for a solution choice.
        print("\n")
        print("The following graphs of the sine function are available: ")
        print("1. Graph between 0 and pi using a vertical x-axis")
        print("2. Graph between 0 and 2*pi using a vertical x-axis")
        print("3. Graph between 0 and pi using a horizontal x-axis")
        print("4. Graph between 0 and 2*pi using a horizontal x-axis")    
        print("5. Quit the program")
        print("\n")
        num_soln = int(input("Enter the number of the solution you want: "))
        print("\n")
       
        if num_soln == 1:
        
            # Print out the sine curve between 0 and pi
            # using a vertical x-axis.

            # for loop with the height of the graph being represented on the x axis
            for n in range(x_resolution):
                # set x to be a multiple of pi between 0 and pi  
                x = (n * math.pi) / (x_resolution)
                # set y to be the sin function with its height on the x axis
                y = math.sin(x)
                bar = ''
                
                # for loop with the length of the graph being represented on the y axis
                # add one to the range so that the graph stops at y_resolution*y instead
                # of at y_resolution*y-1
                for m in range(int(y_resolution*y + 1)):
                    # if an x value equals the equation for y*y_resoultion, add a *
                    # multiply y by y_resolution to scale it
                    if m == int(y*y_resolution):
                        bar += '*'
                    # if the x value does not equal the equation for y, add a space
                    else:
                        bar += ' '
                # print the solution
                print(bar)

        elif num_soln == 2:
        
            # Print out the sine curve between 0 and 2*pi
            # using a vertical x-axis.

            # for loop with the height of the graph being represented on the x axis
            for n in range(x_resolution):
                # change to x = n*math.pi*2 in order to shorten the graph so the whole
                # period of the sine graph shows
                x = (n * math.pi*2) / (x_resolution)
                y = math.sin(x)
                bar = ''

                # change the range of the y axis to be an additional y_resolution to fit
                # the entire period of the sine graph in the range
                for m in range(int(y_resolution*y+y_resolution+1)):
                    # since we increased the range, we also need to add a y_resolution to
                    # our equation
                    if m == int(y*y_resolution+y_resolution):
                        bar += '*'
                    else:
                        bar += ' '
                # print the solution
                print(bar)
        elif num_soln == 3:

            # Print out the sine curve between 0 and pi
            # using a horizontal x-axis.
            
            # start with y axis and count down
            for n in range(y_resolution,0,-1):
                bar = ''
                # create a loop for the x axis so you are now going top to bottom and
                # left to right
                for m in range(int(x_resolution)):

                    # set y = math.sin(x) (same as requirements 1 and 2)
                    x = (m * math.pi) / (x_resolution)
                    y = math.sin(x)
                    # compare a y value to a y value which is why we use n rather than m
                    # if n = y*y_resolution we add a * to bar
                    if n == int(y*y_resolution):
                        bar += '*'
                    else:
                        bar += ' '
                # print the solution
                print(bar)
            
        elif num_soln == 4:

            # Print out the sine curev between 0 and 2pi
            # using a horizontal x-axis

            # Change the range to go up half as high and go down below 0 so it shows
            # both the top and bottom halves of the graph
            for n in range(int(y_resolution/2),int((-y_resolution-1)/2),-1):
                bar = ''
                # The x range does not change
                for m in range(int(x_resolution)):
                    # Change to m*math.pi*2 so it shows a full period in the same amount
                    # of space. Multiply the y equation by 0.5 so it is not stretched so
                    # far up.
                    x = (m * math.pi*2) / (x_resolution)
                    y = 0.5*math.sin(x)
                    # if n = y*y_resolution we ad a * to bar
                    if n == int(y*y_resolution):
                        bar += '*'
                    else:
                        bar += ' '
                # print the solution
                print(bar)
                  
        elif num_soln == 5:

            # Quit the program

            sys.exit(0)
            
# Run the main function.
main()

