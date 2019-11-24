from ._base import PatternBase, CLASSES
from ._chord import Chord
from ._convert import convert_to_list
from ._crop import MaxLength, Length
from ._divisors import Divisors
from ._euclidean import EuclideanRhythm
from ._gate import GateToMidi
from ._inspect import is_iterable
from ._key_value import KeyValue
from ._lambda import Lambda
from ._list import List, FlatList
from ._next import Next
from ._math import IsPrime, Sin
from ._midi_note import MidiNoteOns, MergeMidiNoteOns
from ._range import Range
from ._repeat import Repeat, RepeatEach


__doc__ = "\n".join(
    f"{cls.__name__}: {cls.__doc__}"
    for cls in sorted(CLASSES, key=lambda cls: cls.__name__)
)
