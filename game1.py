import pygame
import sys
from tkinker import *
import os


#COLORS
BLANC = (255, 255, 255)
NEGRE = (0, 0, 0)
LIGHTGREEN = (144, 238, 144)
DARKGREY = (169, 169, 169)
DARKGREY_HOVER = (150, 150, 150)
GRIS_CLAR = (230, 230, 230)
VERMELL = (200, 60, 60)
VERD = (60, 160, 60)
BLAU = (70, 130, 180)
pygame.init()
screen = pygame.display.set_mode((550, 900))




#Finestra d'inici
def finestrainiciarsesió():
   WIDTH, HEIGHT = 550, 900
   screen = pygame.display.set_mode((WIDTH, HEIGHT))
   pygame.display.set_caption("Iniciar Sessió")
   clock = pygame.time.Clock()


   font_titol = pygame.font.SysFont("Arial", 24, bold=True)
   font_text = pygame.font.SysFont("Arial", 18)


   # 1. DEFINIM ELS RECTANGLES (x, y, ample, alt)
   caja_usuari = pygame.Rect(50, 150, 450, 45)
   caja_contrasenya = pygame.Rect(50, 250, 450, 45)
   boto_entrar = pygame.Rect(50, 340, 200, 45)
   boto_tornar = pygame.Rect(300, 340, 200, 45)


   text_usuari = "   "
   text_contrasenya = ""
   casella_activa = None
  
