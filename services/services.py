from exceptions import exceptions
from repository.repo import Repo


class Services:
    def __init__(self):
        self.__game = Repo()

    def check_if_player_wins(self):
        """
        Checks if player wins
        :return: true/false
        """
        return self.__game.check_if_wins(1)

    def check_if_bot_wins(self):
        """
        Checks if bot wins
        :return: true/false
        """
        return self.__game.check_if_wins(2)

    def check_if_draw(self):
        """
        Checks if it's a draw
        :return: true/false
        """
        if (not self.check_if_player_wins()) and (not self.check_if_bot_wins()) and (self.__game.get_total_dots()==42):
            return True
        return False

    def game_not_over(self):
        """
        Checks if the game is not over
        :return: true/false
        """
        if (not self.check_if_player_wins()) and (not self.check_if_bot_wins()) and (self.__game.get_total_dots()<42):
            return True
        return False

    def bot_selects_choice(self):
        """
        Makes the bot select a column and places its move
        :return: -
        """
        self.__game.bot_move()

    def player_selects_choice(self,col):
        """
        Places the column given as a parameter for player
        :param col:
        :return: -
        """
        try:
            self.__game.player_move(col)
        except exceptions.CannotSelectThatColumn:
            raise exceptions.CannotSelectThatColumn
        else:
            pass

    def return_board(self):
        """
        Returns the board with all the moves until that moment
        :return: a matrix
        """
        return self.__game.return_current_board()


