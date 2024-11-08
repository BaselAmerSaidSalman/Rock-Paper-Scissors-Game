import random

# Rock, Paper, Scissors Ascii Arts
rock = """
███████████████████████████████████
███████████████████████████████████
███████████████████████████████████
███████████────███──────███████████
██████████─────███───────██████████
█████████───██████───────██████████
██████████████───██───────█████████
██████████────────█──────██████████
███████───────────█──────██████████
█████─────────────█─────█────██████
████──────────────█────██────██████
████─────────────██────█──────█████
████────────────██─────█─────██████
████──────────███──────█─────██████
███───────██████──────██─────██─███
███───────██████──────█─────██───██
███────────█████─────██─────██───██
███──────────███─────██─────█────██
███───────────██──████─────██───███
███────────────██──███─────██───███
███─────────────██████─────█────███
████────────────██████─────█────███
█████────────────██████───██────███
██████───────────█──████████───████
██████───────────────███─██████████
███████───────────────────█████████
████████─────────────────────██████
█████████────────────────────██████
█████████───────────────────███████
██████████─────────────────████████
██████████────────────────█████████
██████████──────────────███████████
██████████─────────────████████████
██████████─────────────████████████
██████████─────────────████████████
██████████─────────────████████████
██████████─────────────████████████
██████████─────────────████████████
██████████─────────────████████████
██████████─────────────████████████"""
paper = """ 
▐▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▌
▐─────────────────────────▄▄─────────▌
▐────────────────────────███─▄▄──────▌
▐─────────▄▄────────────████─██──────▌
▐────────▐██▌──────────████▌██─▄▄────▌
▐────────███▌─────────████▌███▐██────▌
▐────────████─────────███▌▐██▌▐██────▌
▐────────████────────████▌███▐███────▌
▐────────████───────████▌▐██▌▐██▌────▌
▐────────█████▄────█████▌███▐██▌─██──▌
▐────────██████───█████▌███▌▐██▌███──▌
▐───────▐███████──████▌▐███▐██▌─██▌──▌
▐───────████████▌█████▌███▐███─███▌──▌
▐───────█████████████▌███▌▐██─███▌───▌
▐───────████████████▌▐███▐███─██▌────▌
▐───────████████████▌███▌▐██▌███▌█▌──▌
▐───────███████████▌████▐██▌─██▌███──▌
▐──────▐██████████▌▐███████▌███▌███──▌
▐──────███████████████████▌─██▌███▌──▌
▐──────███████████████████▌██▌─██▌───▌
▐──────██████████████████▌─██▌███────▌
▐──────█████████████████████▌─██▌────▌
▐──────█████████████████████▌███─────▌
▐──────████████████████████▌─██▌─────▌
▐──────▐███████████████████████──────▌
▐───────██████████████████████▌──────▌
▐───────██████████████████████───────▌
▐───────█████████████████████▌───────▌
▐──────▐█████████████████████────────▌
▐──────█████████████████████▌────────▌
▐─────▐█████████████████████─────────▌
▐─────█████████████████████▌─────────▌
▐───▐█████████████████████▌──────────▌
▐──▐██████████████████████───────────▌
▐──██████████████████████▌───────────▌
▐──█████████████████████▌────────────▌
▐──████████████████████▌─────────────▌
▐──▐█████████████████▌───────────────▌
▐───▐███████████████▌────────────────▌
▐────▐█████████████▌─────────────────▌
▐────────────────────────────────────▌
▐▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▌"""
scissors = """ 
888888888888888888888888888888888
88888888888888888____88888____888
8888888888888888______888_____888
8888888888888888______888_____888
8888888888888888______888_____888
8888888888888888______88_____8888
8888888888888888______88_____8888
8888888888888888______88_____8888
8888888888_____8______88_____8888
8888___88______8______8_____88888
888_____8______8______8_____88888
888_____8______8______8_____88888
888_____8______8______8_____88888
888_____8____88888888888888888888
8_8_____8___88________________888
8_8_____8__88__________________88
8__888888_888_________888_______8
8_________88________8___________8
8____________8888888____________8
88_____________88_______________8
88_______________88_____________8
888______________8_____________88
888_______________8___________888
88888_____________8__________8888
888888_____________________888888
888888____________________8888888"""


# Game Rules
print("Welcome to the Rock, Paper, Scissors game!")
rules = input("Press Enter to continue or type (Help) for the rules: ").lower()
while rules != "help" and rules != "": 
  print("Sorry, Invalid input")
  rules = input("Press Enter to continue or type (Help) for the rules: ").lower()
if rules == "help":
  print("""\n********* RULES *********
  1) You choose and the computer chooses
  2) Rock smashes Scissors -> Rock wins
  3) Scissors cut Paper -> Scissors win
  4) Paper covers Rock -> Paper wins""")


# User_choice
user_choice = input("Please enter your choice (Rock, Paper, Scissors):").lower()
while user_choice != "rock" and user_choice != "paper" and user_choice != "scissors":
    print("Sorry, Invalid choice")
    user_choice = input("Please enter your choice (Rock, Paper, Scissors): ").lower()
if user_choice == "rock":
  print(f"\nYou chose:\n{rock}")
elif user_choice == "paper":
  print(f"\nYou chose:\n{paper}")
elif user_choice == "scissors":
  print(f"\nYou chose:\n{scissors}")


# Computer_choice
computer_choice = random.choice(["rock", "paper", "scissors"])
if computer_choice == "rock":
  print(f"\nComputer chose:\n{rock}")
elif computer_choice == "paper":
  print(f"\nComputer chose:\n{paper}")
elif computer_choice == "scissors":
  print(f"\nComputer chose:\n{scissors}")


# Game logic
# Tie
if user_choice == computer_choice:
  print("It's a tie!")
# User wins
elif user_choice == "rock" and computer_choice == "scissors"                        or user_choice == "paper" and computer_choice == "rock"                            or user_choice == "scissors" and computer_choice == "paper":
  print(f"\nYou win! {user_choice} beats {computer_choice}")
# Computer wins
elif user_choice == "rock" and computer_choice == "paper"                           or user_choice == "paper" and computer_choice == "scissors"                        or user_choice == "scissors" and computer_choice == "rock":
  print(f"\nYou lose! {computer_choice} beats {user_choice}")



