import time

class Solver:
    """Overall class to manage sudoku solver"""

    def __init__(self, visualizer, board):
        """Initialize board"""
        self.dim = 9
        self.end = (-1, -1)

        # Connect solver to main game
        self.board = board
        self.visualizer = visualizer
        self.tiles = visualizer.tiles

        self.selected_tile = None
    
    def _print_board(self):
        """Print the board to the terminal"""
        for i in range(self.dim):
            for j in range(self.dim):
                print(self.board[i][j], end=" ")
            print("")
    
    def solve(self, coords):
        """Use backtracking to solve sudoku"""
        # When all numbers are placed, there is a solution
        if coords == self.end:
            # self._print_board()
            return True

        next_pos = self._get_next(coords)

        # If number already placed, skip
        if self.board[coords[0]][coords[1]]:
            if self.solve(next_pos):
                return True
        else:
            # Try to place each number from 1 to 9, use backtracking
            for num in range(1, self.dim + 1):
                if self._is_valid(num, coords):
                    self.board[coords[0]][coords[1]] = num

                    # Get current tile
                    self.selected_tile = self._get_current_tile(coords)
                    self.selected_tile.final = True

                    # Set number of current tile
                    self.selected_tile.number = num
                    self.selected_tile.prep_number()
                    time.sleep(0.01)
                    self.visualizer.update_screen()

                    if self.solve(next_pos):
                        return True
                    self.board[coords[0]][coords[1]] = 0

                    # Delete number of current tile
                    self.selected_tile = self._get_current_tile(coords)
                    self.selected_tile.final = True
                    self.selected_tile.number = 0
                    self.selected_tile.prep_number()

                    self.selected_tile = None
                    time.sleep(0.01)
                    self.visualizer.update_screen()
                    
        # After all numbers tried, no solution
        return False

    def _get_current_tile(self, coords):
        """Return tile object with given coords"""
        for tile in self.tiles:
            if tile.position == coords:
                return tile
                
    def _is_valid(self, num, coords):
        """Determine whether the given num can be placed in coords"""
        # Check if the num is unique in current row
        if not all(num != x for x in self.board[coords[0]]):
            return False
        
        # Check if num is unique in current column
        current_col = [self.board[i][coords[1]] for i in range(self.dim)]
        if not all(num != x for x in current_col):
            return False
        
        # Check if num is unique in current 3x3 box
        start_row = coords[0] // 3
        start_col = coords[1] // 3
        current_box = ([self.board[3*start_row + i][3*start_col + j] 
                        for j in range(3) for i in range(3)])
        if not all(num != x for x in current_box):
            return False
        
        return True

    def _get_next(self, coords):
        """Get the next square to fill of given coords"""
        # All squares have been filled
        if coords == (self.dim - 1, self.dim - 1):
            return self.end
        
        # End of row
        if coords[1] == self.dim - 1:
            return (coords[0] + 1, 0)
        
        return (coords[0], coords[1] + 1)
        