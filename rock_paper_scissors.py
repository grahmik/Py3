#!/bin/python3

# Welcome (write welcome message)

# Import modules
import time
import random

# Name variables
ai_name = "Tom"
player_name = (input("What is your name? "))

# Starting game
print("Hello " + player_name + ", My name is " + ai_name + ", and I am an AI designed to play Rock, Paper, Scissors with you!")
ready = (input("Are you ready to play? (Yes or No) ").lower())

if ready == "yes": 
    print("\nOKAY! It's best 3 out of 5!\n")
else:
    print("\nOKAY! See you later!\n")
    time.sleep(.5)
    quit()

# Scores
player_score = 0
ai_score = 0

while True:
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

# GAME:
    
    player_move = (input("Choose Rock, Paper or Scissors: ")).lower()
    ai_list = ["Rock!", "Paper!", "Scissors!"]
    ai_choice = random.choice(ai_list)
    print("I choose " + ai_choice + "\n")

    if player_move == "rock" and ai_choice == "Scissors!":
        print("You win!")
        player_score += 1
        print("SCORE: " + str(ai_name) + ": " + str(ai_score) + " -- " + player_name + ": " + str(player_score))
    elif player_move == "rock" and ai_choice == "Paper!":
        print("I win")
        ai_score += 1
        print("SCORE: " + str(ai_name) + ": " + str(ai_score) + " -- " + player_name + ": " + str(player_score))
    elif player_move == "rock" and ai_choice == "Rock!":
        print("Tie!")
        print("SCORE: " + str(ai_name) + ": " + str(ai_score) + " -- " + player_name + ": " + str(player_score))
    elif player_move == "scissors" and ai_choice == "Paper!":
        print("You win!")
        player_score += 1
        print("SCORE: " + str(ai_name) + ": " + str(ai_score) + " -- " + player_name + ": " + str(player_score))
    elif player_move == "scissors" and ai_choice == "Rock!":
        print("I win")
        ai_score += 1
        print("SCORE: " + str(ai_name) + ": " + str(ai_score) + " -- " + player_name + ": " + str(player_score))
    elif player_move == "scissors" and ai_choice == "Scissors!":
        print("Tie!")
        print("SCORE: " + str(ai_name) + ": " + str(ai_score) + " -- " + player_name + ": " + str(player_score))
    elif player_move == "paper" and ai_choice == "Rock!":
        print("You win!")
        player_score += 1
        print("SCORE: " + str(ai_name) + ": " + str(ai_score) + " -- " + player_name + ": " + str(player_score))
    elif player_move == "paper" and ai_choice == "Scissors!":
        print("I win")
        ai_score += 1
        print("SCORE: " + str(ai_name) + ": " + str(ai_score) + " -- " + player_name + ": " + str(player_score))
    elif player_move == "paper" and ai_choice == "Paper!!":
        print("Tie!")
        print("SCORE: " + str(ai_name) + ": " + str(ai_score) + " -- " + player_name + ": " + str(player_score))
    
    # Check if either player has won the game
    if player_score >= 3 or ai_score >= 3:
        break

# Continue or end game
#if player_score == 3:
   # print(player_name + " wins the game!\n")
#elif ai_score == 3:
    #print(ai_name + " wins the game!\n")

#play_again = (input("Do you want to play again? (Yes or No)")).lower()
#if play_again ==  "yes":
