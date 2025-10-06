from src.game_directory.game import *
from src.state import var


def start():
    var.in_game = True
    game_loop()

if __name__ == '__main__':
    start()
