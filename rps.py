# rps.py 

import pickle
import random
import sys

def print_menu():
    print("Welcome to Rock, Paper. Scissors!")
    print("______________________________\n")
    print("1. Start New Game")
    print("2. Load Game")
    print("3. Quit")

def RepeatMenu():
    print("Round 2")
    print("1. Play Again")
    print("2. View Statistics")
    print("3. Quit")
    secondChoice = int(input("Enter choice: "))
            #return 0
    tieGame = 0

        #return 1
    playerWon = 0

        #return 2
    computerWon = 0
    playerName = ''
    ratio = 0

    
    if secondChoice == 1:
        secondChoice = get_menu_choice() 
        typeofHand = ["rock", "paper", "scissors"]
        playerName = input("What is your name? ")
        userPicks = input("Enter a choice (rock, paper, scissors): ")
        computerPicks = random.choice(typeofHand)
        #need an f" to put input instead (faster than str(input
        print(f"\nHello {playerName}. Let's play\n")
        print(f"\nYou chose {userPicks}, computer chose {computerPicks}!\n")

        #if it is a tie (must be first)
        if userPicks == computerPicks:
            print(f"Both you and the computer selected {userPicks}. It's a tie!")
            tieGame +=1
                

            #deal with rock
        elif userPicks == "rock":
            if computerPicks == "scissors":
                print("Rock beats scissors! You win!\n")
                tieGame +=1
                    
                    
            else:
                print("Paper beats rock! You lose.")
                playerWon +=1
                    
                #deal with paper
        elif userPicks == "paper":
            if computerPicks == "rock":
                print("Paper beats rock! You win!")
                playerWon +=1
                    
            else:
                print("Scissors beats paper! You lose.")
                computerWon +=1
                    
                    #deal with scissors
        elif userPicks == "scissors":
            if computerPicks == "paper":
                print("Scissors beats paper! You win!")
                playerWon +=1
                    
            else:
                print("Rock beats scissors! You lose.")
                computerWon +=1

        print(playerWon)
        print(computerWon)
        print(tieGame)
        if computerWon ==0:
            print("Ratio is infinity")
        else: 
            ration = playerWon / computerWon
            print("Your ration: " + ratio)
        #hold the game
        with open('game.rps','a') as fileName:
            fileName.write(str(playerName)+"\n")
            fileName.write(str(playerWon)+"\n")
            fileName.write(str(computerWon)+"\n")
            fileName.write(str(tieGame)+"\n")
        

        print("Your game was saved to the rps file")

    elif secondChoice == 2:
        playerScore = input("Who's games are you looking for:")
        filename = open('game.rps')
        lineNumber = 0
        test = False
        for i in filename:
            if test:
                
                    if lineNumber % 4 == 0:
                        test = False
                    if lineNumber % 4 ==1:
                        print("Wins: "+ str(i))
                    if lineNumber % 4 ==2:
                        print("Loses: "+ str(i))
                    if lineNumber % 4 ==3:
                        print("Ties: "+ str(i))
            else:
                    if lineNumber % 4 == 0:
                        if i.strip() == playerScore:
                            #.strip() gets rid of left and right spaces
                            print(i.strip() +" here are your stats")
                            test = True
            lineNumber +=1

            
        #leave program
    elif secondChoice == 3:
        print("Goodbye")
        sys.exit()
          
    play_again = input("\nPlay again? (y/n): ")
    if play_again.lower() == "y":
            RepeatMenu()







    


    
    
def get_menu_choice():
    # Prompt for a choice and validate it
    while (True):
        try:
            choice = int(input("\nEnter your choice: "))
            if (choice < 1 or choice > 3):
                print("Please select a valid option.")
                continue
        except:
            print("Please enter a numeric value.")
        else:
            break

    return choice

def main():
    print_menu()
    choice = get_menu_choice()

    while (True):
        #return 0
        tieGame = 0

        #return 1
        playerWon = 0

        #return 2
        computerWon = 0
        playerName = ''
        ratio = 0


        # Make a Tweet
        if (choice == 1):
            typeofHand = ["rock", "paper", "scissors"]
            playerName = input("What is your name? ")
            userPicks = input("Enter a choice (rock, paper, scissors): ")
            computerPicks = random.choice(typeofHand)
            #need an f" to put input instead (faster than str(input
            print(f"\nHello {playerName}. Let's play\n")
            print(f"\nYou chose {userPicks}, computer chose {computerPicks}!\n")

            #if it is a tie (must be first)
            if userPicks == computerPicks:
                print(f"Both you and the computer selected {userPicks}. It's a tie!")
                tieGame +=1
                

            #deal with rock
            elif userPicks == "rock":
                if computerPicks == "scissors":
                    print("Rock beats scissors! You win!\n")
                    tieGame +=1
                    
                    
                else:
                    print("Paper beats rock! You lose.")
                    playerWon +=1
                    
                #deal with paper
            elif userPicks == "paper":
                if computerPicks == "rock":
                    print("Paper beats rock! You win!")
                    playerWon +=1
                    
                else:
                    print("Scissors beats paper! You lose.")
                    computerWon +=1
                    
                    #deal with scissors
            elif userPicks == "scissors":
                if computerPicks == "paper":
                    print("Scissors beats paper! You win!")
                    playerWon +=1
                    
                else:
                    print("Rock beats scissors! You lose.")
                    computerWon +=1

            print(playerWon)
            print(computerWon)
            print(tieGame)
            if computerWon ==0:
                print("Ratio is infinity")
            else: 
                ration = playerWon / computerWon
                print("Your ration: " + ratio)
        #hold the game
        with open('game.rps','a') as fileName:
            fileName.write(str(playerName)+"\n")
            fileName.write(str(playerWon)+"\n")
            fileName.write(str(computerWon)+"\n")
            fileName.write(str(tieGame)+"\n")


            print("Your game was saved to the rps file")

        

            
        # View the history
        if (choice == 2):
            playerScore = input("Who's games are you looking for:")
            filename = open('game.rps')
            lineNumber = 0
            test = False
            for i in filename:
                if test:
                
                    if lineNumber % 4 == 0:
                        test = False
                    if lineNumber % 4 ==1:
                        print("Wins: "+ str(i))
                    if lineNumber % 4 ==2:
                        print("Loses: "+ str(i))
                    if lineNumber % 4 ==3:
                        print("Ties: "+ str(i))
                else:
                    if lineNumber % 4 == 0:
                        if i.strip() == playerScore:
                            #.strip() gets rid of left and right spaces
                            print(i.strip() +" here are your stats")
                            test = True
                lineNumber +=1

            
        #leave program
        elif (choice == 3):
            print("Goodbye")
            sys.exit()
          
        play_again = input("\nPlay again? (y/n): ")
        if play_again.lower() == "y":
            RepeatMenu()






# Call main
main()
