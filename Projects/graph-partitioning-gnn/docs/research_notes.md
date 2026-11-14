
# Research notes and provenance

## Sources consulted

- `Abstract.docx` — original student abstract, graph partitioning focus.
- `Internal Technical Report.docx` — original student technical report, conceptual freelancer/job recommendation system.
- `Research Proposal - Desertation Phase II.pdf` — 16-page proposal, *A Study on Graph Partitioning & GNN Systems*.

The documents were provided privately for reconstruction and are not automatically redistributed here. Some embedded figures reproduce third-party research diagrams and should not be republished without rights verification.

## Original research questions

1. How do graph partitioning methods split a network into meaningful groups, and what are their relative trade-offs?
2. Can user–job interactions be represented as a graph to support opportunity recommendations for newcomers and experienced freelancers?
3. Could a GNN and feedback mechanism improve such recommendations? (proposed, not experimentally answered)

## Documented historical result

The original report's methodology describes spectral partitioning applied to a sample graph and illustrates a 34-node network, Laplacian representation and two clusters. The report does not supply reproducible original numerical metrics in the reviewed text. The GNN model and feedback mechanism were not completed, with dataset creation identified as a barrier.

## Distinction from this repository

`src/experiment.py` is newly authored educational code (2026) that recreates the *concept* of partitioning experiments on synthetic data. Its outputs must not be presented as the original 2021–22 experimental results.

## Ethical and reproducibility notes

- No human subjects, clinical records or proprietary datasets are used.
- Synthetic graph data is generated with a fixed seed.
- New code is independently written using public Python libraries.
- Original collaborators are acknowledged. Any redistribution of the original student documents should be agreed with co-authors and checked for university/third-party rights.
