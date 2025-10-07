from src.state import var
import random
import time
from colorama import Fore, Style, init

# Reset Colours
init(autoreset=True)

# Possible options
options = ["Pierre","Feuille","Ciseaux"]

# Starts the main game loop
def game_loop():
    while var.in_game:
        player = player_choice()  # Get player's choice as a string
        if player == "stop":  # Stop the game if the player decides to quit
            print(Fore.YELLOW + "\nAu revoir 👋")
            break
        time.sleep(1.5)  # Pause for better readability
        print(Fore.CYAN + "Au tour de l'ordinateur !")
        time.sleep(1.5)
        computer = computer_choice()  # Get computer's choice as a string
        time.sleep(1)
        winner = fight(player, computer)  # Determine the round winner
        if winner == "Tie":  # Draw
            print(Fore.YELLOW + "Égalité, personne ne gagne cette manche !\n")
        else:
            color = Fore.GREEN if "Vous" in winner else Fore.RED
            print(color + f"{winner} gagné la manche !\n")  # Announce round winner
        time.sleep(1.5)
        print(Fore.MAGENTA + f"Le score est dorénavant:\n{var.score['Player']} - {var.score['Computer']}\n")  # Display the updated score
        get_winner()  # Check if someone has won the game
        time.sleep(1.5)

# Get the player's choice
def player_choice() -> str:
    print(Fore.CYAN + "À votre tour ! (Tapez 'stop' pour arrêter la partie)")
    choice = input(Fore.BLUE + "1. Pierre\n2. Feuille\n3. Ciseaux\nVotre choix: ")  # Get player's input
    if choice.lower() == "stop":  # If the player wants to stop the game
        return choice.lower()
    choice = int(choice)
    if choice > 3 or choice < 1:  # Check if input is between 1 and 3
        print(Fore.RED + "Valeur entrée incorrecte !\n")
        time.sleep(1)
        return player_choice()  # Retry if input is invalid
    choice -= 1
    print(Fore.GREEN + f"Vous avez choisi {options[choice]} !\n")
    return options[choice]  # Return player's choice as a string (based on 'options' list)

# Generate the computer's choice
def computer_choice() -> str:
    random.seed()  # Generate a new seed for true randomness
    choice_index = random.randint(0, 2)
    print(Fore.YELLOW + f"L'ordinateur a choisi {options[choice_index]} !\n")
    return options[choice_index]  # Return computer's random choice

# Determine the winner of the round
def fight(player, computer):
    previous_score = var.score['Player']  # Get player's score before the round
    winner = "L\'Ordinateur a"  # Default winner is the computer
    if player == "Pierre" and computer == "Feuille":
        var.score["Computer"] += 1
    elif player == "Pierre" and computer == "Ciseaux":
        var.score["Player"] += 1
    elif player == "Feuille" and computer == "Ciseaux":
        var.score["Computer"] += 1
    elif player == "Feuille" and computer == "Pierre":
        var.score["Player"] += 1
    elif player == "Ciseaux" and computer == "Feuille":
        var.score["Player"] += 1
    elif player == "Ciseaux" and computer == "Pierre":
        var.score["Computer"] += 1
    else:
        return "Tie"  # Draw
    if previous_score != var.score["Player"]:  # If player's score has changed, they won the round
        winner = "Vous avez"
    return winner  # Return the round winner

# Check if someone has won the match
def get_winner():
    if var.score['Player'] == 2:  # Player victory
        print(Fore.GREEN + Style.BRIGHT + """  
  _   _                                                                        _                          _   _        _ 
 | | | |                                                                      | |                        | | (_)      | |
 | | | | ___  _   _ ___    __ ___   _____ ____   __ _  __ _  __ _ _ __   ___  | | __ _   _ __   __ _ _ __| |_ _  ___  | |
 | | | |/ _ \| | | / __|  / _` \ \ / / _ \_  /  / _` |/ _` |/ _` | '_ \ / _ \ | |/ _` | | '_ \ / _` | '__| __| |/ _ \ | |
 \ \_/ / (_) | |_| \__ \ | (_| |\ V /  __// /  | (_| | (_| | (_| | | | |  __/ | | (_| | | |_) | (_| | |  | |_| |  __/ |_|
  \___/ \___/ \__,_|___/  \__,_| \_/ \___/___|  \__, |\__,_|\__, |_| |_|\___| |_|\__,_| | .__/ \__,_|_|   \__|_|\___| (_)
                                                 __/ |       __/ |                      | |                              
                                                |___/       |___/                       |_|                              \n""")
        restart()
    elif var.score['Computer'] == 2:  # Computer victory
        print(Fore.RED + Style.BRIGHT + """  
 _____      __        _                  
|  _  \    / _|    (_) |                 
| | | |___| |_ __ _ _| |_ ___        
| | | / _ \  _/ _` | | __/ _ \      
| |/ /  __/ || (_| | | ||  __/ _ _ _ 
|___/ \___|_| \__,_|_|\__\___|(_|_|_)
                                         
                                          \n""")
        restart()

# Restart prompt (yes or no)
def restart():
    choice = input(Fore.CYAN + "Voulez-vous rejouer ? (y/n)\n").lower()
    if choice == "n":
        print(Fore.YELLOW + """  
          ___     _     _            _        _   
         / _ \   | |   (_)          | |      | |  
        / /_\ \  | |__  _  ___ _ __ | |_ ___ | |_ 
        |  _  |  | '_ \| |/ _ \ '_ \| __/ _ \| __|
        | | | |  | |_) | |  __/ | | | || (_) | |_       
        \_| |_/  |_.__/|_|\___|_| |_|\__\___/ \__|
                                                  """) # Goodbye Message
        var.in_game = False
    else:  # Player wants to continue (reset scores)
        var.score["Computer"] = 0
        var.score["Player"] = 0
