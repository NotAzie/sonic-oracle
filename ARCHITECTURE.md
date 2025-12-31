# SonicOracle System Architecture Specification

## Overview

SonicOracle is designed as a modular, low-latency, zero-dependency cultural intelligence engine. The architecture enforces strict separation of concerns, deterministic data flow, and constant-time algorithmic complexity across critical path execution.

---

## Topology and Core Subsystems

```
[ Ingestion & Normalization ]
         |
         v
[ 1024-bit HDC Extraction ] ----> [ MinHash LSH & Bloom Filter ]
         |
         v
[ Memetic Hypergraph Construction ]
         |
         v
[ Bipartite Markov Power Iteration (EigenVirality) ]
         |
         v
[ Non-Linear Epidemiological Solver (R0 / RK4) ]
         |
         +-----------------------+
         |                       |
         v                       v
[ DCF Valuation Engine ]   [ Alert Bus & Dispatcher ]
         |                       |
         v                       v
[ Presentation Layer: CLI, REST Server, Streaming Batch ]
```

---

## Subsystem Specifications

### 1. Source Layout and Package Organization (`src/yt_song_finder`)
- `hypervector.py`: 1024-bit binary vector primitive.
- `signal.py`: Spectral decomposition into 32 bands and 12-dimensional chroma.
- `graph.py`: Bipartite hypergraph with sparse normalized transition matrices.
- `epidemiology.py`: Kermack-McKendrick SIR model with analytical horizons and RK4 solver.
- `valuation.py`: DCF financial modeling and A&R valuation bands.
- `alerting.py`: Threshold-based event bus with memory, callback, and log sinks.
- `batch.py`: Generator-based streaming NDJSON/CSV batch processor.
- `lsh.py`: MinHash locality-sensitive hashing index.
- `bloom.py`: Kirsch-Mitzenmacher bit-packed Bloom filter.
- `cache.py`: Dual-tier in-memory LRU and SQLite WAL persistent storage.
- `server.py`: Lightweight embedded HTTP microservice.
- `cli.py`: Command-line interface and table renderers.
- `core.py`: Unified API facade (`Oracle`).

### 2. Concurrency and Thread Safety
- The core data structures (`HyperVector`, `ViralContagionModel`, `RoyaltyValuationEngine`) are stateless value objects or encapsulate immutable representations.
- Database access via `DualTierCache` utilizes SQLite Write-Ahead Logging (WAL) mode with dedicated connection boundaries to prevent contention under concurrent access.

### 3. Memory Profile and Resource Boundaries
- 1024-bit hypervectors are stored as native Python arbitrary-precision integers requiring 160 bytes of memory per instance.
- Streaming operations operate via lazy Python generators to guarantee bounded resident memory footprint regardless of dataset scale.
