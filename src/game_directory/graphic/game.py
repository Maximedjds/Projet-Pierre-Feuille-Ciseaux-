# Imports
import time

import pygame
import os
import ctypes

from src.game_directory.graphic.button import Button
from src.state.var import *
from src.game_directory.game import *

# Colours
GOLD = (255, 215, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 128, 255)
DARK_BLUE = (0, 90, 200)
BLACK = (0, 0, 0)
ORANGE = (255, 165, 0)
DARK_ORANGE = (255, 122, 0)

# Images
rock_img = os.path.join("assets/images", "rock.png")
paper_img = os.path.join("assets/images", "paper.png")
scissors_img = os.path.join("assets/images", "scissors.png")

# Game Data
player_choice = []

def start_game():
    """Initialise the game and start the game."""

    pygame.init()

    # Sound Init
    pygame.mixer.init()

    global default_font, title_font, screen, CLICK_SOUND

    # Load Sound
    CLICK_SOUND = pygame.mixer.Sound(os.path.join("assets", "son", "mixkit-arcade-game-jump-coin-216.wav"))
    CLICK_SOUND.set_volume(0.5)

    # Load Musique
    pygame.mixer.music.load(os.path.join("assets", "son", "mixkit-tech-house-vibes-130.mp3"))  # <-- change le chemin ici
    pygame.mixer.music.set_volume(0.1)
    pygame.mixer.music.play(-1)  # boucle infinie

    ## Initialize Game

    #Set Icon
    icon = pygame.image.load(os.path.join("assets/images", "icon.png"))
    pygame.display.set_icon(icon)

    # Screen Size
    screen = pygame.display.set_mode((window[0], window[1]))

    # Caption
    pygame.display.set_caption("Pierre-Feuille-Ciseaux (Deluxe Edition)")

    # Fonts
    default_font = pygame.font.Font(os.path.join("assets/fonts", "NFPixels-Regular.ttf"), 50)
    title_font = pygame.font.Font(os.path.join("assets/fonts", "NFPixels-Regular.ttf"), 100)

    # Focus Game Window
    ctypes.windll.user32.SetForegroundWindow(pygame.display.get_wm_info()['window'])

    MAIN_MENU()

def MAIN_MENU():
    """Create and manage game main menu."""
    global default_font, title_font, screen, CLICK_SOUND

    score['Player'], score['Computer'] = 0, 0


    # Create Buttons
    PLAY = Button("Lancer une partie", None, 300, 400, 75,
                  ORANGE, DARK_ORANGE, WHITE, default_font,
                  None, GAME_SCREEN, click_sound=CLICK_SOUND)

    QUIT = Button("Quitter", None, 400, 400, 75,
                  ORANGE, DARK_ORANGE, WHITE, default_font,
                  None, quit_game, click_sound=CLICK_SOUND)

    while True:
        # Clear Window
        screen.fill(BLACK)

        # Set Background
        bg = pygame.image.load(os.path.join("assets/images", "bg.png"))
        bg = pygame.transform.scale(bg, (window[0], window[1]))
        screen.blit(bg, (0, 0))

        # Game Tile
        title = title_font.render("Pierre-Feuille-Ciseaux", True, GOLD)
        screen.blit(title, ((window[0]/2) - (title.get_width()/2), 100))

        # Quit Input (X)
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        # Update Buttons
        for button in [PLAY, QUIT]:
            button.check_input(screen, events)

        pygame.display.flip()


# GAME SCREEN
def GAME_SCREEN():
    """Create and manage the game screen"""
    global default_font, title_font, screen, player_choice


    # Reset scores if previous game end
    if score['Player'] == 2 or score['Computer'] == 2:
        score['Player'], score['Computer'] = 0, 0

    while True:
        # Clear Window
        screen.fill(BLACK)

        # Set background
        bg = pygame.image.load(os.path.join("assets/images", "bg_game.png"))
        bg = pygame.transform.scale(bg, (window[0], window[1]))
        screen.blit(bg, (0, 0))

        # Screen Title
        title = title_font.render("Choisissez votre arme:", True, GOLD)
        screen.blit(title, ((window[0]/2) - (title.get_width()/2), 100))
        player_choice = []

        # Create Buttons
        ROCK = Button(None, 300, 300, 200, 250,
                      None, None, None, None,
                      rock_img, lambda: player_select("Pierre"), click_sound=CLICK_SOUND)
        PAPER = Button(None, None, 300, 200, 250,
                       None, None, None, None,
                       paper_img, lambda: player_select("Feuille"), click_sound=CLICK_SOUND)
        SCISSORS = Button(None, 775, 300, 200, 250,
                          None, None, None, None,
                          scissors_img, lambda: player_select("Ciseaux"), click_sound=CLICK_SOUND)
        RETURN = Button("Retour", 50, 620, 200, 60,
                        ORANGE, DARK_ORANGE, WHITE,
                        default_font, None, MAIN_MENU, click_sound=CLICK_SOUND)

        # Quit Events
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                quit_game()

        # Update Buttons
        for button in [ROCK, PAPER, SCISSORS, RETURN]:
            button.check_input(screen, events)

        pygame.display.flip()


def player_select(choice):
    """Send the player choice to the Fight manager"""
    player_choice.append(choice)
    FIGHT_SCREEN()
    player_choice.pop(0)



def FIGHT_SCREEN():
    """Fight screen display and management."""
    global default_font, title_font, screen, player_choice, CONTINUE, CLICK_SOUND

    # Generate 
    computer_choice = random.choice(options)
    result = fight(player_choice[0], computer_choice)

    countdown_value = -1


    while True:
        # Clear window
        screen.fill(BLACK)

        # Background
        bg = pygame.image.load(os.path.join("assets/images", "bg_game.png"))
        bg = pygame.transform.scale(bg, (window[0], window[1]))
        screen.blit(bg, (0, 0))

        CONTINUE = None

        # Countdown
        if countdown_value < 2:
            countdown_value += 1
            countdown = title_font.render(f'{options[countdown_value]} !', True, WHITE)
            screen.blit(countdown, ((window[0]/2) - (countdown.get_width()/2), 135))

        if countdown_value < 2:
            # Show Hands
            player_hand = pygame.image.load(os.path.join("assets/images/player", "Pierre.png"))
            player_hand = pygame.transform.scale(player_hand,(player_hand.get_width() * 2, player_hand.get_height() * 2))
            screen.blit(player_hand, (0, 250))

            computer_hand = pygame.image.load(os.path.join("assets/images/computer", "Pierre.png"))
            computer_hand = pygame.transform.scale(computer_hand,(computer_hand.get_width() * 2, computer_hand.get_height() * 2))
            screen.blit(computer_hand, (window[0] - computer_hand.get_width(), 240))
        else:
            player_hand = pygame.image.load(os.path.join("assets/images/player", f"{player_choice[0]}.png"))
            player_hand = pygame.transform.scale(player_hand,(player_hand.get_width() * 2, player_hand.get_height() * 2))
            screen.blit(player_hand, (0, 255))

            computer_hand = pygame.image.load(os.path.join("assets/images/computer", f"{computer_choice}.png"))
            computer_hand = pygame.transform.scale(computer_hand,(computer_hand.get_width() * 2, computer_hand.get_height() * 2))
            screen.blit(computer_hand, (window[0] - computer_hand.get_width(), 235))

            # Display Result
            if result == "Tie":
                result_text = title_font.render("Égalité!", True, GOLD)
            else:
                result_text = title_font.render(f"{result} gagné le round!", True, GOLD)
            screen.blit(result_text, ((window[0] / 2) - (result_text.get_width() / 2), 25))

            # Show Score
            game_score = default_font.render(f"Score: {score['Player']} - {score['Computer']}", True, WHITE)
            screen.blit(game_score, ((window[0] / 2) - (game_score.get_width() / 2), 575))

            # Continue Button
            CONTINUE = Button(
                "Continuer", window[0] - 265, 625, 250, 60,
                ORANGE, DARK_ORANGE, WHITE,
                default_font, None, GAME_SCREEN,
                click_sound=CLICK_SOUND
            )

            # Get Winner
            if score['Player'] == 2:
                end_text = title_font.render("Victoire !", True, GREEN)
                screen.blit(end_text, ((window[0]/2)-(end_text.get_width()/2), 300))
            elif score['Computer'] == 2:
                end_text = title_font.render("Défaite !", True, RED)
                screen.blit(end_text, ((window[0]/2)-(end_text.get_width()/2), 300))

        # Quit Event
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                quit_game()
                return

        # Update Button if existing
        if CONTINUE is not None:
            CONTINUE.check_input(screen, events)
            CONTINUE.draw(screen)

        pygame.display.flip()

        # Timer
        if countdown_value <= 2:
            time.sleep(1)
            if countdown_value == 2:
                countdown_value += 1

def quit_game():
    """Close the game proprely"""
    pygame.quit()
    exit()