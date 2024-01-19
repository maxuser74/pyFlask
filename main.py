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


def read_pgn_csv():
    with open('pgn/pgn.csv', newline='') as csvfile:
        temp_pgn = {}
        reader = csv.reader(csvfile)
        for row in reader:
            temp_pgn[row[0]] = row[1]
    return temp_pgn


pgn_list = read_pgn_csv()
print(pgn_list)


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
        print(t_move_num)
    else:
        pass

    return t_move_num


def prev_move(t_move_num):
    if t_move_num > 1:
        t_move_num = t_move_num - 1
        my_board.pop()
        print(t_move_num)
    else:
        pass
    return t_move_num


def mirror_board(t_orient):
    t_orient = not t_orient
    t_svg_board = chess.svg.board(my_board, size=BOARDSIZE, orientation=orientation)
    return t_svg_board, t_orient


app = Flask(__name__, static_url_path='/static')

#img = './static/chess_board.svg'

ico = './static/chess_king.svg'


@app.route('/', methods=['GET', 'POST'])
def index():
    global move_num, my_board, BOARDSIZE, orientation
    if request.method == "POST":
        #POST
        if 'next_btn' in request.form:
            print('Next')
            move_num = next_move(move_num)
            return render_template('index.html',
                                   board_svg=chess.svg.board(my_board, size=BOARDSIZE, orientation=orientation))

        elif 'prev_btn' in request.form:
            print('Prev')
            move_num = prev_move(move_num)
            return render_template('index.html',
                                   board_svg=chess.svg.board(my_board, size=BOARDSIZE, orientation=orientation))
    else:
        #GET
        return render_template('index.html', board_svg=img)


if __name__ == '__main__':
    app.run(debug=True)

