import pygame
import sys
from Ship import Ship
from Settings import Settings
import Check_events as gf


def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    ship = Ship(screen)
       
    screen.fill(ai_settings.bg_color )
    
    
    
    while True:
        gf.check_events(ship)
        gf.update_screen(ai_settings, screen, ship)


run_game()