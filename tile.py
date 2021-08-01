import pygame
from pygame.sprite import Sprite


class Tile(Sprite):
    """Overall class to manage a Sudoku tile"""

    def __init__(self, visualizer, x_coord, y_coord, number=0):
        """Create a tile at given coords"""
        super().__init__()

        self.screen = visualizer.screen
        self.settings = visualizer.settings
        self.color = self.settings.tile_color
        self.selected_color = self.settings.selected_tile_color

        self.position = (0, 0)

        # Create a rect and place it 
        self.rect = pygame.Rect(0, 0, self.settings.tile_size,
            self.settings.tile_size)
        
        self.rect.x = x_coord
        self.rect.y = y_coord

        # Flag to determine if tile is selected
        self.selected = False

        # Flag to determine if tile is part of original board
        self.original = False

        # Font settings
        self.text_color = (0, 0, 0)
        self.font = pygame.font.SysFont(None, 48)

        self.number = number

    def draw_tile(self):
        """Draw tile to the screen"""
        if not self.selected:
            pygame.draw.rect(self.screen, self.color, self.rect)
        else:
            pygame.draw.rect(self.screen, self.selected_color, self.rect)
        
        if self.number:
            self.screen.blit(self.num_img, self.num_img_rect)

    def prep_number(self):
        """Create the number image"""

        num_color = self.text_color if self.original else (0, 0, 255)

        self.num_img = self.font.render(
            str(self.number), True, num_color, self.color
        )
        self.num_img_rect = self.num_img.get_rect()
        self.num_img_rect.center = self.rect.center