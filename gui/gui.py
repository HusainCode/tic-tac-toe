# Description: This file contains the GUI class that will be responsible
# for the game interface.

import pygame as pg

# self.font = pg.font.Font(font_path, 36)

class GUI:
    WINDOW_WIDTH = 800
    WINDOW_HEIGHT = 600
    LINE_COLOR = (245, 245, 245)
    LINE_WIDTH = 12
    
    GAME_SPEED = 60  # Value for clock() # IT SHOULD MATCH THE "pre_game_menu.py" GAME_SPEED

    def __init__(self):
        pg.init()  # Initialize pygame
        self.screen_width = GUI.WINDOW_WIDTH  # Screen width
        self.screen_height = GUI.WINDOW_HEIGHT  # Screen height

        self.font_path = "../assets/chalktastic/license.txt"  # Path to the font file
        self.font = pg.font.Font(self.font_path, 36)  # Create a font object

        self.screen = pg.display.set_mode((GUI.WINDOW_WIDTH, GUI.WINDOW_HEIGHT))  # Create the screen

        pg.display.set_caption("Tic Tac Toe")  # Set the window title
        self.background = pg.image.load(self.BACKGROUND_IMAGE).convert()  # Convert for faster blitting

        self.clock = pg.time.Clock()  # Create a clock to control the frame rate
        self.running = True  # Flag to control the game loop

        self.background = pg.transform.scale(self.background, (
            GUI.WINDOW_WIDTH, GUI.WINDOW_HEIGHT))  # Scale the background image to fit the screen
        self.board = [[None for _ in range(3)] for _ in range(3)]  # 3x3 board

    # draw the grid lines
    def draw_grid(self):
        # Draw the vertical grid lines
        for x in range(1, 3):
            pg.draw.line(
                self.screen, self.LINE_COLOR,
                (self.screen_width // 3 * x, 0),  # start point of the line
                (self.screen_width // 3 * x, self.screen_height),  # end point of the line
                self.LINE_WIDTH
            )

            # Draw the horizontal lines
            pg.draw.line(
                self.screen, self.LINE_COLOR,
                (0, self.screen_height // 3 * x),  # start point of the line
                (self.screen_width, self.screen_height // 3 * x),  # end point of the line
                self.LINE_WIDTH
            )

    def draw_x(self, screen, row, col):
        # Calculate coordinates for the X based on row and column
        x = col * self.cell_size + self.cell_size // 2
        y = row * self.cell_size + self.cell_size // 2

        # Draw the X as two lines with a bit of offset for a nicer look
        offset = self.cell_size // 4
        pg.draw.line(screen, self.x_color, (x - offset, y - offset), (x + offset, y + offset), self.line_width)
        pg.draw.line(screen, self.x_color, (x + offset, y - offset), (x - offset, y + offset), self.line_width)

    def draw_o(self, screen, row, col):
        # Calculate coordinates for the O based on row and column
        x = col * self.cell_size + self.cell_size // 2
        y = row * self.cell_size + self.cell_size // 2

        # Draw the O as a circle with a slightly smaller radius to fit in the cell
        radius = self.cell_size // 2 - self.line_width // 2
        pg.draw.circle(screen, self.o_color, (x, y), radius, self.line_width)

    # draw the winning line
    def draw_line(self, screen, start, end):
        pass

    # update the content of the screen
    def update_content(self):
        pg.display.update()

    # Display the pre-game menu options before starting the game

    def handle_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return False
        return True

    def run(self):
        running = True  # Flag to control the game loop

        # Game loop to keep the game running
        while running:
            running = self.handle_events()

            # Clear the screen and draw the background
            self.screen.blit(self.background, (0, 0))
            # Draw the grid lines
            self.draw_grid()
            pg.display.flip()
            self.clock.tick(60)

        pg.quit()  # Quit pygame when pressing the close button


GUI().run()
