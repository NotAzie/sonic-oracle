"""
test_signal.py - Unit tests for SpectralSignalProfiler and Chroma hashing.
"""
import unittest
from yt_song_finder.signal import SpectralSignalProfiler

class TestSpectralSignal(unittest.TestCase):
    def test_spectral_decomposition(self):
        sig = SpectralSignalProfiler.decompose("Kordhell - Phonk Horizon")
        self.assertEqual(len(sig.bands), 32)
        for b in sig.bands:
            self.assertTrue(0.0 <= b <= 1.0)
        self.assertTrue(0.0 <= sig.spectral_centroid <= 32.0)
        self.assertTrue(sig.chroma_hash.startswith("CHR-"))
        self.assertEqual(sig.hypervector.bits.bit_count() > 0, True)

    def test_spectral_determinism(self):
        sig1 = SpectralSignalProfiler.decompose("Alan Walker - Faded")
        sig2 = SpectralSignalProfiler.decompose("Alan Walker - Faded")
        self.assertEqual(sig1.chroma_hash, sig2.chroma_hash)
        self.assertEqual(sig1.spectral_centroid, sig2.spectral_centroid)
        self.assertEqual(sig1.hypervector.bits, sig2.hypervector.bits)

if __name__ == "__main__":
    unittest.main()
