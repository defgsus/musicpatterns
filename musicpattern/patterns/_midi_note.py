from ._base import PatternBase
from ._next import Next
from ._key_value import KeyValue
from ._crop import MaxLength


class MidiMixin:
    """
    Mixin to create Mido miditracks from the own sequence consisting of objects:
    {
        "note_on": int,     # note value 0-127
        "note_off": int,    # optional instead of note_on
        "velocity": int,    # 0-127
        "time": int|float,  # number of ticks to wait before note
    }
    """
    def to_midi_track(self, max_length=128, program=None, channel=None):
        import mido

        track = mido.MidiTrack()
        if program:
            track.append(mido.Message(
                "program_change", program=program,
            ))

        for i, n in enumerate(MaxLength(self, max_length)):
            track.append(mido.Message(
                "note_on" if n.get("note_on") else "note_off",
                note=int(n.get("note_on") or n.get("note_off")),
                velocity=int(n["velocity"]),
                time=n["time"],
                channel=channel or n.get("channel") or 0,
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

            cur_time += time

            key_time = cur_time // 32
            if key_time not in notes_by_time:
                notes_by_time[key_time] = set()
            notes_by_time[key_time].add(note)

        min_key_time = min(notes_by_time.keys())
        max_key_time = max(notes_by_time.keys())

        num_notes = max_note - min_note
        num_time_keys = max_key_time - min_key_time

        lines = [["." for x in range(num_time_keys+1)] for y in range(num_notes+1)]
        for key_time, notes in notes_by_time.items():
            x = key_time - min_key_time
            for note in notes:
                y = num_notes - 1 - (note - min_note)
                lines[y][x] = "*"

        return "\n".join("".join(line) for line in lines)


class MidiNoteOns(MidiMixin, KeyValue):
    """
        Generates a dictionary for each input value:
        {
            "note_on": int,     # note value 0-127
            "velocity": int,    # 0-127
            "time": int|float,  # number of ticks to wait before note
            "channel": int,     # channel 0-15
        }
    """
    def __init__(self, note_on, velocity=64, time=0, channel=0):
        super().__init__({
            "note_on": note_on,
            "velocity": velocity,
            "time": time,
            "channel": channel,
        })


class MergeMidiNoteOns(MidiMixin, PatternBase):
    """
    Merge two or more MidiNoteOns outputs
    """
    def __init__(self, *notes):
        self.notes = None
        super().__init__(notes=notes)

    def iterate(self):
        note_iterators = [
            Next(note)
            for note in self.notes
        ]

        cur_time = 0
        last_channel_time = {
            i: 0
            for i in range(len(note_iterators))
        }

        try:
            while True:

                next_notes = []
                for idx, note_iter in enumerate(note_iterators):
                    try:
                        note = note_iter.next()
                        next_notes.append({
                            "note_on": note["note_on"],
                            "velocity": note["velocity"],
                            "time": note["time"],
                            "channel": note.get("channel") or 0,
                            "idx": idx,
                        })
                    except StopIteration:
                        pass

                if not next_notes:
                    break

                next_notes.sort(key=lambda n: n["note_on"])
                next_notes.sort(key=lambda n: n["time"])

                for note in next_notes:
                    note_time = note["time"] + last_channel_time[note["idx"]] - cur_time
                    cur_time += note_time
                    last_channel_time[note["idx"]] = cur_time
                    yield {
                        "note_on": note["note_on"],
                        "velocity": note["velocity"],
                        "time": note_time,
                        "channel": note["channel"],
                    }

        except StopIteration:
            return
