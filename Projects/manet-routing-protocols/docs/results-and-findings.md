# Published results and interpretation

The 2022 study evaluates 20, 30 and 50 nodes and compares packet reception, packet loss, throughput and delay.

- **AODV:** The paper reports higher throughput than OLSR and DSDV under the tested conditions.
- **DSDV:** Packet loss increases as the number of devices increases in the reported comparisons.
- **OLSR:** Uses multipoint relays to reduce redundant dissemination; its observed results depend on the simulation configuration.
- **Delay trade-off:** The paper reports greater end-to-end delay for AODV than for the other protocols in its scenarios.

## Interpretation

A routing method that performs well on throughput may not be the best choice for delay-sensitive traffic. Protocol selection depends on topology, mobility and workload.

## Limits

The study uses only three node counts and a specified mobility and traffic setup. The supplied material does not establish statistically robust performance across many independent random seeds. **No new experimental measurements are presented in this repository.**

[Original publication and figures](https://ieeexplore.ieee.org/document/9971899/)
