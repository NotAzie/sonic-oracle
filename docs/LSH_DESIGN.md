# MinHash LSH Sub-Millisecond Deduplication Architecture

Instead of comparing all pairs ($O(N^2)$), we map each track string into $k$-shingles (3-character grams), compute a 64-dimensional MinHash signature, and partition into $b=16$ bands with $r=4$ rows.

Candidate tracks hashing to the same bucket in any band are identified in $O(1)$ amortized time.
