class Settings:
    """Manage visualizer settings"""

    def __init__(self):
        """Initialize settings"""

        # Global settings
        self.screen_size = 1260
        self.bg_color = (100, 100, 100)

        # Tile settings
        self.tile_size = self.screen_size / 9
        self.tile_color = (240, 240, 240)
        self.selected_tile_color = (180, 180, 180)