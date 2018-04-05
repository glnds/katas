class Game(object):

    def __init__(self):
        self._score = 0

    def roll(self, fallen_pins):
        self._score = fallen_pins

    @property
    def score(self):
        return self._score
