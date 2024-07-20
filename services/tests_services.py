from unittest import TestCase

from .services import Services

def test_all_fn_services():
    t = ServicesTests()
    t.setUp()
    t.test_check_if_player_wins()
    t.setUp()
    t.test_player_selects_choice()
    t.setUp()
    t.test_game_not_over()

class ServicesTests(TestCase):
    def setUp(self):
        self.__object = Services()
        self.__object.player_selects_choice(2)
        self.__object.player_selects_choice(3)

    def test_check_if_player_wins(self):
        self.__object.player_selects_choice(4)
        self.assertEqual(self.__object.check_if_player_wins(), False, "Player didn't win")
        self.__object.player_selects_choice(5)
        self.assertEqual(self.__object.check_if_player_wins(), True, "Player wins")

    def test_player_selects_choice(self):
        self.__object.player_selects_choice(4)
        self.assertEqual(self.__object.return_board(), [[0, 0, 0, 0, 0, 0, 0],
                                                        [0, 0, 0, 0, 0, 0, 0],
                                                        [0, 0, 0, 0, 0, 0, 0],
                                                        [0, 0, 0, 0, 0, 0, 0],
                                                        [0, 0, 0, 0, 0, 0, 0],
                                                        [0, 0, 1, 1, 1, 0, 0]], "...")
        self.__object.player_selects_choice(5)
        self.assertEqual(self.__object.return_board(), [[0, 0, 0, 0, 0, 0, 0],
                                                        [0, 0, 0, 0, 0, 0, 0],
                                                        [0, 0, 0, 0, 0, 0, 0],
                                                        [0, 0, 0, 0, 0, 0, 0],
                                                        [0, 0, 0, 0, 0, 0, 0],
                                                        [0, 0, 1, 1, 1, 1, 0]], "...")

    def test_game_not_over(self):
        self.__object.player_selects_choice(4)
        self.assertEqual(self.__object.game_not_over(), True, "Game not over")
        self.__object.player_selects_choice(5)
        self.assertEqual(self.__object.game_not_over(), False, "Game over")