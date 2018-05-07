# -*- coding: utf-8 -*-
''' Capital City Quiz '''
from __future__ import print_function
import random

''' Seperate states into west, midwest, northeast, and south'''
#, "Illinois", "Michigan", "Indiana", "Ohio"
# West: Alaska, Hawaii, California, Nevada, Utah, Colorado, Idaho, Wyoming, Oregon, Washington, Montana
    # Midwest: North Dakota, South Dakota, Nebraska, Kansas, Missouri, Iowa, Minnesota, Wisconsin, Illinois, Michigan, Indiana, Ohio
    # Northeast: Delaware, Maine, Vermont, New Hampshire, Massachusetts, Connecticut, Rhode Island, New York, New Jersey, Pennsylvania, Maryland
#South west: Texas, Oklahoma, New Mexico, Arizona
#South East: Arkansas, Louisiana, Mississippi, Alabama, Georgia, Florida, North Carolina, South Carolina, Virginia, West Virginia, Kentucky, Tennessee, 
##################################
def choice(options=["Alaska", "Hawaii", "California", "Nevada", "Utah", "Colorado", "Idaho", "Wyoming", "Oregon", "Washington", "Montana","North Dakota", "South Dakota", "Nebraska", "Kansas", "Missouri", "Iowa", "Minnesota", "Wisconsin"]):
    state = random.choice(options)
    if state == "Alaska":
        alaska()
    elif state == "Hawaii":
        hawaii()
    elif state == "California":
        cali()
    elif state == "Nevada":
        neva()
    elif state == "Utah":
        utah()
    elif state == "Colorado":
        colorado()
    elif state == "Idaho":
        idaho()
    elif state == "Wyoming":
        wyo()
    elif state == "Oregon":
        oregon()
    elif state == "Washington":
        wash()
    elif state == "Montana":
        mont()
    elif state == "North Dakota":
        northDakota()
    elif state == "South Dakota":
        southDakota()
    elif state == "Nebraska":
        nebraska()
    elif state == "Kansas":
        kansas()
    elif state == "Missouri":
        missouri()
    elif state == "Iowa":
        iowa()
    elif state == "Minnesota":
        minn()
    elif state == "Wisconsin":
        wisc()
        
def printArr(options):
    option_list = ''
    for option in options[:-1]: # element -1 is left out in order to be inserted into the end fo option_list
        option_list += option + ', '
    option_list += 'or ' + options[-1] # final elements of option_list inserts 'or' and the element in options that was left out
    print("Which is the capital city: ", option_list)
    
    
    
    
def alaska(options=["Juneau", "Anchorage", "Fairbanks"]): 
    print("Your state is Alaska.")  
    printArr(options)
    guesses = 0
    answer = "Juneau"
    guess = raw_input()
    guesses+=1
     # while user answers incorrectly, continue prompting for guess
    while guess != answer:
        print('Guess again: ')
        guesses+=1
        guess = raw_input()
        
    print("Correct! You got the right answer in", guesses, "tries!")
    guesses = 0
    print("To play again, enter 'y'. To quit, press 'enter'")
    if raw_input() == 'y':
        choice()
    else:
        print("Goodbye!")
        
def cali(options=["Sacramento", "San Diego", "Los Angeles"]): 
    print("Your state is California.")   
    printArr(options)
    guesses = 0
    answer = "Sacramento"
    guess = raw_input()
    guesses+=1
    
     # while user answers incorrectly, continue prompting for guess
    while guess != answer:
        print('Guess again: ')
        guesses+=1
        guess = raw_input()
    print("Correct! You got the right answer in", guesses, "tries!")
    guesses = 0
    print("To play again, enter 'y'. To quit, press 'enter'.")
    if raw_input() == 'y':
        choice()
    else:
        print("Goodbye!")
        
def hawaii(options=[ "Kailua","Honolulu","Kapolei"] ):
    print("Your state is Hawaii.")
    printArr(options)
    guesses = 0
    answer = "Honolulu"
    guess = raw_input()
    guesses+=1
    
     # while user answers incorrectly, continue prompting for guess
    while guess != answer:
        print('Guess again: ')
        guesses+=1
        guess = raw_input()
    print("Correct! You got the right answer in", guesses, "tries!")
    guesses = 0
    print("To play again, enter 'y'. To quit, press 'enter'.")
    if raw_input() == 'y':
        choice()
    else:
        print("Goodbye!")
        
def neva(options=[ "Las Vegas", "Carson City", "Reno"]):
    print("Your state is Nevada.")
    printArr(options)
    guesses = 0
    answer = "Carson City"
    guess = raw_input()
    guesses+=1
    
     # while user answers incorrectly, continue prompting for guess
    while guess != answer:
        print('Guess again: ')
        guesses+=1
        guess = raw_input()
    print("Correct! You got the right answer in", guesses, "tries!")
    guesses = 0
    print("To play again, enter 'y'. To quit, press 'enter'.")
    if raw_input() == 'y':
        choice()
    else:
        print("Goodbye!")
        
def utah(options=["St. George","Salt Lake City", "Provo"]):
    print("Your state is Utah.")
    printArr(options)
    guesses = 0
    answer = "Salt Lake City"
    guess = raw_input()
    guesses+=1
    
     # while user answers incorrectly, continue prompting for guess
    while guess != answer:
        print('Guess again: ')
        guesses+=1
        guess = raw_input()
    print("Correct! You got the right answer in", guesses, "tries!")
    guesses = 0
    print("To play again, enter 'y'. To quit, press 'enter'.")
    if raw_input() == 'y':
        choice()
    else:
        print("Goodbye!")

def colorado(options=[ "Boulder", "Aurora", "Denver"]):
    print("Your state is Colorado")
    printArr(options)
    guesses = 0
    answer = "Denver"
    guess = raw_input()
    guesses+=1
    
     # while user answers incorrectly, continue prompting for guess
    while guess != answer:
        print('Guess again: ')
        guesses+=1
        guess = raw_input()
    print("Correct! You got the right answer in", guesses, "tries!")
    guesses = 0
    print("To play again, enter 'y'. To quit, press 'enter'.")
    if raw_input() == 'y':
        choice()
    else:
        print("Goodbye!")
        
def idaho(options=["Meridian","Boise", "Nampa"]):
    print("Your state is Idaho.")
    printArr(options)
    guesses = 0
    answer = "Boise"
    guess = raw_input()
    guesses+=1
    
     # while user answers incorrectly, continue prompting for guess
    while guess != answer:
        print('Guess again: ')
        guesses+=1
        guess = raw_input()
    print("Correct! You got the right answer in", guesses, "tries!")
    guesses = 0
    print("To play again, enter 'y'. To quit, press 'enter'.")
    if raw_input() == 'y':
        choice()
    else:
        print("Goodbye!")
        
def wyo(options=["Casper","Cheyenne", "Jackson"]):
    print("Your state is Wyoming.")
    printArr(options)
    guesses = 0
    answer = "Cheyenne"
    guess = raw_input()
    guesses+=1
    
     # while user answers incorrectly, continue prompting for guess
    while guess != answer:
        print('Guess again: ')
        guesses+=1
        guess = raw_input()
    print("Correct! You got the right answer in", guesses, "tries!")
    guesses = 0
    print("To play again, enter 'y'. To quit, press 'enter'.")
    if raw_input() == 'y':
        choice()
    else:
        print("Goodbye!")
        
def oregon(options=[ "Portland","Salem", "Bend"]):
    print("Your state is Oregon.")
    printArr(options)    
    guesses = 0
    answer = "Salem"
    guess = raw_input()
    guesses+=1
    
     # while user answers incorrectly, continue prompting for guess
    while guess != answer:
        print('Guess again: ')
        guesses+=1
        guess = raw_input()
    print("Correct! You got the right answer in", guesses, "tries!")
    guesses = 0
    print("To play again, enter 'y'. To quit, press 'enter'.")
    if raw_input() == 'y':
        choice()
    else:
        print("Goodbye!")
        
def wash(options=["Olympia", "Seattle", "Vancouver"]):
    print("Your state is Washington.")
    printArr(options)
    guesses = 0
    answer = "Olympia"
    guess = raw_input()
    guesses+=1
    
     # while user answers incorrectly, continue prompting for guess
    while guess != answer:
        print('Guess again: ')
        guesses+=1
        guess = raw_input()
    print("Correct! You got the right answer in", guesses, "tries!")
    guesses = 0
    print("To play again, enter 'y'. To quit, press 'enter'.")
    if raw_input() == 'y':
        choice()
    else:
        print("Goodbye!")
        
def mont(options=["Missoula","Helena", "Billings"]):
    print("Your state is Montana.")
    printArr(options)
    guesses = 0
    answer = "Helena"
    guess = raw_input()
    guesses+=1
    
     # while user answers incorrectly, continue prompting for guess
    while guess != answer:
        print('Guess again: ')
        guesses+=1
        guess = raw_input()
    print("Correct! You got the right answer in", guesses, "tries!")
    guesses = 0
    print("To play again, enter 'y'. To quit, press 'enter'.")
    if raw_input() == 'y':
        choice()
    else:
        print("Goodbye!")
#################################    
    

        
def northDakota(options=["Minot", "Bismarck", "Fargot"]):
    print("Your state is North Dakota.")
    printArr(options)
    guesses = 0
    answer = "Bismarck"
    guess = raw_input()
    guesses+=1
    
     # while user answers incorrectly, continue prompting for guess
    while guess != answer:
        print('Guess again: ')
        guesses+=1
        guess = raw_input()
    print("Correct! You got the right answer in", guesses, "tries!")
    guesses = 0
    print("To play again, enter 'y'. To quit, press 'enter'.")
    if raw_input() == 'y':
        choice()
    else:
        print("Goodbye!")
        
def southDakota(options=["Sioux Falls", "Pierre”, “Yankton"]):
    print("Your state is South Dakota.")
    printArr(options)
    guesses = 0
    answer = "Pierre"
    guess = raw_input()
    guesses+=1
    
     # while user answers incorrectly, continue prompting for guess
    while guess != answer:
        print('Guess again: ')
        guesses+=1
        guess = raw_input()
    print("Correct! You got the right answer in", guesses, "tries!")
    guesses = 0
    print("To play again, enter 'y'. To quit, press 'enter'.")
    if raw_input() == 'y':
        choice()
    else:
        print("Goodbye!")

def nebraska(options=["Omaha", "Lincoln", "Grand Island"]):
    print("Your state is Nebraska.")
    printArr(options)
    guesses = 0
    answer = "Lincoln"
    guess = raw_input()
    guesses+=1
    
     # while user answers incorrectly, continue prompting for guess
    while guess != answer:
        print('Guess again: ')
        guesses+=1
        guess = raw_input()
    print("Correct! You got the right answer in", guesses, "tries!")
    guesses = 0
    print("To play again, enter 'y'. To quit, press 'enter'.")
    if raw_input() == 'y':
        choice()
    else:
        print("Goodbye!")
        

def kansas(options=["Kansas City", "Topeka", "Wichita"]):
    print("Your state is Kansas.")
    printArr(options)
    guesses = 0
    answer = "Topeka"
    guess = raw_input()
    guesses+=1
    
     # while user answers incorrectly, continue prompting for guess
    while guess != answer:
        print('Guess again: ')
        guesses+=1
        guess = raw_input()
    print("Correct! You got the right answer in", guesses, "tries!")
    guesses = 0
    print("To play again, enter 'y'. To quit, press 'enter'.")
    if raw_input() == 'y':
        choice()
    else:
        print("Goodbye!")

def missouri(options=["St. Louis", "Jefferson City", "Branson"]):
    print("Your state is Missouri.")
    printArr(options)
    guesses = 0
    answer = "St. Louis"
    guess = raw_input()
    guesses+=1
    
     # while user answers incorrectly, continue prompting for guess
    while guess != answer:
        print('Guess again: ')
        guesses+=1
        guess = raw_input()
    print("Correct! You got the right answer in", guesses, "tries!")
    guesses = 0
    print("To play again, enter 'y'. To quit, press 'enter'.")
    if raw_input() == 'y':
        choice()
    else:
        print("Goodbye!")
        
def iowa(options=["Des Moines", "Daven Port", "Iowa City"]):
    print("Your state is Iowa.")
    printArr(options)
    guesses = 0
    answer = "Des Moines"
    guess = raw_input()
    guesses+=1
    
     # while user answers incorrectly, continue prompting for guess
    while guess != answer:
        print('Guess again: ')
        guesses+=1
        guess = raw_input()
    print("Correct! You got the right answer in", guesses, "tries!")
    guesses = 0
    print("To play again, enter 'y'. To quit, press 'enter'.")
    if raw_input() == 'y':
        choice()
    else:
        print("Goodbye!")

def minn(options=["Winona", "Saint Paul", "Minneapolis"]):
    print("Your state is Minnesota.")
    printArr(options)
    guesses = 0
    answer = "Saint Paul"
    guess = raw_input()
    guesses+=1
    
     # while user answers incorrectly, continue prompting for guess
    while guess != answer:
        print('Guess again: ')
        guesses+=1
        guess = raw_input()
    print("Correct! You got the right answer in", guesses, "tries!")
    guesses = 0
    print("To play again, enter 'y'. To quit, press 'enter'.")
    if raw_input() == 'y':
        choice()
    else:
        print("Goodbye!")
    
def wis(options=["Green Bay", "Milwaukee", "Madison"]):
    print("Your state is Wisconsin.")
    printArr(options)
    guesses = 0
    answer = "Madison"
    guess = raw_input()
    guesses+=1
    
     # while user answers incorrectly, continue prompting for guess
    while guess != answer:
        print('Guess again: ')
        guesses+=1
        guess = raw_input()
    print("Correct! You got the right answer in", guesses, "tries!")
    guesses = 0
    print("To play again, enter 'y'. To quit, press 'enter'.")
    if raw_input() == 'y':
        choice()
    else:
        print("Goodbye!")
    

# Start of program
print('Welcome to the Capital City Quiz Game!')
choice()


    

  

    