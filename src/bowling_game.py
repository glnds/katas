
class Game(object):

    def __init__(self):
        super().__init__()
        self._score = 0
        self._current_frame = Frame()
        self._frames = [self._current_frame]

    def roll(self, fallen_pins):
        if self._current_frame.finished:
            self._current_frame = Frame()
            self._frames.append(self._current_frame)

        self._current_frame.roll(fallen_pins)

    @property
    def score(self):

        for index, frame in enumerate(self._frames):
            print(frame)
            if frame.is_strike:
                self._score += 10
                self._score += self._get_strike_bonus(index)
                print('s' + str(self._score))
            elif frame.is_spare:
                self._score += 10
                self._score += self._get_spare_bonus(index)
                print('p' + str(self._score))
            else:
                print(frame.sum)
                self._score += frame.sum
                print('n' + str(self._score))

        return self._score

    def _get_strike_bonus(self, index):
        bonus = 0
        if index + 1 < len(self._frames):
            bonus += self._frames[index + 1].sum
            if (self._frames[index + 1].is_strike and index + 2 < len(self._frames) and
                    self._frames[index + 2].first_roll):
                bonus += self._frames[index + 2].first_roll
        return bonus

    def _get_spare_bonus(self, index):
        bonus = 0
        if index + 1 < len(self._frames):
            bonus += self._frames[index + 1].first_roll
        return bonus


class Frame(object):

    def __init__(self):
        super().__init__()
        self._finished = False
        self._first_roll = None
        self._second_roll = None

    def roll(self, fallen_pins):
        if self._first_roll is None:
            self._first_roll = fallen_pins
            if fallen_pins == 10:
                self._finished = True
        else:
            self._second_roll = fallen_pins
            self._finished = True

    @property
    def first_roll(self):
        return self._first_roll

    @property
    def finished(self):
        return self._finished

    @property
    def sum(self):
        if self._first_roll is None:
            return 0
        score = self._first_roll
        if self._second_roll:
            score += self._second_roll
        return score

    @property
    def is_strike(self):
        return self._first_roll == 10

    @property
    def is_spare(self):
        return not self.is_strike and self.sum == 10

    def __str__(self):
        return "[%s, %s]" % (self._first_roll, self._second_roll)
