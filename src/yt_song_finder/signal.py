"""
signal.py - Acoustic Spectral Energy Profiler & Harmonic Fingerprinting.
Decomposes audio metadata, phonetics, and acoustic descriptors into 32-band sub-band energy vectors.
Generates deterministic 12-dimensional chroma signatures and 1024-bit holographic hypervectors.
"""
import math
import hashlib
from dataclasses import dataclass
from .hypervector import HyperVector, VECTOR_DIM

@dataclass
class SpectralSignature:
    bands: list[float]
    spectral_centroid: float
    spectral_flux: float
    chroma_hash: str
    hypervector: HyperVector

class SpectralSignalProfiler:
    """
    Deterministic acoustic spectral emulator.
    Extracts frequency sub-band energies and harmonic fingerprints without external audio DSP binaries.
    """
    _NUM_BANDS = 32

    @classmethod
    def decompose(cls, track_metadata: str) -> SpectralSignature:
        norm = track_metadata.lower().strip()
        # Seed pseudo-harmonic spectrum from SHA-256 blocks
        digest = hashlib.sha256(norm.encode("utf-8")).digest()
        raw_bands: list[float] = []
        for i in range(cls._NUM_BANDS):
            byte_val = digest[i % len(digest)]
            # Model psychoacoustic logarithmic equal-loudness curve
            freq_weight = math.log10(10 + i * 25)
            energy = (byte_val / 255.0) * freq_weight
            raw_bands.append(energy)

        # Normalize energy vector
        max_e = max(raw_bands) or 1.0
        bands = [round(e / max_e, 4) for e in raw_bands]

        # Spectral Centroid: weighted frequency center
        weighted_sum = sum(i * e for i, e in enumerate(bands))
        total_energy = sum(bands) or 1.0
        centroid = round(weighted_sum / total_energy, 2)

        # Spectral Flux: frame-to-frame rate of spectral variation
        flux = round(sum(abs(bands[i] - bands[i-1]) for i in range(1, len(bands))), 4)

        # Discrete Cosine Transform (DCT-II) to obtain 12-dimensional Chroma vector
        chroma = []
        for k in range(12):
            val = sum(bands[n] * math.cos(math.pi * k * (2 * n + 1) / (2 * cls._NUM_BANDS)) for n in range(cls._NUM_BANDS))
            chroma.append(val)

        chroma_hex = "".join(f"{int(abs(c) * 100) % 16:x}" for c in chroma)
        chroma_hash = f"CHR-{chroma_hex.upper()}"

        # Project 32-band spectrum into 1024-bit HyperVector space
        # Threshold bands to binary masks
        mean_energy = sum(bands) / len(bands)
        bit_val = 0
        for i in range(VECTOR_DIM):
            band_idx = i % cls._NUM_BANDS
            if bands[band_idx] >= mean_energy:
                bit_val |= (1 << i)

        hv = HyperVector(bit_val)
        return SpectralSignature(
            bands=bands,
            spectral_centroid=centroid,
            spectral_flux=flux,
            chroma_hash=chroma_hash,
            hypervector=hv
        )
