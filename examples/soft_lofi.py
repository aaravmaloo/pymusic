from pymusic.core.pitch import Note, Scale, Pitch
from pymusic.composition.pattern import Pattern
from pymusic.instruments.lofi import GuitarInstrument, SaxInstrument, MellowPiano, VinylEffect
from pymusic.instruments.drums import DrumInstrument
from pymusic.engine.audio_graph import Song

def create_lofi_soft():
    print("🌅 Creating SOFT Lo-Fi chill vibes...")
    
    # Lo-fi is even slower now
    total_beats = 64
    song = Song(name="Soft Chill", bpm=80, duration_beats=total_beats)
    
    # 1. Vinyl Crackle (Muffled)
    v_track = song.create_track("Vinyl", VinylEffect())
    v_track.gain = 0.15 # Quieter background
    v_pat = Pattern(loop=True, length_beats=16.0)
    v_pat.add_note("C4", duration=16.0)
    v_track.set_pattern(v_pat)
    
    # 2. Mellow Rhodes (Very soft)
    piano = MellowPiano()
    p_track = song.create_track("Rhodes", piano)
    p_track.gain = 0.4
    
    p_pat = Pattern(loop=True, length_beats=16.0)
    # Just the root and fifth for a super ambient feel
    p_pat.add_note("D3", duration=8.0, velocity=0.4)
    p_pat.add_note("C3", duration=8.0, velocity=0.4)
    p_track.set_pattern(p_pat)
    
    # 3. Lo-Fi Guitar (Muted)
    guitar = GuitarInstrument()
    g_track = song.create_track("Guitar", guitar)
    g_track.gain = 0.25 # Extremely soft
    
    g_pat = Pattern(loop=True, length_beats=8.0)
    g_pat.add_rest(2.0)
    g_pat.add_note("E4", duration=2.0, velocity=0.3)
    g_pat.add_note("D4", duration=4.0, velocity=0.2)
    g_track.set_pattern(g_pat)
    
    # 4. Lo-Fi Drums (Softened/Muffled)
    drums = song.create_track("Drums", DrumInstrument())
    drums.gain = 0.35 # Half the previous volume
    
    d_pat = Pattern(loop=True, length_beats=4.0)
    # Use very low velocities for the drums
    d_pat.add_note("C1", duration=1.0, velocity=0.4) # Soft Kick
    d_pat.add_rest(1.0)
    d_pat.add_note("D1", duration=1.0, velocity=0.3) # Brush-like Snare
    d_pat.add_rest(1.0)
    drums.set_pattern(d_pat)
    
    # Render
    print("☕ Rendering soft_lofi.wav...")
    song.render("soft_lofi.wav")
    print("Cloud soft music ready. ☕📚✨")

if __name__ == "__main__":
    create_lofi_soft()
