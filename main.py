from flask import Flask, render_template, request, Response
import chess
import chess.svg
import chess.pgn
import csv


BOARDSIZE = 1000
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
    global move_num, my_board, BOARDSIZE, orientation, img
    if request.method == "POST":
        #POST
        if 'next_btn' in request.form:
            move_num = next_move(move_num)
            temp_svg = chess.svg.board(my_board, size=BOARDSIZE, orientation=orientation)
            img2 = temp_svg.replace('"1000"', '"100%"')
            return render_template('index.html', board_svg=img2,
                                   game_title=title)

        elif 'prev_btn' in request.form:
            move_num = prev_move(move_num)
            temp_svg = chess.svg.board(my_board, size=BOARDSIZE, orientation=orientation)
            img2 = temp_svg.replace('"1000"', '"100%"')
            return render_template('index.html', board_svg=img2,
                                   game_title=title)

        elif 'mirror' in request.form:
            orientation = mirror_board(orientation)
            temp_svg = chess.svg.board(my_board, size=BOARDSIZE, orientation=orientation)
            img2 = temp_svg.replace('"1000"', '"100%"')
            return render_template('index.html', board_svg=img2,
                                   game_title=title)

        elif 'reset' in request.form:
            reset_game()
            temp_svg = chess.svg.board(my_board, size=BOARDSIZE, orientation=orientation)
            img2 = temp_svg.replace('"1000"', '"100%"')
            return render_template('index.html', board_svg=img2,
                                   game_title=title)

        elif 'test_tts' in request.form:
            temp_svg = chess.svg.board(my_board, size=BOARDSIZE, orientation=orientation)
            img2 = temp_svg.replace('"1000"', '"100%"')
            return render_template('index.html', board_svg=img2,
                                   game_title=title)

    else:
        #GET
        reset_game()
        img = img.replace('"1000"', '"100%"')

        return render_template('index.html', board_svg=img,
                               game_title=title)


if __name__ == '__main__':
    app.run(debug=True)

