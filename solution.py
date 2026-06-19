import random
# Topic 04 Collaborative Assignment
# Your Name: Bradley Moore
# Date: 18 June, 2026

# --- STARTER CODE ---
# This starter program checks if a temperature is hot, warm, or cold.
# Extend it, change the theme, or use it as inspiration for your own idea.

#temp_input = input("Enter a temperature in Fahrenheit: ")
#temperature = float(temp_input)

#if temperature >= 90:
#    print("It is hot outside.")
#elif temperature >= 60:
#    print("It is warm outside.")
#else:
#   print("It is cold outside.")

# --- YOUR EXTENSION BELOW THIS LINE ---
# Ideas: Add more conditions, change the topic entirely,
# or add a second input and a second set of branches.

# Rock, Paper, Scissors Game
user_hand = input('Type "Rock" "Paper" or "Scissors":\n')
options = ("Rock", "Paper", "Scissors")

comp_hand = random.choice(options)

print(f"\n\nYou chose {user_hand}. Comuter chose {comp_hand}.\n")

#You chose Rock
if user_hand == "Rock":
    if comp_hand == "Paper":
        print(f"{comp_hand} beats {user_hand}. Computer wins!\n\n")
    elif comp_hand == "Scissors":
        print(f"{user_hand} beats {comp_hand}. User wins!\n\n")
    else:
        print("It's a tie!\n\n")

#You chose Paper
if user_hand == "Paper":
    if comp_hand == "Scissors":
        print(f"{comp_hand} beats {user_hand}. Computer wins!\n\n")
    elif comp_hand == "Rock":
        print(f"{user_hand} beats {comp_hand}. User wins!\n\n")
    else:
        print("It's a tie!\n\n")

#You chose Scissors
if user_hand == "Scissors":
    if comp_hand == "Rock":
        print(f"{comp_hand} beats {user_hand}. Computer wins!\n\n")
    elif comp_hand == "Paper":
        print(f"{user_hand} beats {comp_hand}. User wins!\n\n")
    else:
        print("It's a tie!\n\n")
