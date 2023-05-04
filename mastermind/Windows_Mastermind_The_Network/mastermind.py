# Mike G 5/3/2023

# Imports

import random
import time
import pygame
from ASCii import win
from ASCii import welcome
from ASCii import lose

# Initialize pygame

pygame.mixer.init()

# Load sound files

welcome_sound = pygame.mixer.Sound('./sounds/intro2.mp3')
input_sound = pygame.mixer.Sound('./sounds/input.mp3')
win_sound = pygame.mixer.Sound('./sounds/win.mp3')
negative_sound = pygame.mixer.Sound('./sounds/negative.mp3')
bye_sound = pygame.mixer.Sound('./sounds/bye.mp3')

# Welcome to MASTERMIND

welcome_sound.play()
welcome()
time.sleep(1)

# Mastermind Lists:

mm_list = ["router", "server", "firewall", "load balancer", "internet", "client", "vpn", 
           "wireless router", "switch"]

mm_solved = random.sample(list(set(mm_list)), 4)

TRIES = 10



#################### Game Loop ####################

while True:
    
    print(
        "\n\033[34m\033[1mChoose 4 Networking terms:\033[0m\n\n", 
        mm_list, 
        f"\n\n\033[34m\033[1mGuess all 4 in the correct order. You have {TRIES} tries.\033[0m"
    )
    
    # User solve list
    u_solve = []
    
    u_input1 = input("\nChoose term 1: ").lower()
    input_sound.play()
    u_input2 = input("Choose term 2: ").lower()
    input_sound.play()
    u_input3 = input("Choose term 3: ").lower()
    input_sound.play()
    u_input4 = input("Choose term 4: ").lower()
    input_sound.play()
    
    u_solve.extend([u_input1, u_input2, u_input3, u_input4])  
    
    # Win condition
    if u_solve == mm_solved:
        win_sound.play()
        print("\nCongratulations! You win!")
        win()
        
        # Does the player want to play again
        play_again = input("\nWould you like to play Mastermind again? (Y/N): ").lower()
        input_sound.play()
        
    
        while True:
            
            if play_again == "y":
                mm_solved = random.sample(list(set(mm_list)), 4)
                break
            
            elif play_again == "n":
                print("\nGoodbye!")
                bye_sound.play()
                pygame.time.wait(int(bye_sound.get_length() * 1000))
                quit()
                
            else:
                negative_sound.play()
                print("\033[31mPlease enter a valid option\033[0m")
                continue
            
        continue
        
    elif u_solve != mm_solved:
        # Create copies of the lists to avoid modifying the originals
        temp_mm = list(mm_solved)
        temp_u = list(u_solve)
        
        # Initialize counters for matches and mismatches
        matches = 0
        total_matches = 0
        
        # Check for matches in the correct position
        for i in range(len(temp_mm)):
            if temp_mm[i] == temp_u[i]:
                matches += 1
                # mark the matches as already counted
                temp_mm[i] = None
                temp_u[i] = None
    
        # Check for total matches
        for i in range(len(temp_mm)):
            if temp_u[i] in temp_mm:
                total_matches += 1
                # Mark the matches as already counted
                temp_mm[temp_mm.index(temp_u[i])] = None
                temp_u[i] = None

        print(
            "\033[32mYou have\033[0m", 
            matches, 
            "\033[32min the correct order | You have\033[0m", 
            total_matches - matches, 
            "\033[32mcorrect, but in the wrong order\033[0m"
        )
        
    
    # Asks if the user wants to continue and continues or quits
    while True:
        
        keep_going = input("\nWould you like to keep going? (Y/N): ").lower()
        input_sound.play()
        
        if keep_going == "y":
            
            TRIES -= 1
            
            if TRIES == 0:
                
                print("\nYou lose!")
                bye_sound.play()
                lose()
                time.sleep(1)
                quit()
                
            break
        
        elif keep_going == "n":
            
            print("\nThanks for playing! Goodbye.")
            bye_sound.play()
            pygame.time.wait(int(bye_sound.get_length() * 1000))
            quit()
            
        else:
            negative_sound.play()
            print("\033[31mPlease enter a valid option\033[0m")
            continue
    
    continue  