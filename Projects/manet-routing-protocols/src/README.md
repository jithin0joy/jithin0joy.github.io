# NS-3 reproduction plan — not original 2022 code

The original experiment's source files were not supplied. This directory intentionally contains no invented 'original' simulation implementation.

## To develop a reproducible extension

1. Install an appropriate NS-3 release and record its version (the paper used NS-3.31).
2. Configure 802.11b ad-hoc Wi-Fi, Friis propagation, 500 × 500 m area and Random Waypoint mobility.
3. Run AODV, OLSR and DSDV separately with 20, 30 and 50 nodes.
4. Use 10 source/sink pairs, 64-byte packets (per the paper's parameter table), 2048-bps application traffic, and a 120-second duration.
5. Record routing setup, exact traffic pattern, seeds, packet counts, throughput and latency.
6. Run repeated seeds, summarize uncertainty and compare against the publication.
7. Clearly label all new code and outputs **independent reproduction (post-2022)**.

**Open methodological issue:** The introduction says 64 bits, while the parameter table says 64 bytes. Document which interpretation is implemented.

No runnable NS-3 code is asserted to be tested or included here.
