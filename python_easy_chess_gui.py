#!/usr/bin/env python3
""" 
python_easy_chess_gui.py

Requirements:
    Python 3.7.3 and up

PySimpleGUI Square Mapping
board = [
    56, 57, ... 63
    ...
    8, 9, ...
    0, 1, 2, ...
]

row = [
    0, 0, ...
    1, 1, ...
    ...
    7, 7 ...
]

col = [
    0, 1, 2, ... 7
    0, 1, 2, ...
    ...
    0, 1, 2, ... 7
]


Python-Chess Square Mapping
board is the same as in PySimpleGUI
row is reversed
col is the same as in PySimpleGUI

"""

from easyChessGui import EasyChessGui


def main():
    engine_config_file = 'pecg_engines.json'
    user_config_file = 'pecg_user.json'

    pecg_book = 'Book/pecg_book.bin'
    book_from_computer_games = 'Book/computer.bin'
    book_from_human_games = 'Book/human.bin'

    is_use_gui_book = True
    is_random_book = True  # If false then use best book move
    max_book_ply = 8
    theme = 'Reddit'

    pecg = EasyChessGui(theme, engine_config_file, user_config_file,
                        pecg_book, book_from_computer_games,
                        book_from_human_games, is_use_gui_book, is_random_book,
                        max_book_ply)

    pecg.main_loop()


if __name__ == "__main__":
    main()
