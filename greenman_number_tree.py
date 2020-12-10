# Trent Greenman
# CS 21, Fall 2018
# Program: number tree

# get_number takes 2 parameters, n and k, which are coordinates and gives the
# value of pascal's triangle based on the the row (n) and column (k)
def get_number(n,k):
    # if k is greater than n, return None
    if k > n:
        return None
    else:
        # if k is equal to n (all points on the far right of the nummber tree)
        # then return 1
        if k == n:
            return 1
        # if k is zero (all points on the far left of the number tree), then
        # return 1
        elif k == 0:
            return 1
        # otherwise, return the sum of the two numbers above it which are at
        # positions (n-1,k) and (n-1,k-1)
        else:
            return get_number(n-1,k) + get_number(n-1,k-1)

# get_row_sum takes 1 parameter, i, which is a row of pascal's triangle, and
# it gives the sum of all the numbers in that row
def get_row_sum(i):
    # initialize the sum (b) to be zero
    b = 0
    # take the sum i times since the number of rows always equals the number of
    # columns in pascal's triangle
    for a in range(0, i):
        # add the value at each coordinate. a increases by 1 each time we iterate
        # so we can get each column
        b += get_number(i-1,a)
    # return the total sum of the row
    return b

# get_alternating_sum takes the sum of each row, but the sign changes between +
# and - from term to term. It takes one parameter which is the row number
def get_alternating_sum(i):
    # initialize the sum (b) to be zero
    b = 0
    for a in range(0, i):
        # everything is the same as get_row_sum, except we multiply each term by
        # (-1)**a this way, when a is odd, the term is multiplied by -1 and when
        # a is even, we just multiply by 1
        b += get_number(i-1,a)*(-1)**a
    return b

# get_sum_of_squares takes the sum of each value in the row squared and takes one
# parameter which is the row number
def get_sum_of_squares(i):
    # initialize the sum (b) to be zero
    b = 0
    for a in range(0, i):
        # everything is the same as get_row_sum, except we square each term being
        # added to the sum so we get the sum of the squares in each row
        b += (get_number(i-1,a))**2
    return b

# print_tree takes one parameter (num_rows), and prints out the first num_rows of
# pascal's triangle
def print_tree(num_rows):
    # iterate throuth each individual row
    for i in range(0, num_rows):
        # go to a new line each time you start a new row except for the first row
        if i > 0:
            print("")
        # iterate through each individual value for each row and print the value of
        # pascal's triangle at each coordinate. Each time j increases, this represents
        # k increasing and each time num_rows increase, this represents n increasing
        for j in range(0,i+1):
            print(get_number(i,j), end=" ")

# get_diagonal_sum takes one parameter (i) which is the number of rows and gives the
# sum of terms added diagonally going up to the right starting at the first term in
# the ith tow.
def get_diagonal_sum(i):
    # initialize the sum to be zero
    b = 0
    # we will be using 2 separate cases for odd rows and even rows since the total
    # number of terms being added is different for odd and even values of i
    if i % 2 == 0:
        # for even rows, the number of terms being added is always half the row
        # number so we iterate from 0 to i//2
        for a in range(0, (i//2)):
            # each time we run through the loop, add the term to b and the subtract
            # 1 from i which represents going up 1 in the row and a will increase by
            # 1 each time we go through the loop which represents going to the right
            # by 1 unit.
            b += get_number(i-1,a)
            i -= 1
        # return the total sum
        return b
    # odd cases now
    else:
        # for odd rows, the number of terms being added is always half the row
        # number + 1 so we iterate from 0 to (i//2)+1
        for a in range(0, (i//2)+1):
            # same explanation as even cases
            b += get_number(i-1,a)
            i -= 1
        # return the total sum
        return b

# print_pretty_tree takes 1 parameter (num_rows) and prints out pascal's triangle,
# but it is now centered and each odd term is a star and each even term is a space
def print_pretty_tree(num_rows):
    # iterate through all the rows
    for i in range(0, num_rows):
        # go to the next line after each row is completed
        print("")
        # iterate through all the values in each row, start at -1 so we can include
        # the first value
        for j in range(-1,i+1):
            # when j is -1, print (num_rows-i) spaces so we can center the tree
            if j == -1:
                print(" " * (num_rows-i), end="")
            # if get_number is odd, then print *
            elif get_number(i,j) % 2 == 1:
                print("*", end=" ")
            # if get_number is even, the print a space
            else:
                print(" ", end=" ")
