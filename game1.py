import pygame


WIDTH, HEIGHT = 550, 900
BACKGROUND = (230, 242, 255)
TEXT_COLOR = (35, 45, 65)
BUTTON_COLOR = (70, 130, 180)
BUTTON_HOVER_COLOR = (50, 105, 155)
BUTTON_TEXT_COLOR = (255, 255, 255)


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Pou - Menú principal")
    clock = pygame.time.Clock()

    title_font = pygame.font.SysFont("Arial", 42, bold=True)
    button_font = pygame.font.SysFont("Arial", 25, bold=True)
    message_font = pygame.font.SysFont("Arial", 18)

    buttons = [
        (pygame.Rect(75, 290, 400, 70), "Iniciar sesión", "iniciar sesión"),
        (pygame.Rect(75, 390, 400, 70), "Registrarse", "registro"),
        (pygame.Rect(75, 490, 400, 70), "Tabla de puntuación", "tabla de puntuación"),
        (pygame.Rect(75, 590, 400, 70), "Salir", "salir"),
    ]
    message = ""
    running = True

    while running:
        mouse_position = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                for rect, _, action in buttons:
                    if rect.collidepoint(event.pos):
                        if action == "salir":
                            running = False
                        else:
                            message = f"La pantalla de {action} aún no está disponible."

        screen.fill(BACKGROUND)
        title = title_font.render("Pou - Bienvenido!", True, TEXT_COLOR)
        screen.blit(title, title.get_rect(center=(WIDTH // 2, 175)))

        for rect, label, _ in buttons:
            color = BUTTON_HOVER_COLOR if rect.collidepoint(mouse_position) else BUTTON_COLOR
            pygame.draw.rect(screen, color, rect, border_radius=12)
            button_text = button_font.render(label, True, BUTTON_TEXT_COLOR)
            screen.blit(button_text, button_text.get_rect(center=rect.center))

        if message:
            rendered_message = message_font.render(message, True, TEXT_COLOR)
            screen.blit(
                rendered_message,
                rendered_message.get_rect(center=(WIDTH // 2, 720)),
            )

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()
