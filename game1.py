import pygame


AMPLADA, ALCADA = 550, 900
COLOR_PANTALLA = (230, 242, 255)
COLOR_TEXT = (35, 45, 65)
COLOR_BOTO = (70, 130, 180)
COLOR_BOTO_ACTIU = (50, 105, 155)
COLOR_TEXT_BOTO = (255, 255, 255)


def mostrar_pantalla_principal():
    pygame.init()
    pantalla = pygame.display.set_mode((AMPLADA, ALCADA))
    pygame.display.set_caption("Pou - Menú principal")
    rellotge = pygame.time.Clock()

    lletra_titol = pygame.font.SysFont("Arial", 42, bold=True)
    lletra_boto = pygame.font.SysFont("Arial", 25, bold=True)
    lletra_missatge = pygame.font.SysFont("Arial", 18)

    botons = [
        (pygame.Rect(75, 290, 400, 70), "Iniciar sessió", "iniciar sessió"),
        (pygame.Rect(75, 390, 400, 70), "Registrar-se", "registre"),
        (pygame.Rect(75, 490, 400, 70), "Classificació", "classificació"),
        (pygame.Rect(75, 590, 400, 70), "Sortir", "sortir"),
    ]
    missatge = ""
    en_marxa = True

    while en_marxa:
        posicio_ratoli = pygame.mouse.get_pos()

        for esdeveniment in pygame.event.get():
            if esdeveniment.type == pygame.QUIT:
                en_marxa = False
            elif esdeveniment.type == pygame.MOUSEBUTTONDOWN and esdeveniment.button == 1:
                for rectangle, _, accio in botons:
                    if rectangle.collidepoint(esdeveniment.pos):
                        if accio == "sortir":
                            en_marxa = False
                        else:
                            missatge = f"La pantalla de {accio} encara no està disponible."

        pantalla.fill(COLOR_PANTALLA)
        titol = lletra_titol.render("Pou - Benvingut!", True, COLOR_TEXT)
        pantalla.blit(titol, titol.get_rect(center=(AMPLADA // 2, 175)))

        for rectangle, text_boto, _ in botons:
            color = COLOR_BOTO_ACTIU if rectangle.collidepoint(posicio_ratoli) else COLOR_BOTO
            pygame.draw.rect(pantalla, color, rectangle, border_radius=12)
            text_renderitzat = lletra_boto.render(text_boto, True, COLOR_TEXT_BOTO)
            pantalla.blit(text_renderitzat, text_renderitzat.get_rect(center=rectangle.center))

        if missatge:
            missatge_renderitzat = lletra_missatge.render(missatge, True, COLOR_TEXT)
            pantalla.blit(
                missatge_renderitzat,
                missatge_renderitzat.get_rect(center=(AMPLADA // 2, 720)),
            )

        pygame.display.flip()
        rellotge.tick(60)

    pygame.quit()


if __name__ == "__main__":
    mostrar_pantalla_principal()
