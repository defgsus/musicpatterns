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

    def to_string(self, max_length=128):
        notes_by_time = dict()
        min_note = None
        max_note = None

        cur_time = 0
        for n in MaxLength(self, max_length):
            note = n["note_on"]
            time = n["time"]

            if min_note is None:
                min_note = note
            else:
                min_note = min(min_note, note)
            if max_note is None:
                max_note = note
            else:
                max_note = max(max_note, note)

            key_time = cur_time // 32
            if key_time not in notes_by_time:
                notes_by_time[key_time] = set()
            notes_by_time[key_time].add(note)
            
            cur_time += time

        min_key_time = min(notes_by_time.keys())
        max_key_time = max(notes_by_time.keys())

        num_notes = max_note - min_note
        num_time_keys = max_key_time - min_key_time

        lines = [["." for x in range(num_time_keys+1)] for y in range(num_notes+1)]
        print(notes_by_time)
        for key_time, notes in notes_by_time.items():
            x = key_time - min_key_time
            for note in notes:
                y = num_notes - 1 - (note - min_note)
                lines[y][x] = "*"

        return "\n".join("".join(line) for line in lines)
