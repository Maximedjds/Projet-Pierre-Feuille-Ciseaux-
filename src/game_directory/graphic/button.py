import pygame
from src.state.var import *
import time


class Button:
    def __init__(self, text, x, y, width, height, inactive_color, active_color, base_color, font, image, action=None):
        self.text = text
        self.font = font
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.inactive_color = inactive_color
        self.active_color = active_color
        self.base_color = base_color
        self.action = action
        self.image = image
        if self.image is not None:
            self.text = None
        if self.x is None and self.width is not None:
            self.x = (window[0]/2) - (self.width/2)



    def draw(self, screen):
        if self.image is not None:
            return
        surface = self.font.render(self.text, True, self.base_color)
        rect = surface.get_rect(center=((self.x + self.width / 2), (self.y + self.height / 2)))
        screen.blit(surface, rect)

    def check_input(self, screen):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if self.x + self.width > mouse[0] > self.x and self.y + self.height > mouse[1] > self.y:
            if self.image is None:
                pygame.draw.rect(screen, self.active_color, (self.x, self.y, self.width, self.height))
            else:
                img = pygame.transform.smoothscale(pygame.image.load(self.image), (self.width*1.1, self.height*1.1))
                screen.blit(img, (self.x-(self.width*1.1-self.width)//2, self.y-(self.height*1.1-self.height)//2))
            if click[0] == 1 and self.action is not None:
                time.sleep(0.1) 
                self.action()
                
        else:
            if self.image is None:
                pygame.draw.rect(screen, self.inactive_color, (self.x, self.y, self.width, self.height))
            else:
                img = pygame.transform.smoothscale(pygame.image.load(self.image), (self.width, self.height))
                screen.blit(img, (self.x, self.y))
