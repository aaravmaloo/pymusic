from pymusic.core.pitch import Note, Scale
from pymusic.composition.pattern import Pattern
from pymusic.composition.chord import Chord
from pymusic.instruments.synth import SynthInstrument
from pymusic.instruments.piano import PianoInstrument
from pymusic.instruments.drums import DrumInstrument
from pymusic.engine.audio_graph import Song

def main():
    print("Initializing pymusic demo...")
    
    # 1. Create Song
    song = Song(name="Techno Genesis", bpm=128)
    
    # 2. Setup Drums
    drum_inst = DrumInstrument()
    drums = song.create_track("Drums", drum_inst)
    drum_pat = Pattern()
    for _ in range(4):
        drum_pat.add_note("C1", duration=0.5)  # Kick
        drum_pat.add_note("F#1", duration=0.5) # Hi-hat
    drums.set_pattern(drum_pat)
    
    # 3. Setup Bass Synth
    bass_inst = SynthInstrument(oscillator_type="saw")
    bass = song.create_track("Bass", bass_inst)
    bass_pat = Pattern(["C2", "C2", "G1", "C2"])
    bass.set_pattern(bass_pat)
    
    # 4. Setup Lead Piano
    piano_inst = PianoInstrument()
    lead = song.create_track("Lead", piano_inst)
    
    # Use a scale for the lead
    c_minor = Scale("C", "minor")
    notes = c_minor.get_notes(octave=4)
    lead_pat = Pattern([notes[0], notes[2], notes[4], notes[6]])
    lead.set_pattern(lead_pat)
    
    # 5. Render
    print("Rendering to techno.wav...")
    song.render("techno.wav")
    
    # 6. Export MIDI
    print("Exporting to techno.mid...")
    song.export_midi("techno.mid")
    
    print("Done!")

if __name__ == "__main__":
    main()
