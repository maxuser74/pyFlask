import flask
from flask import Flask, render_template, request, jsonify
import chess
import chess.svg
import chess.pgn
import os
import json

STAT_DEV = True

BOARDSIZE = 1000
my_board = chess.Board()
orientation = True
move_num = 0
img = chess.svg.board(my_board, size= BOARDSIZE, orientation= orientation )
img = img.replace('"1000"', '"100%"')

moves = ['---','e4', 'e5', 'Nf3', 'Nc6', 'd4', 'exd4', 'Nxd4', 'Bc5']
title = 'Scotch'

dir_path = 'pgn'

# list to store files
pgn_list = []
# Iterate directory
for file in os.listdir(dir_path):
    if file.endswith('.pgn'):
        file = file.replace('.pgn','')
        pgn_list.append(file)


def run_pgn(file_name):
    global my_board, move_num, moves, title
    try:
        # Open PGN file
        temp_game = chess.pgn.read_game(open(file_name))
        temp_board = chess.Board()
        moves = ['---']

        # Make moves array
        for move in temp_game.mainline_moves():
            a = temp_board.san(move)
            moves.append(a)
            temp_board.push(move)

        # reset Board
        my_board = chess.Board()
        move_num = 0
        title = file_name.replace('pgn/','')
        title = title.replace('.pgn', '')

    except:
        print('Wrong PGN')
        reset_game()


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

def refresh_board():
    global img
    temp_svg = chess.svg.board(my_board, size=BOARDSIZE, orientation=orientation)
    img = temp_svg.replace('"1000"', '"100%"')
    return render_template('index.html', board_svg=img,
                           game_title=title,
                           pgn_select_list=pgn_list)


@app.route('/process', methods=['POST', 'GET'])
def process():
    if request.method == "POST":
        ajax_data = request.get_json()
        print(ajax_data['file_name'])
        file_name_complete = 'pgn/' + ajax_data['file_name'] + '.pgn'
        print(file_name_complete)
        run_pgn(file_name_complete)

    results = {'processed': 'true'}
    return jsonify(results)


@app.route('/', methods=['GET', 'POST'])
def index():
    global move_num, my_board, orientation, img, pgn_list, title
    if request.is_json:
        # Request is a JSON Object
        if request.method == "GET":
            # GET = send data to DOM client
            return jsonify({'svg': img, 'title': title})

        if request.method == 'POST':
            # POST = receive data from DOM client
            print('POST')

            variable2 = json.loads(request.data)
            if 'button' in variable2.keys():
                print(variable2['button'])

                if variable2['button'] == 'mirror':
                    orientation = mirror_board(orientation)
                    temp_svg = chess.svg.board(my_board, size=BOARDSIZE, orientation=orientation)
                    img = temp_svg.replace('"1000"', '"100%"')

                if variable2['button'] == 'next':
                    move_num = next_move(move_num)
                    temp_svg = chess.svg.board(my_board, size=BOARDSIZE, orientation=orientation)
                    img = temp_svg.replace('"1000"', '"100%"')

                if variable2['button'] == 'prev':
                    move_num = prev_move(move_num)
                    temp_svg = chess.svg.board(my_board, size=BOARDSIZE, orientation=orientation)
                    img = temp_svg.replace('"1000"', '"100%"')

                if variable2['button'] == 'reset':
                    reset_game()
                    temp_svg = chess.svg.board(my_board, size=BOARDSIZE, orientation=orientation)
                    img = temp_svg.replace('"1000"', '"100%"')

            return jsonify({'svg': img, 'title': title})

    return render_template('index.html')


if __name__ == '__main__':
    if STAT_DEV:
        app.run(debug=True)
    else:
        from waitress import serve
        serve(app, host="0.0.0.0", port=8080)