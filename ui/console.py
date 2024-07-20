import copy

from texttable import Texttable

from exceptions import exceptions
from services.services import Services


class Console:
    def __init__(self):
        self.__game = Services()

    def start_game(self):
        while self.__game.game_not_over():
            self.player_moves()
            self.bot_moves()

    def check_for_winner(self):
        if self.__game.check_if_player_wins():
            print("Player wins!")
            exit()
        elif self.__game.check_if_bot_wins():
            print("Bot wins!")
            exit()
        elif self.__game.check_if_draw():
            print("Draw!")
            exit()

    def print_board(self):
        l = copy.deepcopy(self.__game.return_board())
        table = Texttable()
        print()
        t = [['0', '1', '2', '3', '4', '5', '6']]
        for i in range(6):
            row = []
            for j in range(7):
                if l[i][j] == 1:
                    row.append('X')
                elif l[i][j] == 2:
                    row.append('O')
                else:
                    row.append(' ')
            t.append(row)
        table.add_rows(t)
        print(table.draw())
        print()


    def insert_choice_player(self, col):
        try:
            self.__game.player_selects_choice(col)
        except exceptions.CannotSelectThatColumn:
            print("Can't insert here!")
            col = int(input("> "))
            self.insert_choice_player(col)
        else:
            pass

    def player_moves(self):
        col = int(input("> "))
        self.insert_choice_player(col)
        self.print_board()
        self.check_for_winner()

    def bot_moves(self):
        self.__game.bot_selects_choice()
        self.print_board()
        self.check_for_winner()