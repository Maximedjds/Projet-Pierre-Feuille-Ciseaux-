import pygame
from src.state.var import *


class Button:
    def __init__(self, text, x, y, width, height,
                 inactive_color, active_color, base_color,
                 font, image=None, action=None, radius=12,
                 click_sound=None):
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
        self.radius = radius
        self.click_sound = click_sound

        # Disable the text if has image
        if self.image is not None:
            self.text = None

        # Center the button if x coordinate is None
        if self.x is None and self.width is not None:
            self.x = (window[0] / 2) - (self.width / 2)


    def draw(self, screen):
        """Draw the button on the screen."""
        # Ignore if it has image
        if self.image is not None:
            return
        surface = self.font.render(self.text, True, self.base_color)
        rect = surface.get_rect(center=((self.x + self.width / 2), (self.y + self.height / 2)))
        screen.blit(surface, rect)

    def check_input(self, screen, events):
        """Manage mouse interaction with buttons (Hover/Click)."""
        mouse = pygame.mouse.get_pos()
        hovered = self.x + self.width > mouse[0] > self.x and self.y + self.height > mouse[1] > self.y

        if self.image is not None:
            if hovered:
                img = pygame.transform.smoothscale(
                    pygame.image.load(self.image),
                    (int(self.width * 1.1), int(self.height * 1.1))
                )
                screen.blit(img, (self.x - (self.width * 0.1) / 2, self.y - (self.height * 0.1) / 2))
            else:
                img = pygame.transform.smoothscale(pygame.image.load(self.image), (self.width, self.height))
                screen.blit(img, (self.x, self.y))
        else:
            color = self.active_color if hovered else self.inactive_color
            pygame.draw.rect(screen, color, (self.x, self.y, self.width, self.height), border_radius=self.radius)
            pygame.draw.rect(screen, (0, 0, 0), (self.x, self.y, self.width, self.height),
                             width=2, border_radius=self.radius)
            self.draw(screen)
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if hovered and self.action is not None:
                    if self.click_sound:
                        self.click_sound.play()
                    self.action()
