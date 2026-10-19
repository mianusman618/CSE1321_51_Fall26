midi_note=int(input("Enter a MIDI note [0, 127]: "))
letter_note=midi_note%12
freq=440*2**((midi_note-69)/12)
actual_letter_note=""
#print(freq,letter_note)
match letter_note:
    case 0:
        actual_letter_note="C"
    case 1:
        actual_letter_note = "C#"
    case 2:
        actual_letter_note = "D"
    case 3:
        actual_letter_note = "D#"
    case 4:
        actual_letter_note = "E"
    case 5:
        actual_letter_note = "F"
    case 6:
        actual_letter_note = "F#"
    case 7:
        actual_letter_note = "G"
    case 8:
        actual_letter_note = "G#"
    case 9:
        actual_letter_note = "A"
    case 10:
        actual_letter_note = "A#"
    case 11:
        actual_letter_note = "B"

print(f"MIDI Note {midi_note} is {freq:.2f} Hz which is a {actual_letter_note}")