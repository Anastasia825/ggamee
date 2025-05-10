import random
import sys
import pygame 
from pygame.locals import *

FPS = 32
scr_width = 289
scr_height = 511
display_screen_window = pygame.display.set_mode((scr_width, scr_height))
playground = scr_height * 0.8
game_img = {}
game_audio_sound = {}
player = 'images/bird.png'
bcg_img = 'images/background.png'
pipe_img = 'images/pipe.png'

def welcome_main_screen():
    p_x = int(scr_width/5)
    p_y = int((scr_height - game_img['player'].get_height())/2)
    msgx = int((scr_width - game_img['message'].get_width())/2)
    msgy = int(scr_height * 0.13)
    b_x = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == KEYDOWN and event.type == K_ESCAPE):
                pygame.quit()
                sys.exit()
                