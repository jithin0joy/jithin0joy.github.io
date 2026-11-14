# Simulation methodology (reported in the paper)

| Parameter | Reported value |
|---|---|
| Simulator | NS-3.31 |
| Protocols | OLSR, AODV, DSDV |
| Node counts | 20, 30, 50 |
| Area | 500 × 500 m |
| Duration | 120 seconds |
| Mobility | Random Waypoint |
| Node speed | 10 m/s |
| Pause time | 10 seconds |
| MAC / PHY | 802.11b / DSSS 11 Mbps |
| Packet size | 64 bytes (simulation table) |
| Application data rate | 2048 bps |
| Propagation delay | Constant Speed |
| Propagation loss | Friis |
| Transmit power | 7.5 dBm (simulation narrative) |
| Traffic | Ten source/sink pairs; start around 60–61 seconds |

**Source inconsistency:** The paper's introduction describes a packet size of **64 bits**, whereas its simulation parameter table specifies **64 bytes**. This repository retains the table value and flags the inconsistency instead of silently resolving it.

## Metrics

- Packet delivery ratio (%) = 100 × packets received / packets sent.
- Packet loss ratio (%) = 100 × (packets sent − packets received) / packets sent.
- End-to-end delay = reception timestamp − transmission timestamp for delivered packets; average over received packets for an aggregate metric.
- Throughput = received payload bits / measured interval. The precise denominator and aggregation convention must be documented in any reproduction; do not assume a new calculation exactly matches the published results.

## Reproducibility caveats

The original source code, raw packet traces, per-run random seeds and full traffic configurations were not provided with this repository. Exact numerical replication is not guaranteed from the paper's parameter table alone. See `../src/README.md`.
