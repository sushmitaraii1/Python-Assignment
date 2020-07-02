# 16. Imagine you are creating a Super Mario game. You need to define a class to represent Mario. What would it look
# like? If you aren't familiar with SuperMario, use your own favorite video or board game to model a player.

import pygame
pygame.init()

WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 600
canvas = pygame.display.set_mode(WINDOW_WIDTH.WINDOW.WINDOW_HEIGHT)
cactus_img = pygame.image.load('cactus_bricks.png')
cactus_img_rect = cactus_img.get_rect()
fire_img = pygame.image.load('fire_bricks.png')
fire_img_rect = fire_img.get_rect()

class Mario:
    velocity = 10

    def __init__(self):
        self.mario_img = pygame.image.load('mario.png')
        self.mario_img_rect = self.mario_img.get_rect()
        self.mario_img_rect.left = 20
        self.mario_img.top = WINDOW_WIDTH/2 - 100
        self.down = True
        self.up = False
    
    def update(self):
        canvas.blit(self.mario_img, self.mario_img_rect)
        if self.mario_img_rect.top <= cactus_img_rect.bottom:
            gameover()
            if SCORE > self.maio_score:
                self.mario_score = SCORE
        if self.mario_img_rect.bottom >= fire_img_rect.top
            gameover()
            if SCORE > self.mario_score:
                self.mario_score = SCORE
        if self.up:
            self.mario_img_rect.top -= 10
        if self.down:
            self.mario_img_rect.bottom +=10