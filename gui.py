# Description: This file contains the GUI class that will be responsible
# for the game interface.

import pygame as pg


# font_path = "fonts/Chalktastic.ttf"
# self.font = pg.font.Font(font_path, 36)

class GUI:
    LINE_COLOR = (245, 245, 245)
    LINE_WIDTH = 12
    BACKGROUND_IMAGE = "image/background.jpg"

    def __init__(self, initial_window_width=800, initial_window_height=600):
        pg.init()  # Initialize pygame
        self.screen_width = initial_window_width  # Screen width
        self.screen_height = initial_window_height  # Screen height
        self.screen = pg.display.set_mode((initial_window_width, initial_window_height))  # Create the screen
        pg.display.set_caption("Tic Tac Toe")  # Set the window title
        self.background = pg.image.load(self.BACKGROUND_IMAGE).convert()  # Convert for faster blitting
        self.clock = pg.time.Clock()  # Create a clock to control the frame rate
        self.running = True  # Flag to control the game loop
        self.background = pg.transform.scale(self.background, (
            initial_window_width, initial_window_height))  # Scale the background image to fit the screen

    # draw the grid lines
    def draw_grid(self):
        for x in range(1, 3):
            # Vertical lines
            pg.draw.line(
                self.screen, self.LINE_COLOR,
                (self.screen_width // 3 * x, 0),
                (self.screen_width // 3 * x, self.screen_height),
                self.LINE_WIDTH
            )

            # Horizontal lines
            pg.draw.line(
                self.screen, self.LINE_COLOR,
                (0, self.screen_height // 3 * x),
                (self.screen_width, self.screen_height // 3 * x),
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

    def run(self):

        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False

            self.screen.blit(self.background, (0, 0))
            self.draw_grid()
            pg.display.flip()
            self.clock.tick(60)

        pg.quit()


GUI().run()
