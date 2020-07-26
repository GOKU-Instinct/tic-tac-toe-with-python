#print('I must do it.', 'Lets go Ultra Instinct')

def printBoard(bT, a):
    if(bT == 1):
        print('[', a[0][0], '][', a[0][1], '][', a[0][2], ']', sep='')
        print('[', a[1][0], '][', a[1][1], '][', a[1][2], ']', sep='')
        print('[', a[2][0], '][', a[2][1], '][', a[2][2], ']', sep='')
        print('')

    if(bT == 2):
        print(' ', a[0][0], ' | ', a[0][1], ' | ', a[0][2], ' ', sep='')
        print('---+---+---')
        print(' ', a[1][0], ' | ', a[1][1], ' | ', a[1][2], ' ', sep='')
        print('---+---+---')
        print(' ', a[2][0], ' | ', a[2][1], ' | ', a[2][2], ' ', sep='')
        print('')

def selectBoard(a):
    print('Board 1 :')
    printBoard(1, a)
    print('Board 2 :')
    printBoard(2, a)
    x = 50
    while x > 2:
        x = int(input('To select a board, enter the board no.: '))
        if x > 2:
            print('Invalid input. Try again.')
    return x

def isBoardFull(a):
    for i in range(3):
        for j in range(3):
            if a[i][j]==' ':
                return False
    return True

def isWin(ch, a):
    x = ' '
    if(ch == 0):
        x = 'X'
    else:
        x = 'O'
    if a[0][0] == x and a[0][0] == a[0][1] and a[0][1] == a[0][2]:
        return True
    if a[1][0] == x and a[1][0] == a[1][1] and a[1][1] == a[1][2]:
        return True
    if a[2][0] == x and a[2][0] == a[2][1] and a[2][1] == a[2][2]:
        return True
    if a[0][0] == x and a[0][0] == a[1][0] and a[1][0] == a[2][0]:
        return True
    if a[0][1] == x and a[0][1] == a[1][1] and a[1][1] == a[2][1]:
        return True
    if a[0][2] == x and a[0][2] == a[1][2] and a[1][2] == a[2][2]:
        return True
    if a[0][0] == x and a[0][0] == a[1][1] and a[1][1] == a[2][2]:
        return True
    if a[2][0] == x and a[2][0] == a[1][1] and a[1][1] == a[0][2]:
        return True
    return False

def game():
    a = [[' ', ' ', ' '],
         [' ', ' ', ' '],
         [' ', ' ', ' ']]

    boardType = selectBoard(a)

    print('')
    p1 = input('Enter name of 1st Player: ')
    p2 = input('Enter name of 2nd Player: ')
    print('')
    print('Instructions: -')
    print('\t', p1, 'will use X')
    print('\t', p2, 'will use O')
    print('\t', 'You will have to give coordinates for your move in each turn (0 based index and in one line)')
    print('\t', 'The player who will be able to put their symbol in a line(horizontally or vertically or diagonally) will win the game.')
    print('\t', p1, 'will start the game.\n')

    chance = 0
    draw = True
    while isBoardFull(a) == False:
        if chance == 0:
            print(p1, "'s turn, ", sep='', end='')
            turn = input("Enter the coordinates for your move: ")
            turn = turn.split()
            try:
                x = int(turn[0])
                y = int(turn[1])
                if x>2 or x<0 or y>2 or y<0:
                    print('Invalid coordinates. Enter again')
                    continue
            except:
                print('Invalid coordinates. Enter again')
                continue
            if a[x][y] != ' ':
                print('This place is already occupied. Please try again.')
                continue
            else:
                a[x][y] = 'X'
        if chance == 1:
            print(p2, "'s turn, ", sep='', end='')
            turn = input("Enter the coordinates for your move: ")
            turn = turn.split()
            try:
                x = int(turn[0])
                y = int(turn[1])
                if x>2 or x<0 or y>2 or y<0:
                    print('Invalid coordinates. Enter again')
                    continue
            except:
                print('Invalid coordinates. Enter again')
                continue
            if a[x][y] != ' ':
                print('This place is already occupied. Please try again.')
                continue
            else:
                a[x][y] = 'O'
        printBoard(boardType, a)
        if isWin(chance, a):
            if chance == 0:
                print(p1, 'won the game.')
            else:
                print(p2, 'won the game.')
            draw = False
            break
        chance = (chance + 1) % 2

    if draw == True:
        print('This game is a tie. Nobody won.')

def newGame():
    startGame = True
    while startGame:
        game()
        inp = input('If you want to play a new game, press "Y", else enter anything you want, Enter your choice: ')
        print('')
        if inp != 'y' and inp != 'Y':
            startGame = False

newGame()
