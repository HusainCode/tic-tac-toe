# This class handles the pre game menu before starting the game.
# It displays the name of the game and allows the user to choose
# between playing against a friend or AI.


import pygame as pg
import os
import random


class PreGameMenu:
    WINDOW_WIDTH = 400  # Window/screen width
    WINDOW_HEIGHT = 300  # Window/screen height

    TEXT_COLOR = (255, 155, 55)  # Text color
    TEXT_SIZE = 40
    TEXT_WIDTH = 100  # Text width
    TEXT_HEIGHT = 260  # Text height
    TEXT_POSITION = (0, 0)

    GAME_SPEED = 60  # Value for clock()

    BUTTON_TEXT_SIZE = 25
    BUTTONS = [  # Define buttons with text and positions
        ("  Play AI  ", (50, 250, 150, 50)),
        ("Play Friend", (210, 250, 150, 50))
    ]

    def __init__(self):
        pg.init()  # Initializes Pygame modules
        self.running = True  # Flag to keep the game running

        self.setup_screen()
        self.load_assets()
        self.play_music()

    # Set up the game screen and caption.
    def setup_screen(self):
        self.screen = pg.display.set_mode((self.WINDOW_WIDTH, self.WINDOW_HEIGHT))
        pg.display.set_caption('Pre Game Menu')

    #  CONSIDER REFACTORING THIS METHOD
    # Load all necessary assets like fonts
    def load_assets(self):
        base_dir = os.path.dirname(os.path.dirname(__file__))
        self.font_path = os.path.join(base_dir, "assets", "font", "game_over_cre", "gameovercre1.ttf")

        if not os.path.exists(self.font_path):
            raise FileNotFoundError(f"No file '{self.font_path}' found")
        print(f"Using font path: {self.font_path}")

        self.font = pg.font.Font(self.font_path, self.TEXT_SIZE)

        self.font = pg.font.Font(self.font_path, self.TEXT_SIZE)
        self.button_font = pg.font.Font(self.font_path, self.BUTTON_TEXT_SIZE)

    # CONSIDER REFACTORING THIS METHOD
    def play_music(self):
        base_dir = os.path.dirname(os.path.dirname(__file__))
        music_path = os.path.join(base_dir, "assets", "music", "8-bit_bluesy_battle.ogg")

        if os.path.exists(music_path):
            pg.mixer.music.load(music_path)
            pg.mixer.music.play(-1)
        else:
            print(f"Music file '{music_path}' not found")

    def handle_event(self, events):
        for event in events:
            if event.type == pg.QUIT:
                self.running = False
            elif event.type == pg.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                for text, rect in self.BUTTONS:
                    if pg.Rect(rect).collidepoint(mouse_pos):
                        print(f"Button '{text}' clicked!")

    # IT MUST BE REFACTORED
    def run(self):
        hue = 0
        hue_ai = 10
        hue_friend = 30

        self.clock = pg.time.Clock()
        while self.running:
            self.handle_event(pg.event.get())
            self.screen.fill((0, 0, 0))

            for _ in range(100):  # number of stars
                x = random.randint(0, self.WINDOW_WIDTH)
                y = random.randint(0, self.WINDOW_HEIGHT)
                self.screen.set_at((x, y), (255, 255, 255))  # Draw white stars

            hue = (hue + 5) % 360
            color = pg.Color(0)
            color.hsva = (hue, 100, 100, 100)

            hue_ai = (hue_ai + 7) % 360
            hue_friend = (hue_friend + 3) % 360

            # Set button text colors
            text_color_ai = pg.Color(0)
            text_color_ai.hsva = (hue_ai, 100, 100, 100)

            text_color_friend = pg.Color(0)
            text_color_friend.hsva = (hue_friend, 100, 100, 100)

            greet_text = self.font.render("Tic Tac Toe", True, color)
            self.screen.blit(greet_text, (75, 100))  # Draw the text surface

            button_text_colors = [text_color_ai, text_color_friend]
            for i, (text, rect) in enumerate(self.BUTTONS):
                text_color = button_text_colors[i]
                button_text = self.button_font.render(text, True, text_color)
                text_rect = button_text.get_rect(center=(rect[0] + rect[2] // 2, rect[1] + rect[3] // 2))
                self.screen.blit(button_text, text_rect)

            pg.display.flip()
            self.clock.tick(self.GAME_SPEED)

        pg.quit()


if __name__ == "__main__":
    PreGameMenu().run()
