validBoard = {  # starting board layout with shortnames
    '1a': 'brook1', '1b': 'bknight1', '1c': 'bbishop1', '1d': 'bqueen', '1e': 'bking', '1f':'bbishop2', '1g': 'bknight2', '1h': 'brook2',
    '2a': 'bpawn1', '2b': 'bpawn2', '2c': 'bpawn3', '2d': 'bpawn4', '2e': 'bpawn5', '2f': 'bpawn6', '2g': 'bpawn7', '2h': 'bpawn8',
    '3a': '   ', '3b': '   ', '3c': '   ', '3d': '   ', '3e': '   ', '3f': '   ', '3g': '   ', '3h': '   ',
    '4a': '   ', '4b': '   ', '4c': '   ', '4d': '   ', '4e': '   ', '4f': '   ', '4g': '   ', '4h': '   ',
    '5a': '   ', '5b': '   ', '5c': '   ', '5d': '   ', '5e': '   ', '5f': '   ', '5g': '   ', '5h': '   ',
    '6a': '   ', '6b': '   ', '6c': '   ', '6d': '   ', '6e': '   ', '6f': '   ', '6g': '   ', '6h': '   ',
    '7a': 'wpawn1', '7b': 'wpawn2', '7c': 'wpawn3', '7d': 'wpawn4', '7e': 'wpawn5', '7f': 'wpawn6', '7g': 'wpawn7', '7h': 'wpawn8',
    '8a': 'wrook1', '8b': 'wknight1', '8c': 'wbishop1', '8d': 'wking', '8e': 'wqueen', '8f': 'wbishop2', '8g': 'wknight2', '8h': 'wrook2'
    }
pieceIndex = { # verbose versions of shortnames
    'brook1': 'Black Rook', 'bknight1': 'Black Knight', 'bbishop1': 'Black Bishop', 'bqueen': 'Black Queen', 'bking': 'Black King',
    'bpawn1': 'Black Pawn', 'bpawn2': 'Black Pawn', 'bpawn3': 'Black Pawn', 'bpawn4': 'Black Pawn', 'bpawn5': 'Black Pawn', 'bpawn6': 'Black Pawn', 'bpawn7': 'Black Pawn', 'bpawn8': 'Black Pawn',
    'brook2': 'Black Rook', 'bknight2': 'Black Knight', 'bbishop2': 'Black Bishop',
    'wrook1': 'White Rook', 'wknight1': 'White Knight', 'wbishop1': 'White Bishop', 'wking': 'White King', 'wqueen': 'White Queen', 'wpawn': 'White Pawn',
    'wrook2': 'White Rook', 'wknight2': 'White Knight', 'wbishop2': 'White Bishop',
    'wpawn1': 'White Pawn', 'wpawn2': 'White Pawn', 'wpawn3': 'White Pawn', 'wpawn4': 'White Pawn', 'wpawn5': 'White Pawn', 'wpawn6': 'White Pawn', 'wpawn7': 'white Pawn', 'wpawn8': 'White Pawn'
    }
pieceSymbols = {  # symbols for shortnames
    'brook1': ' BR1 ', 'bknight1': ' BN1 ', 'bbishop1': ' BB1 ', 'bqueen': ' B Q ', 'bking': ' B K ',
    'bpawn1': ' BP1 ', 'bpawn2': ' BP2 ', 'bpawn3': ' BP3 ', 'bpawn4': ' BP4 ', 'bpawn5': ' BP5 ', 'bpawn6': ' BP6 ', 'bpawn7': ' BP7 ', 'bpawn8': ' BP8 ',
    'brook2': ' BR2 ', 'bknight2': ' BN2 ', 'bbishop2': ' BB2 ',
    'wrook1': ' WR1 ', 'wknight1': ' WN1 ', 'wbishop1': ' WB1 ', 'wking': ' W K ', 'wqueen': ' W Q ',
    'wrook2': ' WR2 ', 'wknight2': ' WK2 ', 'wbishop2': ' WB2 ',
    'wpawn1': ' WP1 ', 'wpawn2': ' WP2 ', 'wpawn3': ' WP3 ', 'wpawn4': ' WP4 ', 'wpawn5': ' WP5 ', 'wpawn6': ' WP6 ', 'wpawn7': ' WP7 ', 'wpawn8': ' WP8 ',
    '   ': '     '
    }

def printBoard():  # prints board with symbols standing in for pieces
    print('  ', ' a     b     c     d     e     f     g     h ')
    print(' |------------------------------------------------')
    print('1|' + pieceSymbols[str(validBoard['1a'])] + '|' + pieceSymbols[str(validBoard['1b'])] + '|' + pieceSymbols[str(validBoard['1c'])] + '|' + pieceSymbols[str(validBoard['1d'])] + '|' + pieceSymbols[str(validBoard['1e'])] + '|' + pieceSymbols[str(validBoard['1f'])] + '|' + pieceSymbols[str(validBoard['1g'])]+ '|' + pieceSymbols[str(validBoard['1h'])] + '|' )
    print(' |------------------------------------------------')
    print('2|' + pieceSymbols[str(validBoard['2a'])] + '|' + pieceSymbols[str(validBoard['2b'])] + '|' + pieceSymbols[str(validBoard['2c'])] + '|' + pieceSymbols[str(validBoard['2d'])] + '|' + pieceSymbols[str(validBoard['2e'])] + '|' + pieceSymbols[str(validBoard['2f'])] + '|' + pieceSymbols[str(validBoard['2g'])]+ '|' + pieceSymbols[str(validBoard['2h'])] + '|' )
    print(' |------------------------------------------------')
    print('3|' + pieceSymbols[str(validBoard['3a'])] + '|' + pieceSymbols[str(validBoard['3b'])] + '|' + pieceSymbols[str(validBoard['3c'])] + '|' + pieceSymbols[str(validBoard['3d'])] + '|' + pieceSymbols[str(validBoard['3e'])] + '|' + pieceSymbols[str(validBoard['3f'])] + '|' + pieceSymbols[str(validBoard['3g'])]+ '|' + pieceSymbols[str(validBoard['3h'])] + '|' )
    print(' |------------------------------------------------')
    print('4|' + pieceSymbols[str(validBoard['4a'])] + '|' + pieceSymbols[str(validBoard['4b'])] + '|' + pieceSymbols[str(validBoard['4c'])] + '|' + pieceSymbols[str(validBoard['4d'])] + '|' + pieceSymbols[str(validBoard['4e'])] + '|' + pieceSymbols[str(validBoard['4f'])] + '|' + pieceSymbols[str(validBoard['4g'])]+ '|' + pieceSymbols[str(validBoard['4h'])] + '|' )
    print(' |------------------------------------------------')
    print('5|' + pieceSymbols[str(validBoard['5a'])] + '|' + pieceSymbols[str(validBoard['5b'])] + '|' + pieceSymbols[str(validBoard['5c'])] + '|' + pieceSymbols[str(validBoard['5d'])] + '|' + pieceSymbols[str(validBoard['5e'])] + '|' + pieceSymbols[str(validBoard['5f'])] + '|' + pieceSymbols[str(validBoard['5g'])]+ '|' + pieceSymbols[str(validBoard['5h'])] + '|' )
    print(' |------------------------------------------------')
    print('6|' + pieceSymbols[str(validBoard['6a'])] + '|' + pieceSymbols[str(validBoard['6b'])] + '|' + pieceSymbols[str(validBoard['6c'])] + '|' + pieceSymbols[str(validBoard['6d'])] + '|' + pieceSymbols[str(validBoard['6e'])] + '|' + pieceSymbols[str(validBoard['6f'])] + '|' + pieceSymbols[str(validBoard['6g'])]+ '|' + pieceSymbols[str(validBoard['6h'])] + '|' )
    print(' |------------------------------------------------')
    print('7|' + pieceSymbols[str(validBoard['7a'])] + '|' + pieceSymbols[str(validBoard['7b'])] + '|' + pieceSymbols[str(validBoard['7c'])] + '|' + pieceSymbols[str(validBoard['7d'])] + '|' + pieceSymbols[str(validBoard['7e'])] + '|' + pieceSymbols[str(validBoard['7f'])] + '|' + pieceSymbols[str(validBoard['7g'])]+ '|' + pieceSymbols[str(validBoard['7h'])] + '|' )
    print(' |------------------------------------------------')
    print('8|' + pieceSymbols[str(validBoard['8a'])] + '|' + pieceSymbols[str(validBoard['8b'])] + '|' + pieceSymbols[str(validBoard['8c'])] + '|' + pieceSymbols[str(validBoard['8d'])] + '|' + pieceSymbols[str(validBoard['8e'])] + '|' + pieceSymbols[str(validBoard['8f'])] + '|' + pieceSymbols[str(validBoard['8g'])]+ '|' + pieceSymbols[str(validBoard['8h'])] + '|' )
    print(' |------------------------------------------------')

def isValidChessboard(userPiece):
    pieces = validBoard.values()
    spaces = validBoard.keys()
    if userPiece in pieces:
        print('That is a piece')
        print('Move the ' + pieceIndex[userPiece] + ' to what position?')
        userMove = input()
        userMoveFrom = list(validBoard.keys())[list(validBoard.values()).index(userPiece)]
        print(userMoveFrom)
        if userMove in spaces:
            print('valid board location')
            if validBoard[userMove] == '   ':
                print('valid move!')
                validBoard[userMove] = userPiece
                validBoard[userMoveFrom] = '   '
            else:
                print('there is a piece there already')
        else:
            print('not a valid board location')
    else:
        print('not a piece')




while True:
    print('what piece will you move?')
    userPieceIn = input()
    isValidChessboard(userPieceIn)
    printBoard()
