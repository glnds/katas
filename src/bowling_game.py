class Game(object):

    def roll(self, fallen_pins):
        self._score = fallen_pins

    @property
    def score(self):
        return self._score
