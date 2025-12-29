"""
stream.py - Zero-Copy Streaming Generator Pipeline.
Streams millions of creator propagation events in constant O(1) memory.
"""
from typing import Iterator
from .hypervector import HyperVector

def stream_audio_events(raw_records: list[dict]) -> Iterator[tuple[str, HyperVector]]:
    for rec in raw_records:
        title = rec.get("title", "")
        dna = HyperVector.from_token(title)
        yield (rec.get("id", ""), dna)
