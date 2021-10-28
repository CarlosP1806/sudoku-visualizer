# Sudoku Visualizer

## Description 

This project is a visualization of a backtracking algorithm that solves a classic sudoku puzzle. In addition, the user can also try to solve the sudoku on their own before watching the algorithm's solution. This is my first Python project, so I was motivated to build it to practice both my problem solving and coding knowledge. Moreover, all the project is object-oriented, as I wanted to expand my understanding of Python classes. 

## Technologies

- Python 3
- Pygame (to build visualization)
- Pandas (to store and manage sudoku database)

## Installation

Download all .py and .csv files and save them in a local directory of your choice. Be sure to have Python3, Pygame and Pandas installed to run the project. In order to start the program, type the following command in terminal:

```bash
    python3 visualizer.py
```

## Usage
When the application first opens, the user will be presented with a random sudoku from the database. These are the keys used to interact with the visualization:
- Use mouse to select a tile where you want to place a number
- When a tile is selected, type a number from 1 to 9 to place a provisional number
- When a tile with a provisional number is selected, press Enter to verify if number was correct (if it was, it will turn into a normal tile). Press 0 to delete provisional number
- To start the algorithm visualization, press s.

![Unsolved Soduku](assets/images/unsolved.png)

![Solved Sudoku](assets/images/solved_sudoku.png)

## Credits
All data of file "sudoku.csv" is retrieved from Kaggle. Original author is user Kyubyong Parg. File can be downloaded at
https://www.kaggle.com/bryanpark/sudoku/version/3