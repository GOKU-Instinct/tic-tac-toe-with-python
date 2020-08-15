#print('I must do it.', 'Lets go Ultra Instinct')

import time
import math
import random

class Player():
    def __init__(self, letter):
        self.letter = letter

    def get_move(self, game):
        pass


class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            square = input(self.letter + '\'s turn. Input move (1-9): ')
            try:
                val = int(square)
                val-=1
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True
            except ValueError:
                print('Invalid square. Try again.')
        return val


class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        square = random.choice(game.available_moves())
        return square


class SmartComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        if len(game.available_moves()) == 9:
            square = random.choice(game.available_moves())
        else:
            square = self.minimax(game, self.letter)['position']
        return square

    def minimax(self, state, player):
        max_player = self.letter  # yourself
        other_player = 'O' if player == 'X' else 'X'

        # first we want to check if the previous move is a winner
        if state.current_winner == other_player:
            return {'position': None, 'score': 1 * (state.num_empty_squares() + 1) if other_player == max_player else -1 * (
                        state.num_empty_squares() + 1)}
        elif not state.empty_squares():
            return {'position': None, 'score': 0}

        if player == max_player:
            best = {'position': None, 'score': -math.inf}  # each score should maximize
        else:
            best = {'position': None, 'score': math.inf}  # each score should minimize
        for possible_move in state.available_moves():
            state.make_move(possible_move, player)
            sim_score = self.minimax(state, other_player)  # simulate a game after making that move

            # undo move
            state.board[possible_move] = ' '
            state.current_winner = None
            sim_score['position'] = possible_move  # this represents the move optimal next move

            if player == max_player:  # X is max player
                if sim_score['score'] > best['score']:
                    best = sim_score
            else:
                if sim_score['score'] < best['score']:
                    best = sim_score
        return best



class TicTacToe():
    def __init__(self):
        self.board = self.make_board()
        self.boardType = 0
        self.current_winner = None

    @staticmethod
    def make_board():
        return [' ' for _ in range(9)]

    def print_board(self, x):

        if x==1:
            print('[', self.board[0], ']', '[', self.board[1], ']', '[', self.board[2], ']', sep='')
            print('[', self.board[3], ']', '[', self.board[4], ']', '[', self.board[5], ']', sep='')
            print('[', self.board[6], ']', '[', self.board[7], ']', '[', self.board[8], ']', sep='')
            print()

        if x==2:
            print('{', self.board[0], '}', '{', self.board[1], '}', '{', self.board[2], '}', sep='')
            print('{', self.board[3], '}', '{', self.board[4], '}', '{', self.board[5], '}', sep='')
            print('{', self.board[6], '}', '{', self.board[7], '}', '{', self.board[8], '}', sep='')
            print()

        if x==3:
            print(' ', self.board[0], ' | ', self.board[1], ' | ', self.board[2], ' ', sep='')
            print('---+---+---')
            print(' ', self.board[3], ' | ', self.board[4], ' | ', self.board[5], ' ', sep='')
            print('---+---+---')
            print(' ', self.board[6], ' | ', self.board[7], ' | ', self.board[8], ' ', sep='')
            print()

        #for row in [self.board[i*3:(i+1) * 3] for i in range(3)]:
            #print('| ' + ' | '.join(row) + ' |')

    def boardSelect(self):
        print('Board 1. ')
        self.print_board(1)
        print('Board 2. ')
        self.print_board(2)
        print('Board 3. ')
        self.print_board(3)
        print('Which board do you want to select?')
        while self.boardType <= 0 or self.boardType > 3:
            inp = input('Enter your choice(1/2/3): ' )
            try:
                inp = int(inp)
                self.boardType = inp
                if inp > 3 or inp < 1:
                    print('Invalid board choice!')
                    continue
            except:
                print('Invalid board choice!!! Try again.')
                continue
        print('So, you have selected the following baord to play.')
        print('Use the following reference position numbers when asked to input the position to play.')
        for i in range(0,9):
            self.board[i]=str(i+1)
        self.print_board(self.boardType)
        for i in range(0,9):
            self.board[i]=' '

    def make_move(self, square, letter):
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, square, letter):
        # check the row
        row_ind = math.floor(square / 3)
        row = self.board[row_ind*3:(row_ind+1)*3]
        # print('row', row)
        if all([s == letter for s in row]):
            return True
        col_ind = square % 3
        column = [self.board[col_ind+i*3] for i in range(3)]
        # print('col', column)
        if all([s == letter for s in column]):
            return True
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            # print('diag1', diagonal1)
            if all([s == letter for s in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            # print('diag2', diagonal2)
            if all([s == letter for s in diagonal2]):
                return True
        return False

    def empty_squares(self):
        return ' ' in self.board

    def num_empty_squares(self):
        return self.board.count(' ')

    def available_moves(self):
        return [i for i, x in enumerate(self.board) if x == " "]


def play(game, x_player, o_player, print_game=True):

    letter = 'X'
    while game.empty_squares():
        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)
        if game.make_move(square, letter):

            if print_game:
                print(letter + ' makes a move to square {}'.format(square+1))
                game.print_board(t.boardType)
                print('')

            if game.current_winner:
                if print_game:
                    print(letter + ' wins!')
                return letter  # ends the loop and exits the game
            letter = 'O' if letter == 'X' else 'X'  # switches player

        time.sleep(.2)

    if print_game:
        print('It\'s a tie! Well played.....but no winner is there.')



if __name__ == '__main__':

    startGame = True
    while startGame:
        print("Note: You can't beat the computer here :)")
        print('Select one of theh option from below to start.')
        print('\tPress 1 to play with computer(you vs computer)')
        print('\tPress 2 to play with computer(computer vs you)')
        print('\tPress 3 to play with your friend(1 vs 1)')
        try:
            ch = int(input('\tEnter Your Choice: '))
            if ch == 1:
                x_player = HumanPlayer('X')
                o_player = SmartComputerPlayer('O')
            elif ch == 2:
                x_player = SmartComputerPlayer('X')
                o_player = HumanPlayer('O')
            elif ch == 3:
                x_player = HumanPlayer('X')
                o_player = HumanPlayer('O')
            else:
                print('Not a valid Choice. Try Again.')
                continue
        except:
            print('Invalid Choice. Try Again.')
            continue
        t = TicTacToe()
        t.boardSelect()
        play(t, x_player, o_player, print_game=True)
        inp = input('If you want to play a new game, press "Y", else enter anything you want, Enter your choice: ')
        print('')
        if inp != 'y' and inp != 'Y':
            startGame = False