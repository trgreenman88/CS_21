fo# Trent Greenman
# CS 21, Fall 2018
# Program: word base
# Worked on this project with Mike Yee

"""
    Module description:
    This is a function that accepts arbitrary string and converts it to an integer.
    It converts the code words: [the, quick, fox, dog] and assigns each value a base
    4 digit where the=0, quick=1, fox=2, and dog=3
"""
# define the convert function
def convert(in_string):
    # here I assigned innitial values to all the variables that I will be using
    # throughout the algorithm
    out_num = 0
    newword = ""
    newlist = []
    finallist = []
    # here I give the code words that will be used later
    code = ["the","quick","fox","dog"]
    # here I put the string in a list and each list item is determined by any group
    # of characters not separated by a space
    words = in_string.split()
    # nested for loop so that I can test whether each letter is alphanumeric
    for word in words:
        # add a space after each word so that I can put it back into a list later
        newword = newword + " "
        for letter in word:
            # only add the letter if it meets the following criteria (alphanumeric)
            if "A" <= letter <= "Z":
                newword = newword + letter
            if "a" <= letter <= "z":
                newword = newword + letter
            if "0" <= letter <= "9":
                newword = newword + letter
    # put my new string back into a list with split
    mylist = newword.split()
    # loop that tests whether each list item is a code word and if it is it adds
    # it to a new list
    for item in mylist:
        if item in code:
            newlist.append(item)
    # loop that turns each code word into an integer based on its index
    for thing in newlist:
        finallist += [code.index(thing)]
    # reverse the order of the final list to make the final equation work
    finallist.reverse()
    # loop with an equation that puts each number in the final list into the equation
    # to give us the final answer of out_num
    for num in finallist:
        out_num += num * 4 ** finallist.index(num)
    return(out_num)
    
# this calls back the convert function and asks to input any string
my_string = input("What is the string you want to convert? ")
soln = convert(my_string)
print("The decimal equivalent of your string is: ", soln)
# the end :)

