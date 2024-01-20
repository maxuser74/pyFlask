moves = ['e4', 'e5', 'Nf3', 'Nc6', 'd4', 'exd4', 'Nxd4', 'Bc5']
pieces = {'N':'Knight', 'B':'Bishop', 'R':'Rook', 'Q':'Queen',
          'K':'King','a':'a', 'b':'b', 'c':'c', 'd':'d',
          'e':'e', 'f':'f', 'g':'g', 'h':'h'}
for move in moves:
    print(moves)
    len_move = len(move)
    san_expl = ''
    if len_move == 2:
        san_expl = move
    elif len_move == 3:
        san_expl = pieces[move[0]] + ' ' + move[1:3]
    elif len_move == 4:
        san_expl = pieces[move[0]]
        if move[1] == 'x':
            san_expl = san_expl + ' takes ' + move[2:4]

    print(move + ' = ' + san_expl)

