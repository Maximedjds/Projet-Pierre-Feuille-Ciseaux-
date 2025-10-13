from src.game_directory.game import *
from src.state import var
from src.start.begining import begining

def start():
    var.in_game = True
    begining()
    game_loop()

if __name__ == '__main__':
    start()
