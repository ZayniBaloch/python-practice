import chromaprint
import os
from tempfile import NamedTemporaryFile
import numpy as np
from scipy.io import wavfile

def test_chromaprint_fingerprint():
    # Generate a test signal: a 440 Hz sine wave for 1 second
    sample_rate = 44100
    duration = 1.0
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    signal = 0.5 * np.sin(2 * np.pi * 440 * t)

    # Convert to int16
    signal_int16 = np.int16(signal * 32767)

    # Write to a temporary WAV file
    with NamedTemporaryFile(suffix=".wav", delete=False) as tmpfile:
        wavfile.write(tmpfile.name, sample_rate, signal_int16)
        tmpfile_path = tmpfile.name

    try:
        # Compute the fingerprint using chromaprint
        fingerprint, version = chromaprint.decode_fingerprint(chromaprint.fingerprint_file(tmpfile_path))

        # Check that the fingerprint is not empty and has a valid version
        assert fingerprint is not None
        assert len(fingerprint) > 0
        assert version > 0

    finally:
        os.remove(tmpfile_path)
