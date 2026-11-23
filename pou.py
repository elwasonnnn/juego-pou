import pygame
import sys
import random

pygame.init()
saltant = 0
WIDTH = 1500
HEIGHT = 1500
playerWidth = 50
playerHeight = 50
screen = pygame.display.set_mode((550, 1080))
pygame.display.set_caption("Projecte-pygame")

clock = pygame.time.Clock()

mario = pygame.Rect(600, 820, 50, 50)
terra = pygame.Rect(0, 870, 550, 150)

comida1 = pygame.Rect(0, 870, 550, 150)
comida2 = pygame.Rect(0, 870, 550, 150)
comida3 = pygame.Rect(0, 8objeto = pygame.Rect(0, 870, 550, 150)70, 550, 150)
comida4 = pygame.Rect(0, 870, 550, 150)

objeto1 = pygame.Rect(0, 870, 550, 150)
objeto2 = pygame.Rect(0, 870, 550, 150)
objeto3 = pygame.Rect(0, 870, 550, 150)
objeto4 = pygame.Rect(0, 870, 550, 150)


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