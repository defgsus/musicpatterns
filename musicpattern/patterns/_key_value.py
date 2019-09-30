from ._base import PatternBase
from ._next import Next


class KeyValue(PatternBase):

    def __init__(self, data):
        self.data = None
        super().__init__(data=data)

    def iterate(self):
        data = {
            key: Next(value, repeat_scalar=True)
            for key, value in self.data.items()
        }

        try:
            while True:
                yield {
                    key: value.next()
                    for key, value in data.items()
                }

        except StopIteration:
            return
