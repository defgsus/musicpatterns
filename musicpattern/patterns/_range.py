from ._base import PatternBase
from ._next import Next


class Range(PatternBase):

    def __init__(self, end=None, step=1):
        self.end = None
        self.step = None
        super().__init__(end=end, step=step)

    def iterate(self):
        try:
            if self.end is None:
                step = Next(self.step, repeat_scalar=True)

                value = 0
                while True:
                    cur_offset = step.next()
                    yield value
                    value += cur_offset

            else:
                end = Next(self.end, repeat_scalar=True)
                step = Next(self.step, repeat_scalar=True)

                value = 0
                while True:
                    cur_end = end.next()
                    cur_offset = step.next()
                    if cur_offset > 0:
                        if value >= cur_end:
                            return
                    elif cur_offset < 0:
                        if value <= cur_end:
                            return
                    else:
                        # TODO: what to do on offset==0 ?
                        pass

                    yield value
                    value += cur_offset

        except StopIteration:
            pass
