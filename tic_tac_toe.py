board = {
    'T1': ' ', 'T2': ' ', 'T3': ' ',
    'M1': ' ', 'M2': ' ', 'M3': ' ',
    'D1': ' ', 'D2': ' ', 'D3': ' '
}

# first player
player = 1
# to count movement of the player
total_move = 0
# ending the game frm each player that won
end_check = 0


def check():

    # movement of player one  and
    # for the horizontal (start)
    if board['T1'] == 'X' and board['T2'] == 'X' and board['T3'] == 'X':
        print('player one won !')
        return 1
    if board['M1'] == 'X' and board['M2'] == 'X' and board['M3'] == 'X':
        print('player one won !!')
        return 1
    if board['D1'] == 'X' and board['D2'] == 'X' and board['D3'] == 'X':
        print('player one won !!')
        return 1
# for horizontal (end)

# for diagonal (start)
    if board['T1'] == 'X' and board['M2'] == 'X' and board['D3'] == 'X':
        print('player one won !!')
        return 1
# for diagonal (end)

# for vertical (start)
    if board['T1'] == 'X' and board['M1'] == 'X' and board['D1'] == 'X':
        print('player one won !')
        return 1
    if board['T2'] == 'X' and board['M2'] == 'X' and board['D2'] == 'X':
        print('player one won !')
        return 1
    if board['T3'] == 'X' and board['M3'] == 'X' and board['D3'] == 'X':
        print('player one won !')
        return 1
# for vertical (end)

   # checking the movement of player two and
   # for the horizontal(start)
    if board['T1'] == 'O' and board['T2'] == 'O' and board['T3'] == 'O':
        print('player two won !')
        return 1
    if board['M1'] == '0' and board['M2'] == 'O' and board['M3'] == 'O':
        print('player two won !!')
        return 1
    if board['D1'] == 'O' and board['D2'] == 'O' and board['D3'] == 'O':
        print('player two won !!')
        return 1
    # for horizontal (end)

    # for diagonal (start)
    if board['T1'] == 'O' and board['M2'] == 'O' and board['D3'] == 'O':
        print('player two won !!')
        return 1
    # for diagonal (end)

    # for vertical (start)
    if board['T1'] == 'O' and board['M1'] == 'O' and board['D1'] == 'O':
        print('player two won !')
        return  1
    if board['T2'] == 'O' and board['M2'] == 'O' and board['D2'] == 'O':
        print('player two won !!')
        return 1
    if board['T3'] == 'O' and board['M3'] == 'O' and board['D3'] == 'O':
        print('player two won !!')
        return 1
    return 0
# for vertical (end)

print('T1|T2|T3')
print('- +- +-')
print('M1|M2|M3')
print('- +- +-')
print('D1|D2|D3')
print('************************')

while True:
    print(board['T1']+'|'+board['T2']+'|'+board['T3'])
    print('-+-+-')
    print(board['M1'] + '|' + board['M2'] + '|' + board['M3'])
    print('-+-+-')
    print(board['D1'] + '|' + board['D2'] + '|' + board['D3'])
    end_check = check()
# movement
    if total_move == 9 or end_check == 1:
        break
# players input
    while True:
        if player == 1:    # player choose
            p1_input = input('player one')
            if p1_input.upper() in board and board[p1_input.upper()] == ' ':
                board[p1_input.upper()] = 'X'
                player = 2
                break
            # on wrong input
            else:
                print('invalid input, please try again')
                continue
        else:
            p2_input = input('player two')
            if p2_input.upper() in board and board[p2_input.upper()] == ' ':
                board[p2_input.upper()] = 'O'
                player = 1
                break
            # on wrong input
            else:
                print('invalid input, please try again')
                continue


    total_move += 1
    print('*************************')
    print()