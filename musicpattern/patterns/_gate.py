from ._base import PatternBase
from ._next import Next
from ._key_value import KeyValue
from ._crop import MaxLength
from ._note import MidiMixin


class GateToMidi(MidiMixin, PatternBase):
    """
    Convert a sequence of gates like
        [1, 0, 0, 0, 1, 0, 0, 0]
    to midi notes.

    """

    def __init__(self, gate, note, velocity=64, ticks=128):
        self.gate = gate
        self.note = note
        self.velocity = velocity
        self.ticks = ticks
        super().__init__(gate=gate, note=note, velocity=velocity, ticks=ticks)

    def iterate(self):
        gates = Next(self.gate)
        notes = Next(self.note, repeat_scalar=True)
        velocities = Next(self.velocity, repeat_scalar=True)
        ticks_iter = Next(self.ticks, repeat_scalar=True)

        cur_time = 0
        last_note_time = 0

        try:
            while True:
                gate = gates.next()
                note = notes.next()
                vel = velocities.next()
                ticks = ticks_iter.next()

                if gate:
                    yield {
                        "note_on": note,
                        "velocity": vel,
                        "time": cur_time - last_note_time,
                    }
                    last_note_time = cur_time

                cur_time += ticks

        except StopIteration:
            return
