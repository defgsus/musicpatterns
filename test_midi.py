import time
import mido

from tools.midi import *
from tools.patterns import *
from tools.plot import *


def open_midi_output(idx=None):
    ports = mido.get_output_names()
    if idx is None:
        for i, p in enumerate(ports):
            print("[%s] %s" % (i, p))
        idx = input("?")
    return mido.open_output(ports[int(idx)])


def test_output(output):
    for note in range(32, 60):
        output.send( mido.Message("note_on", note=note) )
        time.sleep(.1)
        output.send( mido.Message("note_off", note=note) )

def test_midifile(output):
    midifile = mido.MidiFile()
    miditrack = mido.MidiTrack()
    midifile.tracks.append(miditrack)

    t = 0.
    for note in range(32, 60):
        miditrack.append(mido.Message("note_on", note=note, time=109))
        miditrack.append(mido.Message("note_off", note=note, time=109))
        t += 10.

    for msg in midifile.play():
        if msg.type == "note_on":
            print(msg)
        output.send(msg)

if 0:
    output = open_midi_output(0)
    test_midifile(output)


if 1:
    p1 = PatternRepeat(PatternValues([1,2,3]), PatternValues([1,2,3,4]))
    dump_values(p1[:128])

    midi = generate_midifile(p1+36)
    play_midifile(midi, idx=0)