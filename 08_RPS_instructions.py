def yes_no(question):
    valid = False
    while not valid:
        response = input(question).lower()

        if response == "yes" or response == "y":
            response = "yes"
            return response

        elif response == "no" or response == "n":
            response = "no"
            return response

        else:
            print("please answer yes / no")
            print()


def instructions():
    print()
    print("**** How to Play ****")
    print()
    print('''Choose either a number of rounds or press <enter> for
    infinite mode.
    Then for each round, choose from rock
    / paper / scissors (or xxx to quit)
    tou can type r / p / s / x if you
    don't want to type the entire word.
    The rules are...
    - Rock beat scissors
    - Scissors beats paper
    - Paper beats rock''')

    return""
# Main Routine goes here
played_before = yes_no("Have you played the game before? ")

if played_before == "no":
    instructions()

print("Program Continues")

