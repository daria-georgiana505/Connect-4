import copy
import math
import random

from exceptions import exceptions


class Repo():
    def __init__(self):
        self.__matrix = [[0 for i in range(7)] for j in range(6)]
        self.__nr_dots_on_columns = [0,0,0,0,0,0,0]

    def get_total_dots(self):
        """
        Returns the total number of moves until that moment
        :return: an integer ( <= 42)
        """
        s = 0
        for i in range(7):
            s += self.__nr_dots_on_columns[i]
        return s

    def add_move_at_position(self, column, player_move):
        """
        Places the move of player/bot at a given column
        :param column: the given column to place the move (integer, 0 <= column <= 6)
        :param player_move: 1 - for player, 2 - for bot
        :return: -
        """
        row = 6-self.__nr_dots_on_columns[column]-1
        if self.__nr_dots_on_columns[column] < 6 and column < 7:
            if self.__matrix[row][column] == 0 and (row == 5 or self.__matrix[row + 1][column] != 0):
                self.__matrix[row][column] += player_move
                self.__nr_dots_on_columns[column] += 1
            else:
                raise IndexError
        else:
            raise IndexError

    def get_random_valid_position(self,list_of_choices):
        """
        Returns a random column
        :param list_of_choices:  a list with all the available columns
        :return: a random value from the given list
        """
        r = random.choices(list_of_choices,k=1)
        list_of_choices.remove(r[0])
        return r[0]

    def check_if_wins(self,player_move):
        """
        Checks if player/bot wins
        :param player_move: 1 - for player, 2 - for bot
        :return: true/false
        """
        for i in range(6):
            for j in range(7-3):
                if self.__matrix[i][j]==player_move and self.__matrix[i][j+1]==player_move and self.__matrix[i][j+2]==player_move and self.__matrix[i][j+3]==player_move:
                    return True
        for i in range(6-3):
            for j in range(7):
                if self.__matrix[i][j]==player_move and self.__matrix[i+1][j]==player_move and self.__matrix[i+2][j]==player_move and self.__matrix[i+3][j]==player_move:
                    return True
        for i in range(6-3):
            for j in range(7-3):
                if self.__matrix[i][j]==player_move and self.__matrix[i+1][j+1]==player_move and self.__matrix[i+2][j+2]==player_move and self.__matrix[i+3][j+3]==player_move:
                    return True
        for i in range(3, 6):
            for j in range(7-3):
                if self.__matrix[i][j]==player_move and self.__matrix[i-1][j+1]==player_move and self.__matrix[i-2][j+2]==player_move and self.__matrix[i-3][j+3]==player_move:
                    return True
        return False


    def partial_score_for_bot(self):
        """
        Returns a score for bot's moves until this moment, based on the number of consecutive circles on the row columns and
        diagonals
        :return: the score (integer)
        """
        score = 0
        for i in range(6):
            for j in range(7-3):
                nr_consec_dots_bot = 0
                nr_consec_dots_player = 0
                nr_consec_dots_empty = 0
                for k in range(4):
                    if self.__matrix[i][j+k]==2:
                        nr_consec_dots_bot += 1
                    elif self.__matrix[i][j+k]==1:
                        nr_consec_dots_player += 1
                    else:
                        nr_consec_dots_empty += 1
                if nr_consec_dots_bot == 4:
                    score += 10000
                elif nr_consec_dots_bot == 3 and nr_consec_dots_empty == 1:
                    score += 10
                elif nr_consec_dots_bot == 2 and nr_consec_dots_empty == 2:
                    score += 5
                if nr_consec_dots_player == 3 and nr_consec_dots_empty == 1:
                    score -= 8

        for i in range(6-3):
            for j in range(7):
                nr_consec_dots_bot = 0
                nr_consec_dots_player = 0
                nr_consec_dots_empty = 0
                for k in range(4):
                    if self.__matrix[i+k][j] == 2:
                        nr_consec_dots_bot += 1
                    elif self.__matrix[i+k][j] == 1:
                        nr_consec_dots_player += 1
                    else:
                        nr_consec_dots_empty += 1
                if nr_consec_dots_bot == 4:
                    score += 10000
                elif nr_consec_dots_bot == 3 and nr_consec_dots_empty == 1:
                    score += 10
                elif nr_consec_dots_bot == 2 and nr_consec_dots_empty == 2:
                    score += 5
                if nr_consec_dots_player == 3 and nr_consec_dots_empty == 1:
                    score -= 8

        for i in range(6-3):
            for j in range(7-3):
                nr_consec_dots_bot = 0
                nr_consec_dots_player = 0
                nr_consec_dots_empty = 0
                for k in range(4):
                    if self.__matrix[i+k][j + k] == 2:
                        nr_consec_dots_bot += 1
                    elif self.__matrix[i+k][j + k] == 1:
                        nr_consec_dots_player += 1
                    else:
                        nr_consec_dots_empty += 1
                if nr_consec_dots_bot == 4:
                    score += 10000
                elif nr_consec_dots_bot == 3 and nr_consec_dots_empty == 1:
                    score += 10
                elif nr_consec_dots_bot == 2 and nr_consec_dots_empty == 2:
                    score += 5
                if nr_consec_dots_player == 3 and nr_consec_dots_empty == 1:
                    score -= 8

        for i in range(3, 6):
            for j in range(7-3):
                nr_consec_dots_bot = 0
                nr_consec_dots_player = 0
                nr_consec_dots_empty = 0
                for k in range(4):
                    if self.__matrix[i-k][j + k] == 2:
                        nr_consec_dots_bot += 1
                    elif self.__matrix[i-k][j + k] == 1:
                        nr_consec_dots_player += 1
                    else:
                        nr_consec_dots_empty += 1
                if nr_consec_dots_bot == 4:
                    score += 10000
                elif nr_consec_dots_bot == 3 and nr_consec_dots_empty == 1:
                    score += 10
                elif nr_consec_dots_bot == 2 and nr_consec_dots_empty == 2:
                    score += 5
                if nr_consec_dots_player == 3 and nr_consec_dots_empty == 1:
                    score -= 8
        return score

    def minimax(self, depth, alpha, beta, isMaximising, nr_steps):
        """
        The minimax algorithm (alpha-beta pruning)
        :param depth: depth
        :param alpha: alpha
        :param beta: beta
        :param isMaximising: True/False
        :param nr_steps: nr of steps until a solution is reached
        :return: nr of steps & the best score
        """
        player_wins = self.check_if_wins(1)
        bot_wins = self.check_if_wins(2)
        if depth == 0 or player_wins or bot_wins or ((not player_wins) and (not bot_wins) and self.get_total_dots() == 42):  # if depth == 0 or player_wins or bot_wins or (not player_wins and not bot_wins and self.get_total_dots()==42):
            if player_wins or bot_wins or ((not player_wins) and (not bot_wins) and self.get_total_dots() == 42):
                if bot_wins:
                    return nr_steps, 1000000000
                elif player_wins:
                    return nr_steps, -1000000000
                elif (not player_wins) and (not bot_wins) and self.get_total_dots() == 42:
                    return nr_steps, 0
            else:
                return nr_steps, self.partial_score_for_bot()
        if isMaximising:
            bestScore = -math.inf
            q = -1

            list_of_columns = [0, 1, 2, 3, 4, 5, 6]
            for k in range(7):
                j = self.get_random_valid_position(list_of_columns)
                i = 6-self.__nr_dots_on_columns[j]-1
                try:
                    self.add_move_at_position(j, 2)
                    q, score = self.minimax(depth - 1, alpha, beta, False,nr_steps+1)
                    self.__matrix[i][j] = 0
                    self.__nr_dots_on_columns[j] -= 1
                    if score > bestScore:
                        bestScore = score
                    alpha = max(alpha, bestScore)
                    if alpha >= beta:
                        break
                except IndexError:
                    pass
                else:
                    pass
            return q, bestScore

        else:
            bestScore = math.inf
            q = -1

            list_of_columns = [0, 1, 2, 3, 4, 5, 6]
            for k in range(7):
                j = self.get_random_valid_position(list_of_columns)
                i = 6 - self.__nr_dots_on_columns[j] - 1

                try:
                    self.add_move_at_position(j, 1)
                    q, score = self.minimax(depth - 1, alpha, beta, True, nr_steps+1)
                    self.__matrix[i][j] = 0
                    self.__nr_dots_on_columns[j] -= 1
                    if score < bestScore:
                        bestScore = score
                    beta = min(beta, bestScore)
                    if alpha >= beta:
                        break
                except IndexError:
                    pass
                else:
                    pass
            return q, bestScore # return bestScore

    def bot_move(self):
        """
        Bot places its move
        :return: -
        """
        bestScore = -math.inf
        bestMoveY = 3
        bestNrSteps = 5

        list_of_columns = [0,1,2,3,4,5,6]
        for k in range(7):
            j = self.get_random_valid_position(list_of_columns)
            i = 6 - self.__nr_dots_on_columns[j] - 1

            try:
                self.add_move_at_position(j,2)
                # # score = self.minimax(42, False)
                nr_steps, score = self.minimax(4, -math.inf, math.inf, False, 0)

                self.__matrix[i][j] = 0
                self.__nr_dots_on_columns[j] -= 1
                if score > bestScore:
                    bestScore = score
                    bestMoveY = j
                    bestNrSteps = nr_steps
                elif score == bestScore and score >= 1000000000 and nr_steps < bestNrSteps:
                    bestMoveY = j
                    bestNrSteps = nr_steps
                elif score == bestScore and score <= -100000000 and nr_steps > bestNrSteps:
                    bestMoveY = j
                    bestNrSteps = nr_steps
            except IndexError:
                pass
            else:
                pass
        self.add_move_at_position(bestMoveY,2)

    def player_move(self,col):
        """
        Player places their move at the given column
        :param col: a given column (integer, 0 <= col <= 6)
        :return: -
        """
        try:
            self.add_move_at_position(col,1)
        except IndexError:
            raise exceptions.CannotSelectThatColumn
        else:
            pass

    def return_current_board(self):
        """
        Returns the board with all the moves until that moment
        :return: a matrix
        """
        return self.__matrix
