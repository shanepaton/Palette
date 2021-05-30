__author__ = "Shane Paton"
__copyright__ = "Copyright 2021, Shane Paton"
__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = "Shane Paton"
__email__ = "spaton08@gmail.com"
__status__ = "Development"

import sys
variables = [None] * 9
inputVariable = None

# This grabs the file you want to load from the command line argument
file_name = sys.argv[1]
line = []                                   # Declare a list called line which will store all lines from the file.
with open (file_name, 'rt') as inputFile:   # Opens the file.
    for inputLine in inputFile:             # For everyline line in the file,
        line.append(inputLine)              # store its contents in the array line[].

# Enforce the WASH which is used to close the file input
if line[-1] != "WASH":
    raise Exception("Error: No WASH statement.")

for x in range(len(line)):
    if "BOTTLE" in line[x]:
        res = [int(i) for i in line[x].split() if i.isdigit()]
        typeCheckText = line[x].replace('BOTTLE ' + str(res[0]) + " = ", '')
        # String is now text Hello WOORD

        # These if statements set types and remove their declarations from their strings

        if "text" in typeCheckText:
            variables[res[0]] = str(typeCheckText.replace('text ', ''))

        if "number" in typeCheckText:
            variables[res[0]] = int(typeCheckText.replace('number ', ''))

        if "decimal" in typeCheckText:
            variables[res[0]] = float(typeCheckText.replace('decimal ', ''))

    # Paint prints to the console function
    if "PAINT" in line[x].split():
        # Self Explanatory: Print value from string minus `PAINT `
        if "USING BOTTLE" in line[x]:
            formatedUseText = line[x].replace('PAINT USING BOTTLE ', '')
            res = [int(i) for i in formatedUseText.split() if i.isdigit()]
            print(variables[res[0]], end="")
        else:
            print(line[x].replace('PAINT ', ''), end="")

    # Blend adds values and stores them in a Bottle
    if "BLEND" in line[x].split():
        # Removes `BLEND ` from the string
        formatedText = line[x].replace('BLEND ', '')

        # Searches for all numbers in the operation and stores them in the array res[]
        res = [int(i) for i in formatedText.split() if i.isdigit()]

        # Sets a variable to last value of the array which is the variable to store to
        variableValue = res[-1]

        # Removes it since it was added to the total
        added = sum(res) - res[-1]

        # Sets the variable to the sum
        variables[variableValue] = added

    # Redraw creates a loop taking in a value for its itterations
    if "REDRAW" in line[x].split():
        # Removes `REDRAW ` from the string
        formatedText = line[x].replace('REDRAW ', '')

        # Searches for the itteration value 
        res = [int(i) for i in formatedText.split() if i.isdigit()]

        # Sets a value equal to the itteration value
        times = res[0]

        # If PAINT is below it then print for the amount of times
        if "PAINT" in line[x + 1]:
            for Z in range(times):
                print(line[x + 1].replace('PAINT ', ''), end="")

    # Input is used to take input from the user
    if "INPUT" in line[x].split():
        tempInput = input(">")

        # Stores the input gathered from input() and stores it in the global input variable
        inputVariable = tempInput

    # Should is a conditional statement which checks if the input is equal to the number 1
    if "SHOULD" in line[x].split():
        
        formatedText = line[x].replace('SHOULD ', '')
        
        if "EQUALINPUT" in formatedText.split():

            if int(inputVariable) == 1:

                if "SHOULDREDRAW" in line[x + 1]:
                    formatedRedrawText = line[x + 1].replace('SHOULDREDRAW ', '')
                    res = [int(i) for i in formatedRedrawText.split() if i.isdigit()]
                    shouldTimes = res[0]
                    if "EQUALPAINT" in line[x + 2]:
                        for Z in range(shouldTimes):
                            print(line[x + 2].replace('EQUALPAINT ', ''), end="")

    if "SHOULD NOT" in line[x]:
        #Formats for INPUT statement
        formatedText = line[x].replace('SHOULD NOT ', '')

        if "EQUALINPUT" in formatedText:
            if int(inputVariable) != 1:
                if "REDRAW" in line[x + 1]:
                    formatedRedrawText = line[x + 1].replace('REDRAW ', '')
                    res = [int(i) for i in formatedRedrawText.split() if i.isdigit()]
                    shouldTimes = res[0]
                    if "EQUALPAINT" in line[x + 2]:
                        for Z in range(shouldTimes):
                            print(line[x + 2].replace('EQUALPAINT ', ''), end="")

                if "EQUALPAINT" in line[x + 1]:
                    formatedPrintText = line[x + 1].replace('EQUALPAINT ', '')
                    res = [int(i) for i in formatedPrintText.split() if i.isdigit()]
                    print(formatedPrintText, end="")

    #Quits and closes the file read buffer
    if "WASH" in line[x]:
        inputFile.close()
        exit()