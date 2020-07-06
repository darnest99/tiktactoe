board = [0, 0, 0, 0, 0, 0, 0, 0, 0]
combos = []
won = False


def player1(board):
    print('Go 1!')
    try:
        move = int(input('Choose your position via the number pad.')) - 1
        if move > 8:
            print('Press a valid key.')
            player1(board)
        elif board[move] == 0:
            board[move] = 1
            return board
    except:
        print('Press a valid key.')
        player1(board)


def player2(board):
    print('Go 2!')
    try:
        move = int(input('Choose your position via the number pad.')) - 1
        if move > 8:
            print('Press a valid key.')
            player2(board)
        elif board[move] == 0:
            board[move] = 2
            return board
    except:
        print('Press a valid key.')
        player2(board)


while won is False:
    combos = [board[:3], board[3:6], board[6:], [board[0], board[3], board[6]], [board[1], board[4], board[7]],
              [board[2], board[5], board[8]], [board[0], board[4], board[8]], [board[2], board[4], board[6]]]
    ones = [i for i in combos if i == [1, 1, 1]]
    twos = [i for i in combos if i == [2, 2, 2]]
    visual = [''.join(str(board[:3])), ''.join(str(board[3:6])), ''.join(str(board[6:]))]
    print(visual[2])
    print(visual[1])
    print(visual[0])
    if len(ones) == 1:
        print('1 won!')
        won = True
    elif len(twos) == 1:
        print('2 won!')
        won = True
    else:
        if board.count(1) == board.count(2):
            player1(board)
        else:
            player2(board)
