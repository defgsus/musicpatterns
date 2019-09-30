from musicpattern.midi import MidoPlayer
from musicpattern.patterns import *


def notes1():
    return NoteOns(
        note_on=Repeat([1, 2, 3, 4, 5]) + 60,
        time=128,
    )


def notes_divisors():
    divisors = Divisors(Range(24) + 1) + 60

    return NoteOns(
        note_on=Repeat(divisors),
        velocity=60,
        time=128,
    )


def notes_layers():
    layers = (
        Repeat(Range(3)) +
        Repeat(Range(5)) +
        Repeat(Range(7))
    )

    return NoteOns(
        note_on=layers + 50,
        velocity=Repeat(List([1, .7, .8, .6]) * 127),
        time=2 ** Repeat([7, 7, 8]),
    )


if __name__ == "__main__":

    try:
        player = MidoPlayer(device_index=1)

        notes = notes_layers()

        print(notes.to_string())

        player.play(notes.to_midi_file(max_length=2**16))

    except KeyboardInterrupt:
        pass

