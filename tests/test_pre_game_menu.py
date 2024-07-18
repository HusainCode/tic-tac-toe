# This class is responsible for testing the pre game menu

import unittest
import pygame as pg
from unittest.mock import patch, MagicMock

from gui.pre_game_menu import PreGameMenu


class TestPreGameMenu(unittest.TestCase):

    @patch('pygame.display.set_mode')
    @patch('pygame.display.set_caption')  # Avoid changing the window title
    @patch('pygame.mixer.music.load') #
    def test_initialize(self,mock_play,mock_load, mock_set_mode, mock_set_caption):
        # Test the initialization of PreGameMenu
        pre_game_menu = PreGameMenu()

        # Ensure set_mode is called with the correct parameters
        mock_set_mode.assert_called_once_with((PreGameMenu.WINDOW_WIDTH, PreGameMenu.WINDOW_HEIGHT))
        # Ensure set_caption is called with the correct parameters
        mock_set_caption.assert_called_once_with('Pre Game Menu')

    @patch('os.path.exists', return_value=True) # Mock the os.path.exists method to always return True
    @patch('pygame.font.Font') # Mock the pygame font.Font method
    def test_load_assets(self, mock_font, mock_exists):
        pre_game_menu = PreGameMenu()
        self.assertTrue(mock_font.called)

    @patch("pygame.event.get")
    def test_handle_event_quit(self, mock_event_get):
        # Mock a Quit event
        mock_event_get.return_value = [pg.event.Event(pg.QUIT)]
        pre_game_menu = PreGameMenu()
        pre_game_menu.handle_event(mock_event_get.return_value)
        self.assertFalse(pre_game_menu.running)


if __name__ == '__main__':
    unittest.main()
