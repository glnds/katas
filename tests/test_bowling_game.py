import unittest

from bowling_game import Game


class TestBowlingGame(unittest.TestCase):
    def setUp(self):
        self.game = Game()

    def test_new_game(self):
        assert self.game.score == 0

    def test_normal_roll(self):
        self.game.roll(4)
        assert self.game.score == 4