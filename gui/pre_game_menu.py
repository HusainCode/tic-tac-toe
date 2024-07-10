# This file contains
# the PreGameMenu class which is responsible for creating the pre-game menu

import pygame as pg


class PreGameMenu:
    WINDOW_WIDTH = 400
    WINDOW_HEIGHT = 300
    BUTTON_WIDTH = 50
    BUTTON_HEIGHT = 50
    BUTTON_COLOR = (192, 192, 192)
    BUTTON_HIGHLIGHT = (255, 255, 255)
    BUTTON_SHADOW = (128, 128, 128)
    TEXT_COLOR = (0, 0, 0)

    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((self.WINDOW_WIDTH, self.WINDOW_HEIGHT))
        pg.display.set_caption('Pre-Game Menu')
        self.font = pg.font.SysFont('Arial', 20)
        self.running = True
        self.clock = pg.time.Clock()
        self.buttons = [("Play against AI", (100, 200, self.BUTTON_WIDTH, self.BUTTON_HEIGHT)),
                        ("Play against a friend", (10, 260, self.BUTTON_WIDTH, self.BUTTON_HEIGHT))]

    def draw_buttons(self, text, rect):
        x, y, width, height = rect
        pg.draw.rect(self.screen, self.BUTTON_COLOR, rect)
        pg.draw.line(self.screen, self.BUTTON_HIGHLIGHT, (x, y), (x + width, y), 2)
        pg.draw.line(self.screen, self.BUTTON_HIGHLIGHT, (x, y), (x, y + height), 2)
        pg.draw.line(self.screen, self.BUTTON_SHADOW, (x, y + height), (x + width, y + height), 2)
        pg.draw.line(self.screen, self.BUTTON_SHADOW, (x + width, y), (x + width, y + height), 2)

        text_surface = self.font.render(text, True, self.TEXT_COLOR)
        text_rect = text_surface.get_rect(center=(x + width // 2, y + height // 2))
        self.screen.blit(text_surface, text_rect)

    def pre_game_menu(self):
        self.screen.fill((0, 0, 0))
        for text, rect in self.buttons:
            self.draw_buttons(text, rect)

    def start_the_game(self):
        pg.draw.line(self.screen)

    def handle_event(self, events):
        for event in events:
            if event.type == pg.QUIT:
                self.running = False
            elif event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
                mouse_x, mouse_y = event.pos
                for text, rect in self.buttons:
                    if pg.Rect(rect).collidepoint(mouse_x, mouse_y):
                        print(f"Button '{text}' pressed")

    def run(self):
        while self.running:
            self.handle_event(pg.event.get())
            self.pre_game_menu()
            self.clock.tick(60)
            pg.display.flip()
        pg.quit()


PreGameMenu().run()
