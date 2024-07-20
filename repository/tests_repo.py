from unittest import TestCase

from .repo import Repo

def test_all_fn_repo():
    t = RepoTests()
    t.setUp()
    t.test_get_total_dots()
    t.setUp()
    t.test_add_move_at_position()
    t.setUp()
    t.test_check_if_wins()
    t.setUp()
    t.test_partial_score_for_bot()
    t.setUp()
    t.test_player_move()
    t.setUp()
    t.test_bot_move()

class RepoTests(TestCase):
    def setUp(self):
        self.__object = Repo()
        self.__object.add_move_at_position(2, 1)
        self.__object.add_move_at_position(2, 2)
        self.__object.add_move_at_position(3, 1)
        self.__object.add_move_at_position(1, 2)

    def test_get_total_dots(self):
        self.assertEqual(self.__object.get_total_dots(), 4, "4 total moves")
        self.__object.add_move_at_position(4, 1)
        self.assertEqual(self.__object.get_total_dots(), 5, "5 total moves")
        self.__object.add_move_at_position(5, 2)
        self.assertEqual(self.__object.get_total_dots(), 6, "6 total moves")

    def test_add_move_at_position(self):
        self.__object.add_move_at_position(4, 1)
        self.assertEqual(self.__object.return_current_board(), [[0, 0, 0, 0, 0, 0, 0],
                                                                [0, 0, 0, 0, 0, 0, 0],
                                                                [0, 0, 0, 0, 0, 0, 0],
                                                                [0, 0, 0, 0, 0, 0, 0],
                                                                [0, 0, 2, 0, 0, 0, 0],
                                                                [0, 2, 1, 1, 1, 0, 0]], "...")
        self.__object.add_move_at_position(5, 2)
        self.assertEqual(self.__object.return_current_board(), [[0, 0, 0, 0, 0, 0, 0],
                                                                [0, 0, 0, 0, 0, 0, 0],
                                                                [0, 0, 0, 0, 0, 0, 0],
                                                                [0, 0, 0, 0, 0, 0, 0],
                                                                [0, 0, 2, 0, 0, 0, 0],
                                                                [0, 2, 1, 1, 1, 2, 0]], "...")

    def test_check_if_wins(self):
        self.assertEqual(self.__object.check_if_wins(1), False, "Player didn't win")
        self.assertEqual(self.__object.check_if_wins(2), False, "Bot didn't win")
        self.__object.add_move_at_position(4, 1)
        self.__object.add_move_at_position(3, 2)
        self.__object.add_move_at_position(5, 1)
        self.assertEqual(self.__object.check_if_wins(1), True, "Player wins")
        self.assertEqual(self.__object.check_if_wins(2), False, "Bot didn't win")

    def test_partial_score_for_bot(self):
        self.assertEqual(self.__object.partial_score_for_bot(), 5, "...")
        self.__object.add_move_at_position(3, 1)
        self.__object.add_move_at_position(3, 2)
        self.assertEqual(self.__object.partial_score_for_bot(), 15, "...")
        self.__object.add_move_at_position(4, 1)
        self.assertEqual(self.__object.partial_score_for_bot(), 7, "...")

    def test_player_move(self):
        self.__object.player_move(4)
        self.assertEqual(self.__object.return_current_board(), [[0, 0, 0, 0, 0, 0, 0],
                                                                [0, 0, 0, 0, 0, 0, 0],
                                                                [0, 0, 0, 0, 0, 0, 0],
                                                                [0, 0, 0, 0, 0, 0, 0],
                                                                [0, 0, 2, 0, 0, 0, 0],
                                                                [0, 2, 1, 1, 1, 0, 0]], "...")
        self.__object.player_move(5)
        self.assertEqual(self.__object.return_current_board(), [[0, 0, 0, 0, 0, 0, 0],
                                                                [0, 0, 0, 0, 0, 0, 0],
                                                                [0, 0, 0, 0, 0, 0, 0],
                                                                [0, 0, 0, 0, 0, 0, 0],
                                                                [0, 0, 2, 0, 0, 0, 0],
                                                                [0, 2, 1, 1, 1, 1, 0]], "...")

    def test_bot_move(self):
        nr = self.__object.get_total_dots()
        self.__object.bot_move()
        self.assertEqual(self.__object.get_total_dots(), nr + 1, "Bot has selected a column")
        self.__object.bot_move()
        self.assertEqual(self.__object.get_total_dots(), nr + 2, "Bot has selected another column")