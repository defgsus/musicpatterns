from musicpattern.midi import MidoPlayer
from musicpattern.patterns import *


def notes1():
    return NoteOns(
        note_on=List([1, 2, 3, 4]) + 60,
        time=128,
    )


if __name__ == "__main__":

    player = MidoPlayer(device_index=1)

    notes = notes1()

    player.play(notes.to_mido_midi_file(max_length=32))

