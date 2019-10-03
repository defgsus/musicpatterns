from musicpattern.midi import MidoPlayer, GmDrum
from musicpattern.patterns import *
from musicpattern import chords


def notes1():
    return MidiNoteOns(
        note_on=Repeat([1, 2, 3, 4, 5]) + 60,
        time=128,
    )


def notes_divisors():
    divisors = Divisors(Range(24) + 1) + 60

    return MidiNoteOns(
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

    return MidiNoteOns(
        note_on=layers + 50,
        velocity=Repeat(List([1, .7, .8, .6]) * 127),
        time=2 ** Repeat([7, 7, 8]),
    )


def notes_chord_progression():

    notes = FlatList(
        Lambda([0, 2, 3, 5], lambda value: value + List(chords.Major))
    )
    # does the same thing:
    notes = RepeatEach([0, 2, 3, 5], 3) + Repeat(chords.Major)

    return MidiNoteOns(
        note_on=Repeat(notes) + 60,
        velocity=80,
        time=512,
    )


def notes_euclidean_gates():

    eu = EuclideanRhythm([1, 2, 3, 4], 8)

    return GateToMidi(eu, 60, ticks=64)


def notes_merged_midi():

    notes = FlatList(Divisors(Range(300)))

    ticks = 100
    return MergeMidiNoteOns(
        Repeat(GateToMidi(EuclideanRhythm([1, 2, 1, 3], 8), Repeat(Range(20))+35, ticks=ticks, channel=9)),
        Repeat(GateToMidi(EuclideanRhythm([4, 2, 4, 6], 8), Repeat([GmDrum.LowBongo, GmDrum.HiBongo]), ticks=ticks, channel=9)),
        GateToMidi(EuclideanRhythm([1, 4, 4, 4], 32), 76 + notes, ticks=ticks),
    )


def test_mido_midi():
    return MidiNoteOns(
        note_on=[60, 61, 62, 63],
        time=[0, 20, 500, 0],
        channel=10,
    )


if __name__ == "__main__":

    try:
        player = MidoPlayer(device_index=1)

        #notes = notes_layers()
        #notes = notes_euclidean_gates()
        #notes = test_mido_midi()
        notes = notes_merged_midi()

        print(notes.to_string(max_length=40))

        player.play(notes.to_midi_file(max_length=2**16))

    except KeyboardInterrupt:
        pass

