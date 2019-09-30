from ._base import PatternBase
from ._next import Next
from ._key_value import KeyValue
from ._crop import MaxLength


class NoteOns(KeyValue):

    def __init__(self, note_on, vel=127, time=128):
        self.note_on = None
        self.velocity = None
        self.time = None
        super().__init__({
            "note_on": note_on,
            "velocity": vel,
            "time": time
        })

    def to_mido_midi_track(self, max_length=128):
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

    def to_mido_midi_file(self, max_length=128):
        import mido
        track = self.to_mido_midi_track(max_length=max_length)
        midifile = mido.MidiFile()
        midifile.tracks.append(track)
        return midifile

