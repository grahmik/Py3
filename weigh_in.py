#!/usr/bin/env python3
#pinkg 4/21/2023

# 🪐. 🌎. 🌍. 🌌. Hello and welcome to the weigh in! 🌕. 🚀. 🛸. ☾. 
# 🌕. 🚀. 🛸. ☾.  This program will make it easy for 🪐. 🌎. 🌍. 🌌.
# 🪐. 🌎. 🌍. 🌌. you to find out what you weigh on  🌕. 🚀. 🛸. ☾.
# 🌕. 🚀. 🛸. ☾.  some of the other planets in our   🪐. 🌎. 🌍. 🌌.
# 🪐. 🌎. 🌍. 🌌.          solar system.             🌕. 🚀. 🛸. ☾.
#
#
#
#
#
#
# Module Imports 
import time

# Introduction
print("\nHello Codey! I hear you have been training hard to compete in the Interplanetary Boxing League (IBL)")
time.sleep(3)
print("You will need to make weight on all of the planets to compete, just like here on Earth.")
time.sleep(3)
print("Luckily, I know the gravitational force of each planet and can tell you what you will weigh when you arrive to your matches.\n")
time.sleep(3)
while True:
    print("Hmmm.", end="\r")
    time.sleep(1)
    print("Hmmm..", end="\r")
    time.sleep(1)
    print("Hmmm...", end="\r")
    time.sleep(1)
    break

# Planet information
print("I have information for the following planets:\n")

print("   1. Venus   2. Mars    3. Jupiter")
print("   4. Saturn  5. Uranus  6. Neptune")
print("   7. Mercury\n")
time.sleep(5)

# Codey Information
codey_wt = float(input("Codey, how much do you currently weigh on Earth?\n"))
time.sleep(0.5)
while True:
    print("Hmmm.", end="\r")
    time.sleep(1)
    print("Hmmm..", end="\r")
    time.sleep(1)
    print("Hmmm...", end="\r")
    time.sleep(1)
    break

# Planet Index
while True:
    planet = float(input("\nOKAY! What planet are you training for? (1-7)\n"))
    time.sleep(0.5)
    while True:
        print("Hmmm.", end="\r")
        time.sleep(1)
        print("Hmmm..", end="\r")
        time.sleep(1)
        print("Hmmm...", end="\r")
        time.sleep(1)
        break

    venus = 1
    venus_rg = .91
    venus_wt = codey_wt * venus_rg

    mars = 2
    mars_rg = .38
    mars_wt = codey_wt * mars_rg

    jupiter = 3
    jupiter_rg = 2.34
    jupiter_wt = codey_wt * jupiter_rg

    saturn = 4
    saturn_rg = 1.06
    saturn_wt = codey_wt * saturn_rg

    uranus = 5
    uranus_rg = .92
    uranus_wt = codey_wt * uranus_rg

    neptune = 6
    neptune_rg = 1.19
    neptune_wt = codey_wt * neptune_rg

    mercury = 7
    mercury_rg = 0.38
    mercury_wt = codey_wt * mercury_rg

# Weight Calculations:
    if planet == 1:
        print("Codey, on this planet, you will weigh " + str(venus_wt) + " lbs!\n")
    elif planet == 2:
        print("Codey, on this planet, you will weigh " + str(mars_wt) + " lbs!\n")
    elif planet == 3:
        print("Codey, on this planet, you will weigh " + str(jupiter_wt) + " lbs!\n")
    elif planet == 4:
        print("Codey, on this planet, you will weigh " + str(saturn_wt) + " lbs!\n")
    elif planet == 5:
        print("Codey, on this planet, you will weigh " + str(uranus_wt) + " lbs!\n")
    elif planet == 6:
        print("Codey, on this planet, you will weigh " + str(neptune_wt) + " lbs!\n")
    elif planet == 7:
        print("Codey, on this planet, you will weigh " + str(mercury_wt) + " lbs!\n")
    else:
        print("\033[31mInvalid Option. Try again.\033[0m")
    time.sleep(3)
    answer = input("Do you want to see what you will weigh on another planet? (yes or no): ")
    if answer != "yes": #Loops back to planet question or ends program
        time.sleep(0.5)
        print("Alright! Now get out there and win one for Earth!")
        time.sleep(1)
        print("Goodbye.")
        break

    




