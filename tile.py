import pygame
from pygame.sprite import Sprite


class Tile(Sprite):
    """Overall class to manage a Sudoku tile"""

    def __init__(self, visualizer, board_pos, number=0):
        """Create a tile at given coords"""
        super().__init__()

        # Connect tile to main screen
        self.screen = visualizer.screen
        self.settings = visualizer.settings

        # Color of number
        self.color = self.settings.tile_color
        self.selected_color = self.settings.selected_tile_color

        # Set position attributes
        self.position = board_pos
        self.x_coord = board_pos[1] * self.settings.tile_size
        self.y_coord = board_pos[0] * self.settings.tile_size

        # Create a rect and place it appropriately 
        self.rect = pygame.Rect(0, 0, self.settings.tile_size,
            self.settings.tile_size)
        
        self.rect.x = self.x_coord
        self.rect.y = self.y_coord

        # Flag to determine if tile is selected
        self.selected = False

        # Flag to determine if tile is part of final board
        self.final = False

        # Font settings
        self.text_color = (0, 0, 0)
        self.font = pygame.font.SysFont(None, 48)

        self.number = number # Store final number of tile
        self.user_number = 0 # Store user selected number

    def draw_tile(self):
        """Draw tile to the screen"""
        if not self.selected:
            pygame.draw.rect(self.screen, self.color, self.rect)
        else:
            pygame.draw.rect(self.screen, self.selected_color, self.rect)
        
        if self.number or self.user_number:
            self.screen.blit(self.num_img, self.num_img_rect)

    def prep_number(self):
        """Create the number image"""
        number = self.number if self.final else self.user_number
        self.num_img = self.font.render(
            str(number), True, (0,0,0), self.color
        )
        self.num_img_rect = self.num_img.get_rect()

        if self.final:
            self.num_img_rect.center = self.rect.center
        else:
            self.num_img_rect.topright = self.rect.topright