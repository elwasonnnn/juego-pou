import pygame
import sys
import random
from api_login import *


AMPLADA, ALCADA = 550, 900
app = "pou"

BLANC = (255, 255, 255)
NEGRE = (0, 0, 0)
GRIS_CLAR = (230, 230, 230)
GRIS_FOSC = (160, 160, 160)
BLAU = (70, 130, 180)
BLAU_FOSC = (50, 105, 155)
VERD = (60, 160, 60)
VERMELL = (200, 60, 60)
COLOR_PANTALLA = (230, 242, 255)
COLOR_TEXT = (35, 45, 65)


def dibuixar_boto(pantalla, rect, text, font, color_normal, color_actiu, pos_ratoli):
    color = color_actiu if rect.collidepoint(pos_ratoli) else color_normal
    pygame.draw.rect(pantalla, color, rect, border_radius=10)
    surf = font.render(text, True, BLANC)
    pantalla.blit(surf, surf.get_rect(center=rect.center))


def pantalla_iniciar_sessio(pantalla, rellotge, font_titol, font_text, usuaris):
    pygame.display.set_caption("Pou - Iniciar sessió")

    caja_usuari = pygame.Rect(50, 200, 450, 50)
    caja_contrasenya = pygame.Rect(50, 310, 450, 50)
    boto_entrar = pygame.Rect(50, 410, 210, 55)
    boto_tornar = pygame.Rect(290, 410, 210, 55)

    text_usuari = ""
    text_contrasenya = ""
    casella_activa = "usuari"
    missatge = ""

    while True:
        pos_ratoli = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "sortir"

            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if caja_usuari.collidepoint(event.pos):
                    casella_activa = "usuari"
                elif caja_contrasenya.collidepoint(event.pos):
                    casella_activa = "contrasenya"
                elif boto_entrar.collidepoint(event.pos):
                    if text_usuari == "" or text_contrasenya == "":
                        missatge = "Omple tots els camps."
                    elif text_usuari in usuaris and usuaris[text_usuari] == text_contrasenya:
                        missatge = f"Sessió iniciada com a {text_usuari}!"
                    else:
                        missatge = "Usuari o contrasenya incorrectes."
                elif boto_tornar.collidepoint(event.pos):
                    return "menu"

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    if casella_activa == "usuari":
                        text_usuari = text_usuari[:-1]
                    elif casella_activa == "contrasenya":
                        text_contrasenya = text_contrasenya[:-1]
                elif event.key == pygame.K_TAB:
                    casella_activa = "contrasenya" if casella_activa == "usuari" else "usuari"
                elif event.unicode.isprintable():
                    if casella_activa == "usuari" and len(text_usuari) < 15:
                        text_usuari += event.unicode
                    elif casella_activa == "contrasenya" and len(text_contrasenya) < 15:
                        text_contrasenya += event.unicode

        pantalla.fill(COLOR_PANTALLA)

        titol = font_titol.render("Iniciar sessió", True, COLOR_TEXT)
        pantalla.blit(titol, titol.get_rect(center=(AMPLADA // 2, 120)))

        pantalla.blit(font_text.render("Usuari:", True, COLOR_TEXT), (50, 172))
        color_u = GRIS_CLAR if casella_activa == "usuari" else BLANC
        pygame.draw.rect(pantalla, color_u, caja_usuari, border_radius=8)
        pygame.draw.rect(pantalla, BLAU if casella_activa == "usuari" else GRIS_FOSC, caja_usuari, 2, border_radius=8)
        pantalla.blit(font_text.render(text_usuari, True, NEGRE), (caja_usuari.x + 12, caja_usuari.y + 14))

        pantalla.blit(font_text.render("Contrasenya:", True, COLOR_TEXT), (50, 282))
        color_c = GRIS_CLAR if casella_activa == "contrasenya" else BLANC
        pygame.draw.rect(pantalla, color_c, caja_contrasenya, border_radius=8)
        pygame.draw.rect(pantalla, BLAU if casella_activa == "contrasenya" else GRIS_FOSC, caja_contrasenya, 2, border_radius=8)
        pantalla.blit(
            font_text.render("*" * len(text_contrasenya), True, NEGRE),
            (caja_contrasenya.x + 12, caja_contrasenya.y + 14),
        )

        dibuixar_boto(pantalla, boto_entrar, "Entrar", font_text, VERD, (45, 130, 45), pos_ratoli)
        dibuixar_boto(pantalla, boto_tornar, "Tornar", font_text, BLAU, BLAU_FOSC, pos_ratoli)

        if missatge:
            msg_surf = font_text.render(missatge, True, COLOR_TEXT)
            pantalla.blit(msg_surf, msg_surf.get_rect(center=(AMPLADA // 2, 520)))

        pygame.display.flip()
        rellotge.tick(60)


def pantalla_registre(pantalla, rellotge, font_titol, font_text, usuaris):
    pygame.display.set_caption("Pou - Registrar-se")

    caja_usuari = pygame.Rect(50, 200, 450, 50)
    caja_contrasenya = pygame.Rect(50, 310, 450, 50)
    boto_registrar = pygame.Rect(50, 410, 210, 55)
    boto_tornar = pygame.Rect(290, 410, 210, 55)

    text_usuari = ""
    text_contrasenya = ""
    casella_activa = "usuari"
    missatge = ""

    while True:
        pos_ratoli = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "sortir"

            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if caja_usuari.collidepoint(event.pos):
                    casella_activa = "usuari"
                elif caja_contrasenya.collidepoint(event.pos):
                    casella_activa = "contrasenya"
                elif boto_registrar.collidepoint(event.pos):
                    if text_usuari == "" or text_contrasenya == "":
                        missatge = "Omple tots els camps."
                    elif text_usuari in usuaris:
                        missatge = "Aquest usuari ja existeix."
                    else:
                        usuaris[text_usuari] = text_contrasenya
                        missatge = f"Usuari '{text_usuari}' creat!"
                        text_usuari = ""
                        text_contrasenya = ""
                elif boto_tornar.collidepoint(event.pos):
                    return "menu"

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    if casella_activa == "usuari":
                        text_usuari = text_usuari[:-1]
                    elif casella_activa == "contrasenya":
                        text_contrasenya = text_contrasenya[:-1]
                elif event.key == pygame.K_TAB:
                    casella_activa = "contrasenya" if casella_activa == "usuari" else "usuari"
                elif event.unicode.isprintable():
                    if casella_activa == "usuari" and len(text_usuari) < 15:
                        text_usuari += event.unicode
                    elif casella_activa == "contrasenya" and len(text_contrasenya) < 15:
                        text_contrasenya += event.unicode

        pantalla.fill(COLOR_PANTALLA)

        titol = font_titol.render("Registrar-se", True, COLOR_TEXT)
        pantalla.blit(titol, titol.get_rect(center=(AMPLADA // 2, 120)))

        pantalla.blit(font_text.render("Nou usuari:", True, COLOR_TEXT), (50, 172))
        color_u = GRIS_CLAR if casella_activa == "usuari" else BLANC
        pygame.draw.rect(pantalla, color_u, caja_usuari, border_radius=8)
        pygame.draw.rect(pantalla, BLAU if casella_activa == "usuari" else GRIS_FOSC, caja_usuari, 2, border_radius=8)
        pantalla.blit(font_text.render(text_usuari, True, NEGRE), (caja_usuari.x + 12, caja_usuari.y + 14))

        pantalla.blit(font_text.render("Contrasenya:", True, COLOR_TEXT), (50, 282))
        color_c = GRIS_CLAR if casella_activa == "contrasenya" else BLANC
        pygame.draw.rect(pantalla, color_c, caja_contrasenya, border_radius=8)
        pygame.draw.rect(pantalla, BLAU if casella_activa == "contrasenya" else GRIS_FOSC, caja_contrasenya, 2, border_radius=8)
        pantalla.blit(
            font_text.render("*" * len(text_contrasenya), True, NEGRE),
            (caja_contrasenya.x + 12, caja_contrasenya.y + 14),
        )

        dibuixar_boto(pantalla, boto_registrar, "Registrar", font_text, VERD, (45, 130, 45), pos_ratoli)
        dibuixar_boto(pantalla, boto_tornar, "Tornar", font_text, BLAU, BLAU_FOSC, pos_ratoli)

        if missatge:
            msg_surf = font_text.render(missatge, True, COLOR_TEXT)
            pantalla.blit(msg_surf, msg_surf.get_rect(center=(AMPLADA // 2, 520)))

        pygame.display.flip()
        rellotge.tick(60)


def pantalla_classificacio(pantalla, rellotge, font_titol, font_text, classificacio):
    pygame.display.set_caption("Pou - Classificació")
    boto_tornar = pygame.Rect(125, 650, 300, 60)

    while True:
        pos_ratoli = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "sortir"
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if boto_tornar.collidepoint(event.pos):
                    return "menu"

        pantalla.fill(COLOR_PANTALLA)

        titol = font_titol.render("Classificació", True, COLOR_TEXT)
        pantalla.blit(titol, titol.get_rect(center=(AMPLADA // 2, 130)))

        # Ordena de major a menor puntuació
        ranking = sorted(classificacio, key=lambda x: x[1], reverse=True)
        y = 220
        for posicio, (nom, punts) in enumerate(ranking, start=1):
            linia = f"{posicio}. {nom} - {punts} pts"
            surf = font_text.render(linia, True, COLOR_TEXT)
            pantalla.blit(surf, (110, y))
            y += 55

        dibuixar_boto(pantalla, boto_tornar, "Tornar", font_text, BLAU, BLAU_FOSC, pos_ratoli)

        pygame.display.flip()
        rellotge.tick(60)


def menu_principal():
    pygame.init()
    pantalla = pygame.display.set_mode((AMPLADA, ALCADA))
    rellotge = pygame.time.Clock()

    font_titol = pygame.font.SysFont("Arial", 36, bold=True)
    font_boto = pygame.font.SysFont("Arial", 22, bold=True)
    font_text = pygame.font.SysFont("Arial", 20)

    usuaris = {"admin": "1234"}
    classificacio = [("Marta", 420), ("Marc", 310), ("Anna", 250), ("Pol", 180)]

    botons = [
        (pygame.Rect(75, 250, 400, 65), "Iniciar sessió", "login"),
        (pygame.Rect(75, 340, 400, 65), "Registrar-se", "registre"),
        (pygame.Rect(75, 430, 400, 65), "Classificació", "classificacio"),
        (pygame.Rect(75, 520, 400, 65), "Sortir", "sortir"),
    ]

    pantalla_actual = "menu"

    while True:
        if pantalla_actual == "menu":
            pygame.display.set_caption("Pou - Menú principal")
            pos_ratoli = pygame.mouse.get_pos()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    for rect, _, accio in botons:
                        if rect.collidepoint(event.pos):
                            pantalla_actual = accio

            pantalla.fill(COLOR_PANTALLA)
            titol = font_titol.render("Pou - Benvingut!", True, COLOR_TEXT)
            pantalla.blit(titol, titol.get_rect(center=(AMPLADA // 2, 140)))

            for rect, text_boto, _ in botons:
                dibuixar_boto(pantalla, rect, text_boto, font_boto, BLAU, BLAU_FOSC, pos_ratoli)

            pygame.display.flip()
            rellotge.tick(60)

        elif pantalla_actual == "login":
            pantalla_actual = pantalla_iniciar_sessio(pantalla, rellotge, font_titol, font_text, usuaris)
        elif pantalla_actual == "registre":
            pantalla_actual = pantalla_registre(pantalla, rellotge, font_titol, font_text, usuaris)
        elif pantalla_actual == "classificacio":
            pantalla_actual = pantalla_classificacio(pantalla, rellotge, font_titol, font_text, classificacio)
        elif pantalla_actual == "sortir":
            pygame.quit()
            sys.exit()


if __name__ == "__main__":
    menu_principal()


# --- Codi afegit ---
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