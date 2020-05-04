"""
CTEC 121
<Grant Parkinson>
<Mod 3 lab 1>
<assignment/lab description
"""

""" IPO template
Input(s): list/description
Process: description of what function does
Output: return value and description
"""


def main():
    '''
    # conditional expressions

    # literal
    print("\nBoolean literals")
    print(True)
    print(False)
    print(type(True))
    print(type(False))

    # Relational operators
    print("Relational operators")
    print("3 < 5", 3 < 5)
    print("3 <= 3", 3 <= 3)
    print("3==3", 3 == 3)
    print("3>=5", 3 >= 5)
    print("3!=5", 3 != 5)
    print()

    # using variables
    x = 3
    y = 5
    print("using variables")
    print("x:", x, "y:", y)
    print("x<y", x < y)
    print("x!=y", x != y)
    print()

    # simple if statement
    print("x:", x, "y:", y)
    if x < y:
        print("x < y")

    if x > y:
        print("x > y")

    print("end simple if example")
    print()

    # if/else statement
    print("if/else statement")
    print("x:", x, "y:", y)
    if x < y:
        print("x < y")
    else:
        print("x >= y")

    x = 6
    print("x:", x, "y:", y)
    if x < y:
        print("x < y")
    else:
        print("x >= y")
    print("end if/else example\n")


# excercise 3-1
    print("Excercise")
    for x in range(1, 11):
        if x % 2 == 0:
            outputString = "even"
        else:
            outputString = "odd"
        print(x, outputString)
    print()

    # alphabetize names
    firstLetterOfName = "G"

    print("Multi-way if example")
    if firstLetterOfName == "A":
        print("A")
    elif firstLetterOfName == "B":
        print("B")
    elif firstLetterOfName == "C":
        print("C")
    # ...
    elif firstLetterOfName == "G":
        print("G")
    # ...
    elif firstLetterOfName == "Y":
        print("Y")
    else:  # default case: name starts with "Z"
        print("Z")
    print()
    '''
    try:
        print(4/0)
    except:
        print("\nThere was a divide by zero error. Exiting\n")
        exit()


main()
