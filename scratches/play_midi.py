from musicpattern.midi import MidoPlayer
from musicpattern.patterns import *


def notes1():
    return NoteOns(
        note_on=Repeat([1, 2, 3, 4, 5]) + 60,
        time=128,
    )


def notes2():
    divisors = Divisors(Range(24) + 1) + 60

    return NoteOns(
        note_on=Repeat(divisors),
        velocity=60,
        time=128,
    )


if __name__ == "__main__":

    player = MidoPlayer(device_index=1)

    notes = notes2()

    print(notes.to_string())

    player.play(notes.to_midi_file(max_length=2**16))

