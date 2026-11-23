import pygame
import sys
import random

pygame.init()
saltant = 0
WIDTH = 1500
HEIGHT = 1500
playerWidth = 50
playerHeight = 50
screen = pygame.display.set_mode((550, 900))
pygame.display.set_caption("Projecte-pygame")

clock = pygame.time.Clock()

mario = pygame.Rect(550, 700, 50, 50)
terra = pygame.Rect(0, 750, 550, 150)





SPEED = 500  # pixels/second


objetos = [mario]

running = True

while running == True:
    dt = clock.tick(120) / 1000.0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    for obj in objetos:
        oldY = obj.y
        oldX = obj.x
    
    mouse_x, mouse_y = pygame.mouse.get_pos()
    Keys = pygame.key.get_pressed()

    mario.x = mouse_x - 25

    screen.fill((0, 124, 200))
    pygame.draw.rect(screen, (75, 50, 50), mario)
    pygame.draw.rect(screen, (50, 100, 50), terra)



    pygame.display.flip()

pygame.quit()
sys.exit()