import pygame
import sys
import pandas as pd

from settings import Settings
from tile import Tile
from sudoku import Solver

class SudokuVisualizer:
    """Overall class to manage algorithm visualizer"""

    def __init__(self):
        """Initialize game assets"""

        # Pygame basic settings
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_size, 
            self.settings.screen_size)
        )
        pygame.display.set_caption("Sudoku Solver")

        # Matrix to represent board
        self.board, self.solution = self._create_board()
        self.tiles = pygame.sprite.Group()
        self._create_tiles()
        self.selected_tile = None

        # Solver object
        self.solver = Solver(self, self.board)

    def run_visualizer(self):
        """Main loop of visualizer"""
        while True:
            self._check_events()    
            self.update_screen()

    def _check_events(self):
        """Respond to events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_mouse_click(mouse_pos)
            
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_event(event)

    def _check_keydown_event(self, event):
        """Respond to key presses"""

        # Solve button clicked
        if event.key == pygame.K_s:
            self.solver.solve((0,0))

        # Number clicked
        if self.selected_tile:
            if event.key == pygame.K_0:
                self.selected_tile.user_number = 0
            elif event.key == pygame.K_1:
                self.selected_tile.user_number = 1
            elif event.key == pygame.K_2:
                self.selected_tile.user_number = 2
            elif event.key == pygame.K_3:
                self.selected_tile.user_number = 3
            elif event.key == pygame.K_4:
                self.selected_tile.user_number = 4
            elif event.key == pygame.K_5:
                self.selected_tile.user_number = 5
            elif event.key == pygame.K_6:
                self.selected_tile.user_number = 6
            elif event.key == pygame.K_7:
                self.selected_tile.user_number = 7
            elif event.key == pygame.K_8:
                self.selected_tile.user_number = 8
            elif event.key == pygame.K_9:
                self.selected_tile.user_number = 9
            
            # Try to insert number into final board
            elif event.key == pygame.K_RETURN:
                # Correct guess
                if (self.selected_tile.user_number ==
                    self.solution[self.selected_tile.position[0]]
                    [self.selected_tile.position[1]]):
                    self.selected_tile.number = self.selected_tile.user_number
                    self.selected_tile.final = True

                    self.board[self.selected_tile.position[0]] \
                        [self.selected_tile.position[1]] = self.selected_tile.number
                # Incorrect guess
                else:
                    self.selected_tile.user_number = 0

            self.selected_tile.prep_number()

    def _check_mouse_click(self, mouse_pos):
        """Respond to click on tile"""
        tiles_clicked = [
            t for t in self.tiles if t.rect.collidepoint(mouse_pos)
        ]

        if tiles_clicked and not tiles_clicked[0].final:
            # Deselect last clicked tile
            if self.selected_tile:
                self.selected_tile.selected = False

            # Select new tile
            self.selected_tile = tiles_clicked[0]
            self.selected_tile.selected = True

    def _create_board(self):
        """Choose random sudoku and create board along with solution"""
        with open("sudoku.csv", "r") as csv_file:
            sudokus = pd.read_csv("sudoku.csv")
            board_data = sudokus.sample()
            board_str = board_data.iloc[0, 0]
            solution_str = board_data.iloc[0, 1]
        
        return self._parse_board(board_str), self._parse_board(solution_str)

    def _parse_board(self, board_str):
        """Parse a string to sudoku board"""
        print(board_str)

        board = [[0 for j in range(9)] for i in range(9)]

        counter = 0        
        for i, row in enumerate(board):
            for j, element in enumerate(row):
                board[i][j] = int(board_str[counter])
                counter += 1
                
        return board

    def _create_tiles(self):
        """Create and place sudoku tiles"""

        for i in range(9):
            for j in range(9):
                x_coord = j * self.settings.tile_size
                y_coord = i * self.settings.tile_size
                number = self.board[i][j]
                tile = Tile(self, (i, j), number)
                
                if number:
                    tile.final = True

                tile.prep_number()
                self.tiles.add(tile)

    def _draw_separation_lines(self):
        """Draw the board lines that separate tiles"""
        for i in range(9):
            width = 4 if i % 3 == 0 else 1
            pygame.draw.line(
                self.screen,
                (0, 0, 0),
                (self.settings.tile_size*i, 0),
                (self.settings.tile_size*i, self.settings.screen_size),
                width=width
            )
            pygame.draw.line(
                self.screen,
                (0, 0, 0),
                (0, self.settings.tile_size*i),
                (self.settings.screen_size, self.settings.tile_size*i),
                width=width
            )
    
    def update_screen(self):
        """Draw Sudoku board""" 
        self.screen.fill(self.settings.bg_color)

        # Draw tiles
        for tile in self.tiles.sprites():
            tile.draw_tile()

        # Draw board lines
        self._draw_separation_lines()

        # Switch to newest screen
        pygame.display.flip()


if __name__ == '__main__':
    sv = SudokuVisualizer()
    sv.run_visualizer()