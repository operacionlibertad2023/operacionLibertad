import pygame
import sys
from Button import Button
from Zelda_Juego import * 

pygame.init()

PANTALLA = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
W, H = PANTALLA.get_size()
icono = pygame.image.load('imagenes/principal/icon.png')
pygame.display.set_caption("Operacion Libertad")
BG = (18, 54, 52)
# Permite que los enemigos se muevan
Recorido_X = True
Recorido_Y = True
CambiarEje = False


def fuentes(size):
    return pygame.font.Font("imagenes/menu-botones/principal-fuente.ttf", size)


def juego():
    pantalla_paused = False

    class Juego:
        def __init__(self):
            self.PANTALLA = pygame.display.set_mode((W, H))
            pygame.display.set_caption("Operacion Libertad")
            self.nivel = Nivel()

        def corre_juego(self):
            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        sys.exit()
                    elif event.type == pygame.KEYDOWN:  
                        if event.key == pygame.K_ESCAPE:
                            pausa()

                self.PANTALLA.fill("black")
                self.nivel.corre()
                pygame.display.update()

    zelda_juego = Juego()
    zelda_juego.corre_juego()


def pausa():
    while True:
        PANTALLA.fill((54, 211, 238))
        MENU_MOUSE_POS = pygame.mouse.get_pos()

        # Crea boton para reanudar en el menu de pausa
        REANUDAR_BTN = Button(image=pygame.image.load("imagenes/menu-botones/Options Rect.png"), pos=(W // 2, H // 5),
                              text_input="REANUDAR", font=fuentes(70), base_color="#d7fcd4", hovering_color="White")

        # Crea boton para los ajustes en el menu de pausa
        AJUSTES_BTN = Button(image=pygame.image.load("imagenes/menu-botones/Options Rect.png"), pos=(W // 2, H // 3),
                             text_input="AJUSTES", font=fuentes(70), base_color="#d7fcd4", hovering_color="White")

        # Crea boton para volver al menu principal
        VOLVER_BTN = Button(image=pygame.image.load("imagenes/menu-botones/Quit Rect.png"), pos=(W // 2, H // 2),
                            text_input="MENU", font=fuentes(70), base_color="#d7fcd4", hovering_color="White")

        # Crea boton para salir al escritorio
        DESK_BTN = Button(image=pygame.image.load("imagenes/menu-botones/Options Rect.png"), pos=(W // 2, H * 3 // 4),
                          text_input="SALIR", font=fuentes(70), base_color="#d7fcd4", hovering_color="White")

        for button in [REANUDAR_BTN, AJUSTES_BTN, VOLVER_BTN, DESK_BTN]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(PANTALLA)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return

            if event.type == pygame.MOUSEBUTTONDOWN:
                if REANUDAR_BTN.checkForInput(MENU_MOUSE_POS):
                    return
                elif AJUSTES_BTN.checkForInput(MENU_MOUSE_POS):
                    pausa_ajustes()
                elif VOLVER_BTN.checkForInput(MENU_MOUSE_POS):
                    main_menu()
                elif DESK_BTN.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()


def pausa_ajustes():
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        PANTALLA.fill("white")

        OPTIONS_TEXT = fuentes(45).render("aguamte el lol", True, "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(W // 2, H // 3))
        PANTALLA.blit(OPTIONS_TEXT, OPTIONS_RECT)

        OPTIONS_BACK = Button(image=None, pos=(W // 2, H // 2),
                              text_input="BACK", font=fuentes(75), base_color="Black", hovering_color="Green")

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(PANTALLA)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return

            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    pausa()

        pygame.display.update()


def ajustes():
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        PANTALLA.fill("white")

        OPTIONS_TEXT = fuentes(45).render("aguamte el lol", True, "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(W // 2, H // 3))
        PANTALLA.blit(OPTIONS_TEXT, OPTIONS_RECT)

        OPTIONS_BACK = Button(image=None, pos=(W // 2, H // 2),
                              text_input="BACK", font=fuentes(75), base_color="Black", hovering_color="Green")

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(PANTALLA)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return

            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()

        pygame.display.update()


def main_menu():
    while True:
        PANTALLA.fill(BG)

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = fuentes(80).render("Operacion Libertad", True, "#cb08fc")

        MENU_RECT = MENU_TEXT.get_rect(center=(W // 2, H // 6))

        PLAY_BUTTON = Button(image=pygame.image.load("imagenes/menu-botones/Play Rect.png"), pos=(W // 2, H // 3),
                             text_input="JUGAR", font=fuentes(70), base_color="#d7fcd4", hovering_color="Green")
        OPTIONS_BUTTON = Button(image=pygame.image.load("imagenes/menu-botones/Options Rect.png"), pos=(W // 2, H // 1.7),
                                text_input="AJUSTES", font=fuentes(70), base_color="#d7fcd4", hovering_color="Green")
        QUIT_BUTTON = Button(image=pygame.image.load("imagenes/menu-botones/Quit Rect.png"), pos=(W // 2, H * 5 // 6),
                             text_input="SALIR", font=fuentes(70), base_color="#d7fcd4", hovering_color="Green")

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(PANTALLA)

        PANTALLA.blit(MENU_TEXT, MENU_RECT)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    juego()
                elif OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    ajustes()
                elif QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()


if __name__ == '__main__':
    main_menu()
