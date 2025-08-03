# Import Required Modules 
import sys 
import os 
import time 

# Defining Required Functions 
def animation_text(text, delay):
    for i in text:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(delay)

def clear():
    os.system("clear")

# Logo Section
logo = """

\033[1;34m================================================

 \t\033[1;36m _____  _____ ________      _______  
 \t|  __ \\|_   _|___  /\\ \\    / /_   _| 
 \t| |__) | | |    / /  \\ \\  / /  | |   
 \t|  _  /  | |   / /    \\ \\/ /   | |   
 \t| | \\ \\ _| |_ / /__    \\  /   _| |_  
 \t|_|  \\_\\_____/_____|    \\/   |_____| 


       \033[1;32mAuthor   : Rizvi Ahmed
       Facebook : www.facebook.com/rijuorsiam 
       Github   : www.github.com/ahmedrizvisiam
       Group    : STLP TEAM

       Use the tool for Educational Purpose

\033[1;34m================================================\033[0m
"""

# Main Program
clear()
animation_text(logo, 0.01)

option = "\n\n\t\033[1;35m1. Setup Termux\n\n\t2. Exit\n\033[0m"
print(option)

choise = input("\n\n\tEnter your choice: ")

if choise == "1":
    os.system("pkg update -y")
    os.system("pkg upgrade -y")
    os.system("pkg install git -y")
    os.system("pkg install python -y")
    os.system("pkg install python2 -y")
    os.system("pkg install ruby -y")
    os.system("pkg install wget -y")
    os.system("pkg install pip -y")
    os.system("pip install requests")
    os.system("pip2 install requests")
    os.system("pkg install php -y")
    os.system("pkg install bash -y")
    os.system("pip install future")
    os.system("pkg install openssh -y")
    os.system("pkg install curl -y")
    os.system("pip install requirements")
    os.system("pip2 install requirements")
    os.system("termux-setup-storage")

    clear()
    animation_text(logo, 0.01)
    success = ("\n\n\n\t\033[1;32mSetup Successfully Completed ✅\033[0m\n\n")
    animation_text(success,0.05)

elif choise == "2":
    print("\n\n\t\033[1;31mThanks for using the tool. Exiting...\033[0m\n")
    time.sleep(1)

else:
    print("\n\n\t\033[1;31mWrong input! Please enter a valid choice (1 or 2).\033[0m\n")
