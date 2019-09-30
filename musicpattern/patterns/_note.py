from ._base import PatternBase
from ._next import Next
from ._key_value import KeyValue
from ._crop import MaxLength


class NoteOns(KeyValue):

    def __init__(self, note_on, velocity=127, time=128):
        super().__init__({
            "note_on": note_on,
            "velocity": velocity,
            "time": time
        })

    def iterate(self):
        note = Next(self.data["note_on"], repeat_scalar=True)
        velocity = Next(self.data["velocity"], repeat_scalar=True)
        time = Next(self.data["time"], repeat_scalar=True)

        try:
            while True:
                cur_note = note.next()
                cur_velocity = velocity.next()
                cur_time = time.next()
                if not hasattr(cur_note, "__iter__"):
                    yield {
                        "note_on": cur_note,
                        "velocity": cur_velocity,
                        "time": cur_time,
                    }
                else:
                    cur_notes = list(cur_note)
                    for i, n in enumerate(cur_notes):
                        yield {
                            "note_on": n,
                            "velocity": cur_velocity,
                            "time": cur_time if i + 1 == len(cur_notes) else 0,
                        }

        except StopIteration:
            return

    def to_midi_track(self, max_length=128):
        import mido

        track = mido.MidiTrack()

        for i, n in enumerate(MaxLength(self, max_length)):
            track.append(mido.Message(
                "note_on",
                note=n["note_on"],
                velocity=n["velocity"],
                time=n["time"],
            ))

        return track

    def to_midi_file(self, max_length=128):
        import mido
        track = self.to_midi_track(max_length=max_length)
        midifile = mido.MidiFile()
        midifile.tracks.append(track)
        return midifile

