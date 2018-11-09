import unittest

from bowling_game import Game


class TestBowlingGame(unittest.TestCase):
    def setUp(self):
        self.game = Game()

    def throw_spare(self):
        self.game.roll(5)
        self.game.roll(5)

    def throw_strike(self):
        self.game.roll(10)
        self.game.roll(None)

    # def test_new_game(self):
    #     assert self.game.score == 0

    # def test_one_throw(self):
    #     self.game.roll(4)

    #     assert self.game.score == 4

    # def test_one_turn(self):
    #     self.game.roll(3)
    #     self.game.roll(2)

    #     assert self.game.score == 5

    # def test_throw_one_spare(self):
    #     self.throw_spare()
    #     self.game.roll(5)
    #     self.game.roll(4)

    #     assert self.game.score == 24

    # def test_throw_one_srike(self):
    #     self.throw_strike()
    #     self.game.roll(5)
    #     self.game.roll(4)

    #     assert self.game.score == 28

    # def test_throw_two_spares(self):
    #     self.throw_spare()
    #     self.throw_spare()
    #     self.game.roll(5)
    #     self.game.roll(4)

    #     assert self.game.score == 39

    def test_throw_two_strikes(self):
        self.throw_strike()
        self.throw_strike()
        self.game.roll(5)
        self.game.roll(4)

        assert self.game.score == 53

    # def test_gutter_game(self):
    #     for i in range(20):
    #         self.game.roll(0)

    #     assert self.game.score == 0

    def test_perfect_game(self):
        for i in range(10):
            self.throw_strike()

        assert self.game.score == 300
