

def generate_midifile(notes, count=128):
    import mido

    midifile = mido.MidiFile()
    track = mido.MidiTrack()
    midifile.tracks.append(track)

    for i, n in enumerate(notes):
        if i >= count:
            break
        track.append(mido.Message("note_on", note=n, time=128))
        track.append(mido.Message("note_off", note=n))

    return midifile


def open_midi_output(idx=None):
    import mido
    ports = mido.get_output_names()
    if idx is None:
        for i, p in enumerate(ports):
            print("[%s] %s" % (i, p))
        idx = input("?")
    return mido.open_output(ports[int(idx)])


def play_midifile(midifile, idx=None, output=None):
    if output is None:
        output = open_midi_output(idx)

    for msg in midifile.play():
        print(msg)
        output.send(msg)


