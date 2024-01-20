from flask import Flask, render_template, request
import chess
import chess.svg
import chess.pgn
import csv
from markupsafe import Markup

BOARDSIZE = 600
my_board = chess.Board()
orientation = True
move_num = 0

img = chess.svg.board(my_board, size= BOARDSIZE, orientation= orientation )


moves = ['---','e4', 'e5', 'Nf3', 'Nc6', 'd4', 'exd4', 'Nxd4', 'Bc5']
title = 'Scotch'


def elaborate_svg(original_svg):
    specific_word = "<svg "
    new_substring = 'preserveAspectRatio="none" '

    original_svg = original_svg.replace('"600"', '"100%"')

    # Find the position of the specific word
    position = original_svg.find(specific_word)

    # Check if the word is found
    if position != -1:
        # Create a new string by concatenating the parts before and after the word
        new_svg = (original_svg[:position + len(specific_word)] +
                   new_substring + original_svg[position + len(specific_word):])
        return new_svg
    else:
        # Word not found, return the original string
        return original_svg


def read_pgn_csv():
    with open('pgn/pgn.csv', newline='') as csvfile:
        temp_pgn = {}
        reader = csv.reader(csvfile)
        for row in reader:
            temp_pgn[row[0]] = row[1]
    return temp_pgn


pgn_list = read_pgn_csv()


def run_pgn(file_name):
    try:
        # Open PGN file
        temp_game = chess.pgn.read_game(open(file_name))
        temp_board = chess.Board()
        temp_str_san_moves_array = ['---']

        # Make moves array
        for move in temp_game.mainline_moves():
            a = temp_board.san(move)
            temp_str_san_moves_array.append(a)
            temp_board.push(move)
        print(temp_str_san_moves_array[0:5])

        # reset Board
        temp_board = chess.Board()
        t_move_num = 0
        return temp_board, temp_str_san_moves_array, t_move_num

    except:
        print('Wrong PGN')


def next_move(t_move_num):
    if t_move_num < len(moves) - 1:
        t_move_num = t_move_num + 1
        my_board.push_san(moves[t_move_num])
    else:
        pass
    return t_move_num


def prev_move(t_move_num):
    if t_move_num > 0:
        t_move_num = t_move_num - 1
        my_board.pop()
    else:
        pass
    return t_move_num


def mirror_board(t_orient):
    t_orient = not t_orient
    return t_orient


app = Flask(__name__, static_url_path='/static')

ico = './static/chess_king.svg'


def reset_game():
    global move_num, my_board, BOARDSIZE, orientation, moves, title

    moves = ['---', 'e4', 'e5', 'Nf3', 'Nc6', 'd4', 'exd4', 'Nxd4', 'Bc5']
    title = 'Scotch'
    move_num = 0
    my_board = chess.Board()
    orientation = True
    my_board.reset_board()


@app.route('/', methods=['GET', 'POST'])
def index():
    global move_num, my_board, BOARDSIZE, orientation
    if request.method == "POST":
        #POST
        if 'next_btn' in request.form:
            move_num = next_move(move_num)
            temp_svg = chess.svg.board(my_board, size=BOARDSIZE, orientation=orientation)
            img2 = elaborate_svg(temp_svg)
            return render_template('index.html', board_svg=img2,
                                   game_title=title)

        elif 'prev_btn' in request.form:
            move_num = prev_move(move_num)
            temp_svg = chess.svg.board(my_board, size=BOARDSIZE, orientation=orientation)
            img2 = elaborate_svg(temp_svg)
            return render_template('index.html', board_svg=img2,
                                   game_title=title)

        elif 'mirror' in request.form:
            orientation = mirror_board(orientation)
            temp_svg = chess.svg.board(my_board, size=BOARDSIZE, orientation=orientation)
            img2 = elaborate_svg(temp_svg)
            return render_template('index.html', board_svg=img2,
                                   game_title=title)

        elif 'reset' in request.form:
            reset_game()
            temp_svg = chess.svg.board(my_board, size=BOARDSIZE, orientation=orientation)
            img2 = elaborate_svg(temp_svg)
            return render_template('index.html', board_svg=img2,
                                   game_title=title)

    else:
        #GET
        reset_game()
        img2 = elaborate_svg(img)
        return render_template('index.html', board_svg=img2,
                               game_title=title)


if __name__ == '__main__':
    app.run(debug=True)

