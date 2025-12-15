import pygame
import sys 

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Game Additions Setup")

try:
    background_img = pygame.transform.scale(
        pygame.image.load('background.png'), 
        (SCREEN_WIDTH, SCREEN_HEIGHT)
    )
except pygame.error:
    print("ERROR: Could not load 'background.png'. Using black screen.")
    background_img = None
    
try:
    sound_effect = pygame.mixer.Sound('sound.wav')
except pygame.error:
    print("ERROR: Could not load 'sound.wav'. Sound playback will be skipped.")
    sound_effect = None