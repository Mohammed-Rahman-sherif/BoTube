import librosa
y, sr = librosa.load("../Audio/sLhdk.wav")
y_harmonic, y_percussive = librosa.effects.hpss(y)
y_no_music = y_harmonic
librosa.output.write("audio_without_music.wav", y_no_music, sr)
