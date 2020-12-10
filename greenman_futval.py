# Trent Greenman
# CS 21, Fall 2018
# Program: futval.py (Modification #4)

def main():
    print("This program calculates the future value")
    print("of a 10-year investment.")
# Get inputs for yearly amount, interest rate, number of years for the
# investment, number of times compounded, and set the total amount equal to 0
    yearly_amt = eval(input("Enter the initial principal: "))
    apr = eval(input("Enter the annual interest rate: "))
    time = eval(input("Enter the number of years for your investment:"))
    num_compound = eval(input("Enter the number of compounding periods per year:"))
    total_amt = 0
    # for loop to evaluate the equation 'time' times
    for i in range(0,time):
        total_amt = (yearly_amt + total_amt) * (1 + apr / num_compound)**num_compound

    print("The value in", time, "years is:", total_amt)

main()
