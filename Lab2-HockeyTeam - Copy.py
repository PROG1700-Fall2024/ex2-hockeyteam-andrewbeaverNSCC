# LAB 2 - HOCKEY TEAM
#Write a program that will ask the user to enter the name of a hockey team, how many wins the team has and 
# how many losses #the team has.

#The program should calculate and display a single string output containing the team name, it's win-loss 
# ratio and the win #percentage formatted to 4 decimal places.

#Ex: The Calgary Flames have 10 wins and 5 losses, with a win percentage of 0.6667.

#Purpose/Concepts: Input and output to screen, string concatentation, string formatting, datatype casting, 
# simple math operations

def main():
    # YOUR CODE STARTS HERE, each line must be indented (one tab)
    #team names
    fullTeam1 = "Kuala Lumpur" + " " + "Jewels" 

    fullTeam2 = "Singapore" + " " + "Beavers" 

    fullTeam3 = "Ho Chi Ming" + " " + "Whales"

    fullTeam4 = "Bogota" + " " + "Frogs"

    #number of wins/losses and math
    wins1 = 8
    losses1 = 4

    wins2 = 5
    losses2 = 7

    wins3 = 9
    losses3 = 3

    wins4 = 2
    losses4 = 10
    
    winFormula1 = (wins1/12)
    winFormula2 = (wins2/12)
    winFormula3 = (wins3/12)
    winFormula4 = (wins4/12)

    winPercentage1 = ("{:.4f}".format(winFormula1))
    winPercentage2 = ("{:.4f}".format(winFormula2))
    winPercentage3 = ("{:.4f}".format(winFormula3))
    winPercentage4 = ("{:.4f}".format(winFormula4))

    #welcome user to the software
    print("Welcome to the Hockey win/loss database. We tell you how many wins, how many losses and their win percentage.\n Just ask and you shall receive!")
    
    #print team names
    print("We offer statistics for the following teams:\nJewels\nBeavers\nWhales\nFrogs")
    
    
    #user inputs team name
    userTeam = input("Please enter the team here: ")
    
    #print team name and record
    print(("The record and win-loss ratio is 8-4 and" + str(winPercentage1), "for the " + fullTeam1) * (userTeam =="Jewels"),end="")
    print(("The record and win-loss ratio is 5-7 and " + str(winPercentage2), "for the " + fullTeam2) * (userTeam =="Beavers"), end="")
    print(("The record and win-loss ratio is 9-3 and "+ str(winPercentage3), "for the " + fullTeam3)* (userTeam =="Whales"), end="")
    print(("The record and win-loss ratio is 2-10 and "+ str(winPercentage4), "for the " + fullTeam4)* (userTeam =="Frogs"))

    #end the program
    print("Thanks for using this program!")
    # YOUR CODE ENDS HERE

main()