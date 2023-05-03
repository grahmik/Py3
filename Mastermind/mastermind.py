# Mike G 5/3/2023

# Imports
import random
from ASCii import print_mastermind
from ASCii import you_win


# Welcome to MASTERMIND
print_mastermind()


# Mastermind Lists:
mm_list = ["router", "server", "firewall", "load balancer", "internet", "client", "vpn", 
           "wireless router", "switch"]

mm_solved = random.sample(list(set(mm_list)), 4)



#################### Game Loop ####################
while True:
    
    print(
        "\n\033[34m\033[1mChoose 4 Networking terms:\033[0m\n\n", 
        mm_list, 
        "\n\n\033[34m\033[1mYou have to place the terms in the correct order!\033[0m"
    )
    
    # User solve list
    u_solve = []
    
    u_input1 = input("\nChoose term 1: ").lower()
    u_input2 = input("Choose term 2: ").lower()
    u_input3 = input("Choose term 3: ").lower()
    u_input4 = input("Choose term 4: ").lower()
    
    u_solve.extend([u_input1, u_input2, u_input3, u_input4])  
    
    # Win condition
    if u_solve == mm_solved:
        print("Congratulations! You win!")
        you_win()
        quit()
        
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
        
        if keep_going == "y":   
            break
        elif keep_going == "n":
            print("\nThanks for playing! Goodbye.")
            quit()
        else:
            print("\033[31mPlease enter a valid option\033[0m")
            continue
    
    continue  