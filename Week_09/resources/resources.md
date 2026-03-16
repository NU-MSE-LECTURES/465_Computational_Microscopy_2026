# Week 9 Resources

Pipeline design checklist:
- keep every stage explicit: input, preprocessing, measurement, output
- save intermediate results only when they are expensive or reused
- benchmark small before scaling large

Scaling questions:
- which step is CPU-bound versus memory-bound?
- can the sweep be parallelized safely across independent inputs?
- is the output deterministic when random seeds are fixed?