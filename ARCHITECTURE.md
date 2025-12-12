# System Architecture & Technical Specifications

## Pipeline Flowchart

```
┌─────────────────────────┐
│ Targeted Query Generator │ (phonk, amv, gaming, slowed+reverb, meme)
└───────────┬─────────────┘
            ▼
┌─────────────────────────┐
│ Bloom Filter Filter     │ O(1) duplicate video ID rejection
└───────────┬─────────────┘
            ▼
┌─────────────────────────┐
│ Multi-Strategy Extractor │ Title patterns, description credits, tag NLP
└───────────┬─────────────┘
            ▼
┌─────────────────────────┐
│ MinHash LSH Index       │ 64 hashes, b=16, r=4 (Sub-millisecond clustering)
└───────────┬─────────────┘
            ▼
┌─────────────────────────┐
│ Shannon Entropy Scorer   │ 4-factor equation + Sybil upload defense
└───────────┬─────────────┘
            ▼
┌─────────────────────────┐
│ Multi-Format Exporter   │ JSON, CSV, TXT, Web Dashboard
└─────────────────────────┘
```
