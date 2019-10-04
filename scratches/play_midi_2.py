import mido

from musicpattern.midi import MidoPlayer, GmDrum
from musicpattern.patterns import *
from musicpattern import chords


class Music:

    def __init__(self):
        self.beats = {
            GmDrum.AcousticBaseDrum: EuclideanRhythm(2, 8),
            GmDrum.ClosedHiHat: Repeat(EuclideanRhythm(4, 8)) * (Sin(Range()/1.2)*.2+.8),
            GmDrum.LowMidTom: EuclideanRhythm(1, 3),
            GmDrum.LowFloorTom: EuclideanRhythm(1, 14),
            GmDrum.RideCymbal1: IsPrime(Range(48)+101) * .7,
        }

    def to_midi_tracks(self, max_length=1024):

        ticks = 100
        beat_tracks = [
            GateToMidi(
                MaxLength(Repeat(beat), max_length),
                note=note,
                ticks=ticks
            ).to_midi_track(channel=GmDrum.Channel)
            for note, beat in self.beats.items()
        ]

        beat_track = mido.merge_tracks(beat_tracks)

        return [beat_track]

    def to_midi_file(self, max_length=1024):
        midifile = mido.MidiFile()
        for track in self.to_midi_tracks(max_length=max_length):
            midifile.tracks.append(track)
        return midifile


if __name__ == "__main__":

    try:
        player = MidoPlayer(device_index=1)

        music = Music()

        player.play(music.to_midi_file(max_length=2**16))

    except KeyboardInterrupt:
        pass

