import usb_midi
import adafruit_midi
from adafruit_midi.note_on import NoteOn
from adafruit_midi.note_off import NoteOff
import time

midi = adafruit_midi.MIDI(midi_out=usb_midi.ports[1], out_channel=0)

for note_number in range(66,72):
    print("Playing:",note_number)
    midi.send(NoteOn(note_number, 80))
    time.sleep(0.5)
    midi.send(NoteOff(note_number,0))
    
