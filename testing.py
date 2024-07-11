import sys
import pygame as pg

pg.init()

screen = pg.display.set_mode((500, 500))
pg.display.set_caption('Tic-Tac-Toe')
font_path = "assets/font/game_over_cre/gameovercre1.ttf"

font = pg.font.Font(font_path, 44)  # Default font, size 74
text = font.render('Hello, World!', True, (255, 155, 55))  # White color

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()

    screen.fill((0, 0, 0))
    screen.blit(text, (50, 200))  # Position the text
    pg.display.update()
