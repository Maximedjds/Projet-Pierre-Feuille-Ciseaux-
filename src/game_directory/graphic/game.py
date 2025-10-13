# Imports
import pygame
import os

from src.game_directory.graphic.button import Button
from src.state.var import *
from src.game_directory.game import *

# Colours
GOLD = (255, 215, 0)
WHITE = (255, 255, 255)
BLUE = (0, 128, 255)
DARK_BLUE = (0, 90, 200)
BLACK = (0, 0, 0)
ORANGE = (255, 165, 0)
DARK_ORANGE = (255, 122, 0)

# Images
rock_img = os.path.join("assets/images", "rock.png")
paper_img = os.path.join("assets/images", "paper.png")
scissors_img = os.path.join("assets/images", "scissors.png")

def start_game():
    pygame.init()

    global default_font, title_font, screen

    screen = pygame.display.set_mode((window[0], window[1]))
    pygame.display.set_caption("Pierre-Feuille-Ciseaux (Deluxe Edition)")
    default_font = pygame.font.Font(os.path.join("assets/fonts", "NFPixels-Regular.ttf"), 50)
    title_font = pygame.font.Font(os.path.join("assets/fonts", "NFPixels-Regular.ttf"), 100)

    MAIN_MENU()

# Show Main Menu
def MAIN_MENU():
    global default_font, title_font, screen

    # Draw Buttons
    PLAY = Button("Lancer une partie", None, 300, 400, 75, ORANGE, DARK_ORANGE, WHITE, default_font, None, GAME_SCREEN)
    QUIT = Button("Quitter", None, 400, 400, 75, ORANGE, DARK_ORANGE, WHITE, default_font, None, pygame.quit)

    while True:
        screen.fill(BLACK)

        # Background Image
        bg = pygame.image.load(os.path.join("assets/images", "bg.png"))
        bg = pygame.transform.scale(bg, (window[0], window[1]))
        screen.blit(bg, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        # Title
        title = title_font.render("Pierre-Feuille-Ciseaux", True, GOLD)
        screen.blit(title, ((window[0]/2) - (title.get_width()/2), 100))


        for button in [PLAY, QUIT]:
            button.check_input(screen)
            button.draw(screen)

        pygame.display.flip()

# Show Game Screen
def GAME_SCREEN():
    global default_font, title_font, screen

    while True:
        # Reset Screen
        screen.fill(BLACK)

        # Background Image
        bg = pygame.image.load(os.path.join("assets/images", "bg_game.png"))
        bg = pygame.transform.scale(bg, (window[0], window[1]))
        screen.blit(bg, (0, 0))

        # Title
        title = title_font.render("Choisissez votre arme:", True, GOLD)
        screen.blit(title, ((window[0]/2) - (title.get_width()/2), 100))

        # Create Buttons
        ROCK = Button(None, 300, 300, 200, 250, None, None, None, None, rock_img, lambda: player_select("Pierre"))
        PAPER = Button(None, None, 300, 200, 250, None, None, None, None, paper_img, lambda: player_select("Feuille"))
        SCISSORS = Button(None, 775, 300, 200, 250, None, None, None, None, scissors_img, lambda: player_select("Ciseaux"))
        RETURN = Button("Retour", 50, 620, 200,60, ORANGE, DARK_ORANGE, WHITE, default_font, None, MAIN_MENU)

        # Draw Buttons + Events
        for button in [ROCK, PAPER, SCISSORS, RETURN]:
            button.check_input(screen)
            button.draw(screen)

        # Quit Event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        
        pygame.display.flip()

player_choice = []

def player_select(choice):
    player_choice.append(choice)
    if len(player_choice) < 2: # Anti double click
        return
    player_choice.pop(0)
    print(player_choice[0])
    FIGHT_SCREEN()

def FIGHT_SCREEN():
    global default_font, title_font, screen, player_choice

    computer_choice = random.choice(options)
    result = fight(player_choice[0], computer_choice)

    while True:
        # Reset Screen
        screen.fill(BLACK)

        # Background Image
        bg = pygame.image.load(os.path.join("assets/images", "bg_game.png"))
        bg = pygame.transform.scale(bg, (window[0], window[1]))
        screen.blit(bg, (0, 0))

        # Title
        title = title_font.render("Résultat du combat:", True, GOLD)
        screen.blit(title, ((window[0]/2) - (title.get_width()/2), 100))

        # Display Choices
        player_text = default_font.render(f"Vous avez choisi: {player_choice[0]}", True, WHITE)
        computer_text = default_font.render(f"L'ordinateur a choisi: {computer_choice}", True, WHITE)
        screen.blit(player_text, (200, 300))
        screen.blit(computer_text, (200, 400))

        # Display Result
        if result == "Tie":
            result_text = default_font.render("Égalité!", True, WHITE)
        else:
            result_text = default_font.render(f"{result} gagné le round!", True, WHITE)
        screen.blit(result_text, ((window[0]/2) - (result_text.get_width()/2), 500))

        # Continue Button
        CONTINUE = Button("Continuer", None, 600, 250, 60, ORANGE, DARK_ORANGE, WHITE, default_font, None, GAME_SCREEN)
        CONTINUE.check_input(screen)
        CONTINUE.draw(screen)

        # Quit Event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        
        pygame.display.flip()

# Start Game (Remove Later)
start_game()