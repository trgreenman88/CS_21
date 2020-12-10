# Trent Greenman
# CS 21, Fall 2018
# Program: scan and explore

def scan(matrix, num_rows, num_cols):
# Requirement 4 (Bad inputs)
    # makes sure that matrix is a list
    if type(matrix) != list:
        return None
    # makes sure that matrix is not empty
    elif matrix == []:
        return None
    # makes sure that all entries in matrix are integers
    for i in matrix:
        if type(i) != int:
            return None
    # makes sure that num_rows is an integer
    if type(num_rows) != int:
        return None
    # makes sure that num_cols is an integer
    elif type(num_cols) != int:
        return None
    # makes sure that num_rows is positive
    elif num_rows <= 0:
        return None
    # makes sure that num_cols is positive
    elif num_cols <= 0:
        return None
    # makes sure that the number of rows times the number of
    # columns gives the number of items in the matrix
    elif len(matrix) != num_rows * num_cols:
        return None
# Requirement 4 (End)

    # initialize the new list which will be what we add our
    # values to from matrix
    new = []
    # iterate through the rows
    for j in range(0, num_rows):
        # if the number of rows is even then iterate through
        # the columns forwards
        if j % 2 == 0:
            for k in range(0, num_cols):
                # add each value in the columns to new
                new.append(matrix[k + j * num_cols])
        # if the number of rows is even then iterate through
        # the columns backwards
        else:
            for k in range(num_cols - 1, -1, -1):
                # add each column value in the odd rows in
                # reverse order to new
                new.append(matrix[k + j * num_cols])
    return new


def explore(matrix, num_rows, num_cols):
# Requirement 4 (Bad inputs) (comments same as scan function)
    if type(matrix) != list:
        return None
    elif matrix == []:
        return None
    for i in matrix:
        if type(i) != int:
            return None
    if type(num_rows) != int:
        return None
    elif type(num_cols) != int:
        return None
    elif num_rows <= 0:
        return None
    elif num_cols <= 0:
        return None
    elif len(matrix) != num_rows * num_cols:
        return None
# Requirement 4 (End)
    # ititialize all the variables we will be using
    # new will be our output list
    new = []
    # visited will be the indexes of matrix that we have already itterated
    visited = []
    # odd_nums will determine which direction we will be going
    odd_nums = 0
    # rows tells us which row we are in
    rows = 0
    # cols tells us which column we are in
    cols = 0
    # iterate through values as long as they are in the inputted number of
    # rows and columns and are not negative
    while rows < num_rows and cols < num_cols and rows >= 0 and cols >= 0:
        # if a value is visited, the break the loop
        if rows * num_cols + cols in visited:
            break
        # if the number is even, first add it to our new list, then add the
        # index number to our visited list, and continue traveling in the
        # same direction
        if matrix[rows * num_cols + cols] % 2 == 0:
            new.append(matrix[rows * num_cols + cols])
            visited.append(rows * num_cols + cols)
        # if the number if odd, first add it to our new list, then add the
        # index number to our visited list, and then add 1 to odd_nums which
        # will make us rotate 90 degrees clockwise
        if matrix[rows * num_cols + cols] % 2 == 1:
            new.append(matrix[rows * num_cols + cols])
            visited.append(rows * num_cols + cols)
            odd_nums += 1
        # if the number of odd digits prior is divisible by 4, add one to
        # cols which is the same as going one to the right
        if odd_nums % 4 == 0:
            cols += 1
        # if the number of odd digits prior has a remainder of 1 when
        # divided by 4, then add 1 to rows which is the same as going one
        # down
        if odd_nums % 4 == 1:
            rows += 1
        # if the number of odd digits prior has a remainder of 2 when
        # divided by 4, then subtract 1 from cols which is the same as
        # going one to the left
        if odd_nums % 4 == 2:
            cols -= 1
        # if the number of odd digits prior has a remainder of 3 when
        # divided by 4, then subtract 1 from rows which is the same as
        # going up one
        if odd_nums % 4 == 3:
            rows -= 1
    return new
