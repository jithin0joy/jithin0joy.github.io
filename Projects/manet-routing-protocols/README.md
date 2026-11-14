# Mobile Ad-hoc Routing Protocols: AODV, OLSR and DSDV

**Published MCA research (2022) | IEEE GCAT 2022 | NS-3 simulation**

**Paper:** [Comprehensive Study on Mobile Ad-hoc Routing Protocols: OLSR, AODV and DSDV](https://ieeexplore.ieee.org/document/9971899/)  
**Authors:** Jisha R C, Jithin Joseph, Muhammed Nadeem Mohammed Basheer  
**Affiliation:** Amrita Vishwa Vidyapeetham  
**IEEE Xplore document:** 9971899

## Research idea

Mobile ad-hoc networks (MANETs) have no fixed access point or centralized routing infrastructure. As nodes move, network paths change. The paper evaluates whether reactive **AODV** or proactive **OLSR** and **DSDV** performs better under changing node counts.

## What we studied

- NS-3 version 3.31
- 20, 30 and 50 nodes in a 500 × 500 m area
- Random Waypoint mobility at 10 m/s, 10-second pause
- 120-second simulation; application traffic starts around 60–61 seconds
- Packet delivery ratio, packet loss, throughput and end-to-end delay

The publication reports higher average throughput for AODV in the studied scenarios, alongside higher end-to-end delay. These findings are **specific to the experiment**, not a universal protocol ranking.

## Repository contents

- [Research summary](docs/research-summary.md)
- [Experimental setup](docs/simulation-methodology.md)
- [Findings and limitations](docs/results-and-findings.md)
- [Publication and attribution](docs/references.md)
- [Reproduction plan](src/README.md)
- [Data provenance](data/README.md)

## Research integrity and reproducibility

This repository **does not include the IEEE publisher-formatted PDF**. Read the publication at the IEEE link above. The original 2022 NS-3 source, raw traces and random seeds have not been supplied here, so no code or data is represented as the original experiment. `src/` contains a reproducibility plan, **not a claimed verified reproduction**.

## Research extensions (not results of the 2022 paper)

Potential directions: energy-aware routing, secure routing, graph-learning-based routing and robust communication for remote health sensors. These are proposals for future work, not established clinical or experimental findings.

## Author

Jithin Joseph · [GitHub](https://github.com/jithin0joy)
