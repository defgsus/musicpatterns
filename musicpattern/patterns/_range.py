from ._base import PatternBase
from ._next import Next


class Range(PatternBase):

    def __init__(self, end, offset=1):
        self.end = None
        self.offset = None
        super().__init__(end=end, offset=offset)

    def iterate(self):
        try:
            end = Next(self.end)
            offset = Next(self.offset)

            value = 0
            while True:
                cur_end = end.next()
                cur_offset = offset.next()
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
