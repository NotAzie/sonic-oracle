# YouTube Song Finder (Prototype)

An early proof-of-concept exploring how to detect viral songs on YouTube by analyzing re-uploads across edits, AMVs, phonk, and slowed+reverb tracks.

## Known Limitations of Prototype
- Monolithic design in `find_songs.py`.
- Pairwise string matching scales poorly ($O(N^2)$).
- High quota usage without persistent caching.
- Limited anti-compilation filtering.

*Architectural refactoring planned for v2.*
