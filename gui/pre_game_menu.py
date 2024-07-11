# This class handles the pre game menu before starting the game.
# It displays the name of the game and allows the user to choose
# between playing against a friend or AI.


import pygame as pg
import os


class PreGameMenu:
    WINDOW_WIDTH = 400  # Window/screen width
    WINDOW_HEIGHT = 300  # Window/screen height

    TEXT_COLOR = (255, 155, 55)  # Text color
    TEXT_SIZE = 40
    TEXT_WIDTH = 100  # Text width
    TEXT_HEIGHT = 260  # Text height

    GAME_SPEED = 60  # Value for clock()

    def __init__(self):
        pg.init()  # Initializes Pygame modules
        self.running = True  # Flag to keep the game running

        self.setup_screen()
        self.load_assets()
        self.setup_game_elements()
        self.play_music()

    # Set up the game screen and caption.
    def setup_screen(self):
        self.screen = pg.display.set_mode((self.WINDOW_WIDTH, self.WINDOW_HEIGHT))
        pg.display.set_caption('Pre Game Menu')

    # Load all necessary assets like fonts
    def load_assets(self):
        base_dir = os.path.dirname(os.path.dirname(__file__))
        self.font_path = os.path.join(base_dir, "assets", "font", "game_over_cre", "gameovercre1.ttf")

        if not os.path.exists(self.font_path):
            raise FileNotFoundError(f"No file '{self.font_path}' found")
        print(f"Using font path: {self.font_path}")

        self.font = pg.font.Font(self.font_path, self.TEXT_SIZE)

    # Initialize game elements like text and buttons
    def setup_game_elements(self):
        self.clock = pg.time.Clock()
        self.game_speed = self.GAME_SPEED
        self.buttons = [
            ("Play VS AI", (100, 200, self.TEXT_WIDTH, self.TEXT_HEIGHT)),
            ("Play VS Friend", (self.TEXT_WIDTH, self.TEXT_HEIGHT))
        ]

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

    def run(self):
        hue = 0
        while self.running:
            self.handle_event(pg.event.get())
            self.screen.fill((0, 0, 0))  # Clear the screen with black

            hue = (hue + 5) % 360
            color = pg.Color(0)
            color.hsva = (hue, 100, 100, 100)

            greet_text = self.font.render("Tic Tac Toe", True, color)
            self.screen.blit(greet_text, (75, 100))  # Draw the text surface

            pg.display.flip()
            self.clock.tick(self.game_speed)  # 60

        pg.quit()


if __name__ == "__main__":
    PreGameMenu().run()
