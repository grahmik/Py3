#!/bin/python3

# IMPORT
import time

# ASCii VARIABLES
mtn = '''
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# ___  ___  ___   _____ _____ ______________  ________ _   _______  #
# |  \/  | / _ \ /  ___|_   _|  ___| ___ \  \/  |_   _| \ | |  _  \ #
# | .  . |/ /_\  \\ `--.  | | | |__ | |_/ / .  . | | | |  \| | | | | #
# | |\/| ||  _  | `--. \ | | |  __||    /| |\/| | | | | . ` | | | | #
# | |  | || | | |/\__/ / | | | |___| |\ \| |  | |_| |_| |\  | |/ /  #
# \_|  |_/\_| |_/\____/  \_/ \____/\_| \_\_|  |_/\___/\_| \_/___/   #
#  _____ _   _  _____                                               # 
# |_   _| | | ||  ___|                                              #
#   | | | |_| || |__                                                #
#   | | |  _  ||  __|                                               #
#   | | | | | || |___                                               #  
#   \_/ \_| |_/\____/                                               #
#  _   _  _____ _____ _    _  ___________ _   __                    #
# | \ | ||  ___|_   _| |  | ||  _  | ___ \ | / /                    #
# |  \| || |__   | | | |  | || | | | |_/ / |/ /                     #
# | . ` ||  __|  | | | |/\| || | | |    /|    \                     #
# | |\  || |___  | | \  /\  /\ \_/ / |\ \| |\  \                    #
# \_| \_/\____/  \_/  \/  \/  \___/\_| \_\_| \_/by: Mike G          #
#                                                                   #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

'''

you_win = '''
# # # # # # # # # # # # # #
# __   _______ _   _      #
# \ \ / /  _  | | | |     #
#  \ V /| | | | | | |     #
#   \ / | | | | | | |     #
#   | | \ \_/ / |_| |     #
#   \_/  \___/ \___/      #
#                         #
#  _    _ _____ _   _ _   #
# | |  | |_   _| \ | | |  #
# | |  | | | | |  \| | |  #
# | |/\| | | | | . ` | |  #
# \  /\  /_| |_| |\  |_|  #
#  \/  \/ \___/\_| \_(_)  #
# # # # # # # # # # # # # #
'''

# Print functions:
def welcome():
    for line in mtn.splitlines():
        print(line)
        time.sleep(.1)
        
def win():
    for line in you_win.splitlines():
        print(line)
        time.sleep(.1)