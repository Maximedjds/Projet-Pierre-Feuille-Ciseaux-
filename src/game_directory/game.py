from src.state import var
import random
import time
from colorama import Fore, Style, init

init(autoreset=True)

options = ["Pierre","Feuille","Ciseaux"]

# Lance la boucle du jeu
def game_loop():
    while var.in_game:
        player = player_choice()
        time.sleep(1)
        print(Fore.CYAN + "Au tour de l'ordinateur !")
        time.sleep(1)
        computer = computer_choice()
        winner = fight(player, computer)
        if winner == "Tie":
            print(Fore.YELLOW + "Égalité, personne ne gagne cette manche !\n")
        else:
            color = Fore.GREEN if "Vous" in winner else Fore.RED
            print(color + f"{winner} gagné la manche !\n")
        time.sleep(1)
        print(Fore.MAGENTA + f"Le score est dorénavant:\n{var.score['Player']} - {var.score['Computer']}\n")
        get_winner()
        time.sleep(1)

# Récupère le choix du joueur
def player_choice() -> str:
    print(Fore.CYAN + "À votre tour !")
    choice = int(input(Fore.BLUE + "1. Pierre\n2. Feuille\n3. Ciseaux\nVotre choix: "))
    if choice > 3 or choice < 1:
        print(Fore.RED + "Valeur entrée incorrecte !\n")
        time.sleep(1)
        return player_choice()
    choice -= 1
    print(Fore.GREEN + f"Vous avez choisi {options[choice]} !\n")
    return options[choice]

# Génère le choix de l'ordinateur
def computer_choice() -> str:
    choice_index = random.randint(0, 2)
    print(Fore.YELLOW + f"L'ordinateur a choisi {options[choice_index]} !\n")
    return options[choice_index]

# Détermine le gagnant du tour
def fight(player, computer):
    previous_score = var.score['Player']
    winner = "L\'Ordinateur a"
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
        return "Tie"
    if previous_score != var.score["Player"]:
        winner = "Vous avez"
    return winner

def get_winner():
    if var.score['Player'] == 2:
        print(Fore.GREEN + Style.BRIGHT + "🎉 Vous avez gagné la partie !\n")
        restart()
    elif var.score['Computer'] == 2:
        print(Fore.RED + Style.BRIGHT + "💻 L'Ordinateur a gagné la partie !\nDommage pour vous (soyez meilleur).\n")
        restart()

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
                                                  """)
        var.in_game = False
    else:
        var.score["Computer"] = 0
        var.score["Player"] = 0
