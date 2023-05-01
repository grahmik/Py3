#!/bin/python3
# Mike G 4/26/2023

####  Welcome to Rock, Paper, Scissors!  ####
####  This is a program that will allow  ####
####  you to play a game of Rock, Paper, ####
####   Scissors against the computer.    ####
####   I had so much fun writing this    ####
####  program. I really hope you like it ####
####              ENJOY!                 ####





# Import modules
import time
import random

# Title Screen: print ASCii title one line at a time with an interval of 0.1
print("\033[94m\n _______    ______    ______   __    __                             ")
time.sleep(.1)
print("/       \  /      \  /      \ /  |  /  |                                      ")
time.sleep(.1)
print("$$$$$$$  |/$$$$$$  |/$$$$$$  |$$ | /$$/                                       ")
time.sleep(.1)
print("$$ |__$$ |$$ |  $$ |$$ |  $$/ $$ |/$$/                                        ")
time.sleep(.1)
print("$$    $$< $$ |  $$ |$$ |      $$  $$<                                         ")
time.sleep(.1)
print("$$$$$$$  |$$ |  $$ |$$ |   __ $$$$$  \                                        ")
time.sleep(.1)
print("$$ |  $$ |$$ \__$$ |$$ \__/  |$$ |$$  \                                       ")
time.sleep(.1)
print("$$ |  $$ |$$    $$/ $$    $$/ $$ | $$  |                                      ")
time.sleep(.1)
print("$$/   $$/  $$$$$$/   $$$$$$/  $$/   $$/                                       ")
time.sleep(.1)
print("")
time.sleep(.1)
print("")
time.sleep(.1)
print(" _______    ______   _______   ________  _______                              ")
time.sleep(.1)
print("/       \  /      \ /       \ /        |/       \                             ")
time.sleep(.1)
print("$$$$$$$  |/$$$$$$  |$$$$$$$  |$$$$$$$$/ $$$$$$$  |                            ")
time.sleep(.1)
print("$$ |__$$ |$$ |__$$ |$$ |__$$ |$$ |__    $$ |__$$ |                            ")
time.sleep(.1)
print("$$    $$/ $$    $$ |$$    $$/ $$    |   $$    $$<                             ")
time.sleep(.1)
print("$$$$$$$/  $$$$$$$$ |$$$$$$$/  $$$$$/    $$$$$$$  |                            ")
time.sleep(.1)
print("$$ |      $$ |  $$ |$$ |      $$ |_____ $$ |  $$ |                            ")
time.sleep(.1)
print("$$ |      $$ |  $$ |$$ |      $$       |$$ |  $$ |                            ")
time.sleep(.1)
print("$$/       $$/   $$/ $$/       $$$$$$$$/ $$/   $$/                             ")
time.sleep(.1)
print("")                                                                              
time.sleep(.1)
print("")                                                                              
time.sleep(.1)
print("  ______    ______   ______   ______    ______    ______   _______    ______  ")
time.sleep(.1)
print(" /      \  /      \ /      | /      \  /      \  /      \ /       \  /      \ ")
time.sleep(.1)
print("/$$$$$$  |/$$$$$$  |$$$$$$/ /$$$$$$  |/$$$$$$  |/$$$$$$  |$$$$$$$  |/$$$$$$  |")
time.sleep(.1)
print("$$ \__$$/ $$ |  $$/   $$ |  $$ \__$$/ $$ \__$$/ $$ |  $$ |$$ |__$$ |$$ \__$$/ ")
time.sleep(.1)
print("$$      \ $$ |        $$ |  $$      \ $$      \ $$ |  $$ |$$    $$< $$      \ ")
time.sleep(.1)
print(" $$$$$$  |$$ |   __   $$ |   $$$$$$  | $$$$$$  |$$ |  $$ |$$$$$$$  | $$$$$$  |")
time.sleep(.1)
print("/  \__$$ |$$ \__/  | _$$ |_ /  \__$$ |/  \__$$ |$$ \__$$ |$$ |  $$ |/  \__$$ |")
time.sleep(.1)
print("$$    $$/ $$    $$/ / $$   |$$    $$/ $$    $$/ $$    $$/ $$ |  $$ |$$    $$/ ")
time.sleep(.1)
print(" $$$$$$/   $$$$$$/  $$$$$$/  $$$$$$/   $$$$$$/   $$$$$$/  $$/   $$/  $$$$$$/\033[0m by: Mike G\n")
time.sleep(.1)
print("")
time.sleep(.1)
print("")
time.sleep(.1)
print("\033[92m    _______           _______                 _______")
time.sleep(.2)
print("---'   ____)      ---'   ____)____        ---'   ____)______")
time.sleep(.2)
print("      (_____)                ______)                  ______)_")
time.sleep(.2)
print("      (_____)                _______)                 ________)  ")
time.sleep(.2)
print("      (____)               ________)                 (____)")
time.sleep(.2)
print("---.__(___)           ---.________)            ---.__(___)   \033[0m\n")
time.sleep(.2)
print("")
time.sleep(.2)




# Scores
player_score = 0
ai_score = 0

# Name variables
ai_name = "Tom"
player_name = input("What is your name? ")

# Introduction: 
print("\nHello " + player_name + ", My name is " + ai_name + ", and I would love to play Rock, Paper, Scissors with you.")
print("I challenge you to a duel! Best 3 out of 5!")
ready = input("\nAre you ready to play? (Yes or No) ").lower()

if ready == "yes": 
    print("\nOKAY! Here we go!\n")
else:
    print("\nYou didn't type 'Yes', See you later!\n")
    time.sleep(.5)
    quit()
time.sleep(2)

# Beginning of while loop for the entire game
while True:
    # Prints "one, two, three, shoot" on the same line in 1 second intervals
    while True:
        print("One!", end="\r")
        time.sleep(1)
        print("Two!", end="\r")
        time.sleep(1)
        print("Three!", end="\r")
        time.sleep(1)
        print("Shoot!", end="\r")
        time.sleep(1)
        break

    # Records the users choice of rock, paper or scissors
    player_move = input("Choose Rock, Paper or Scissors: ").lower()

    # A list from which a random value is chosen and sent to the screen that is equal to the computer's choice
    ai_list = ["rock!", "paper!", "scissors!"]
    ai_choice = random.choice(ai_list)
    time.sleep(1)
    print("\nI choose " + ai_choice + "\n")
    time.sleep(2)

    # compare user choice against computer choice | add 1 point for winner of each round until someone reaches 3 points
    if player_move == "rock" and ai_choice == "scissors!":
        print("\033[92mYou win!\033[0m")
        player_score += 1
        print("SCORE: " + ai_name + ": " + str(ai_score) + " | " + player_name + ": " + str(player_score))
        print("############################\n")
        time.sleep(1)
    elif player_move == "rock" and ai_choice == "paper!":
        print("\033[91mYou lose!\033[0m")
        ai_score += 1
        print("SCORE: " + ai_name + ": " + str(ai_score) + " | " + player_name + ": " + str(player_score))
        print("############################\n")
        time.sleep(1)
    elif player_move == "rock" and ai_choice == "rock!":
        print("\033[93mIt's a tie!\033[0m")
        print("SCORE: " + ai_name + ": " + str(ai_score) + " | " + player_name + ": " + str(player_score))
        print("############################\n")
        time.sleep(1)
    elif player_move == "scissors" and ai_choice == "paper!":
        print("\033[92mYou win!\033[0m")
        player_score += 1
        print("SCORE: " + ai_name + ": " + str(ai_score) + " | " + player_name + ": " + str(player_score))
        print("############################\n")
        time.sleep(1)
    elif player_move == "scissors" and ai_choice == "rock!":
        print("\033[91mYou lose!\033[0m")
        ai_score += 1
        print("SCORE: " + ai_name + ": " + str(ai_score) + " | " + player_name + ": " + str(player_score))
        print("############################\n")
        time.sleep(1)
    elif player_move == "scissors" and ai_choice == "scissors!":
        print("\033[93mIt's a tie!\033[0m")
        print("SCORE: " + ai_name + ": " + str(ai_score) + " | " + player_name + ": " + str(player_score))
        print("############################\n")
        time.sleep(1)
    elif player_move == "paper" and ai_choice == "rock!":
        print("\033[92mYou win!\033[0m")
        player_score += 1
        print("SCORE: " + ai_name + ": " + str(ai_score) + " | " + player_name + ": " + str(player_score))
        print("############################\n")
        time.sleep(1)
    elif player_move == "paper" and ai_choice == "scissors!":
        print("\033[91mYou lose!\033[0m")
        ai_score += 1
        print("SCORE: " + ai_name + ": " + str(ai_score) + " | " + player_name + ": " + str(player_score))
        print("############################\n")
        time.sleep(1)
    elif player_move == "paper" and ai_choice == "paper!":
        print("\033[93mIt's a tie!\033[0m")
        print("SCORE: " + ai_name + ": " + str(ai_score) + " | " + player_name + ": " + str(player_score))
        print("############################\n")
        time.sleep(1)
    else:
        print("\033[91mOops! you made a mistake :-/ try again.\033[0m\n")
        time.sleep(2)
        continue
    
    # Check if either player has won the game | record input to continue or end the game
    if player_score >= 3:
        print("Dang! You beat me :-(")
        print("The final score was: " + player_name + ": " + str(player_score) + " | " + ai_name + ": " + str(ai_score) + "\n")
        time.sleep(2)
        play_again = input("Do you want to play again? (Yes or No)").lower()
        if play_again == "yes":
            # Scores Reset
            player_score = 0
            ai_score = 0
            continue
        else:
            print("OKAY! Come back and play me soon!")
            break
    if ai_score >= 3:
        print("HAHA! I beat you! :-D")
        print("The final score was: " + player_name + ": " + str(player_score) + " | " + ai_name + ": " + str(ai_score) + "\n")
        time.sleep(2)
        play_again = input("Do you want to play again? (Yes or No) ").lower()
        if play_again == "yes":
            # Scores Reset
            player_score = 0
            ai_score = 0
            continue
        else:
            print("\nOKAY! Come back and play me again, soon!\n")
            time.sleep(1)
            print("\033[94m\n /$$$$$$$$ /$$   /$$  /$$$$$$  /$$   /$$ /$$   /$$       /$$     /$$ /$$$$$$  /$$   /$$")
            time.sleep(.1)
            print("|__  $$__/| $$  | $$ /$$__  $$| $$$ | $$| $$  /$$/      |  $$   /$$//$$__  $$| $$  | $$")
            time.sleep(.1)
            print("   | $$   | $$  | $$| $$  \ $$| $$$$| $$| $$ /$$/        \  $$ /$$/| $$  \ $$| $$  | $$")
            time.sleep(.1)
            print("   | $$   | $$$$$$$$| $$$$$$$$| $$ $$ $$| $$$$$/          \  $$$$/ | $$  | $$| $$  | $$")
            time.sleep(.1)
            print("   | $$   | $$__  $$| $$__  $$| $$  $$$$| $$  $$           \  $$/  | $$  | $$| $$  | $$")
            time.sleep(.1)
            print("   | $$   | $$  | $$| $$  | $$| $$\  $$$| $$\  $$           | $$   | $$  | $$| $$  | $$")  
            time.sleep(.1)
            print("   | $$   | $$  | $$| $$  | $$| $$ \  $$| $$ \  $$          | $$   |  $$$$$$/|  $$$$$$/")
            time.sleep(.1)
            print("   |__/   |__/  |__/|__/  |__/|__/  \__/|__/  \__/          |__/    \______/  \______/ ")
            time.sleep(.1)
            print("")
            time.sleep(.1)
            print("")
            time.sleep(.1)
            print("")
            time.sleep(.1)
            print(" /$$$$$$$$ /$$$$$$  /$$$$$$$        /$$$$$$$  /$$        /$$$$$$  /$$     /$$ /$$$$$$ /$$   /$$  /$$$$$$  /$$")
            time.sleep(.1)
            print("| $$_____//$$__  $$| $$__  $$      | $$__  $$| $$       /$$__  $$|  $$   /$$/|_  $$_/| $$$ | $$ /$$__  $$| $$")
            time.sleep(.1)
            print("| $$     | $$  \ $$| $$  \ $$      | $$  \ $$| $$      | $$  \ $$ \  $$ /$$/   | $$  | $$$$| $$| $$  \__/| $$")
            time.sleep(.1)
            print("| $$$$$  | $$  | $$| $$$$$$$/      | $$$$$$$/| $$      | $$$$$$$$  \  $$$$/    | $$  | $$ $$ $$| $$ /$$$$| $$")
            time.sleep(.1)
            print("| $$__/  | $$  | $$| $$__  $$      | $$____/ | $$      | $$__  $$   \  $$/     | $$  | $$  $$$$| $$|_  $$|__/")
            time.sleep(.1)
            print("| $$     | $$  | $$| $$  \ $$      | $$      | $$      | $$  | $$    | $$      | $$  | $$\  $$$| $$  \ $$    ")
            time.sleep(.1)
            print("| $$     |  $$$$$$/| $$  | $$      | $$      | $$$$$$$$| $$  | $$    | $$     /$$$$$$| $$ \  $$|  $$$$$$/ /$$")
            time.sleep(.1)
            print("|__/      \______/ |__/  |__/      |__/      |________/|__/  |__/    |__/    |______/|__/  \__/ \______/ |__/\033[0m")
            time.sleep(.1)
            print("")
            time.sleep(.1)
            print("")
            break