
# Graph Partitioning & Graph Neural Network Systems

**MCA Semester 3 academic research (2021–2022) + modern educational reconstruction (2026)**

**Original research team:** Jithin Joseph and Muhammed Nadeem Mohammed Basheer  
**Guide:** Jisha R C  
**Institution:** Amrita Vishwa Vidyapeetham, Amrita School of Engineering

## Overview

Our Semester 3 research investigated network science and graph partitioning. We studied Kernighan–Lin and spectral partitioning, demonstrated spectral clustering on a sample graph, and surveyed graph neural network (GNN) architectures for recommendation systems. The proposed application represented freelancers and companies/jobs as interacting entities and considered graph-based grouping followed by a GNN to recommend opportunities, including to newcomers.

**Historical accuracy:** The original report says spectral partitioning was implemented on sample data. It also says the GNN recommender had **not been implemented**: a suitable labelled dataset and feedback mechanism remained open problems. This repository does not claim a trained or evaluated GNN recommender, and no original performance numbers are asserted.

## What I studied

- **Graph modelling:** vertices, edges, adjacency, degrees and Laplacian matrices.
- **Kernighan–Lin:** heuristic balanced graph bisection by improving swaps.
- **Spectral partitioning:** the graph Laplacian, Fiedler vector and normalized-cut ideas.
- **GNNs:** GCN, GraphSAGE, GAT and gated graph neural networks (GGNN); message passing and neighborhood aggregation.
- **Recommendations:** bipartite user–item graphs, general vs sequential recommendation, social and knowledge graph enhancements.
- **Research process:** literature review, architecture design, data availability constraints, evaluation planning and honest reporting of limitations.

## What is implemented here (2026 reconstruction)

A runnable **educational experiment**, written after the original dissertation, compares two graph partitioning methods on a synthetic two-community graph. It measures cut size, normalized cut and partition balance and writes a visualization and JSON metrics. This reconstruction uses NetworkX and SciPy; it is **not recovered original source code**.

```bash
python -m venv .venv
source .venv/bin/activate      # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python -m src.experiment --output results
python -m pytest -q
```

Generated artifacts: `results/partition_comparison.png` and `results/metrics.json` (run locally; outputs not included as historical research results).

## Experimental method

1. Generate a deterministic, seeded stochastic block model graph with two communities.
2. Run NetworkX Kernighan–Lin bisection and a normalized-Laplacian spectral bisection using the second eigenvector.
3. Compare graph cut, normalized cut, group sizes and balance.
4. Save a common graph layout and per-method partition plots.

**Limitations:** synthetic data; two-way partitions only; spectral sign thresholding is a heuristic; no runtime benchmarking or statistical generalization; no trained GNN model. No claims are made about performance on freelancer data.

## Original proposal vs this repository

| Component | 2021–22 academic work | 2026 reconstruction |
|---|---|---|
| Kernighan–Lin | Literature study | Runnable NetworkX baseline |
| Spectral partitioning | Literature study and sample demonstration | Runnable normalized-Laplacian bisection |
| GCN / GraphSAGE / GAT / GGNN | Literature survey | Documented only; not trained |
| Freelancer/job recommendation | Proposed architecture | Not implemented |
| Dataset / feedback | Identified as unresolved | Synthetic graph for partitioning only |

## Attribution and academic integrity

This is a collaborative student research project, not a sole-authored publication. Research credit belongs to both student authors, under the supervision of the academic guide. The implementation in `src/` is a new educational reconstruction and should not be cited as the original university code. Original documents and third-party figures have not been redistributed; see `docs/research_notes.md`.

## Future work

- Evaluate algorithms across graph sizes, community mixing parameters and random seeds.
- Add stronger partitioning baselines and compare runtime and cut-quality trade-offs.
- Acquire a legally shareable user–item dataset, define temporal splits and ranking metrics, then prototype and evaluate a GNN recommender.
- Explore knowledge-graph approaches to interpretable AI, including healthcare applications, as a **separate future research project**.

## References

- Kernighan, B. W. and Lin, S. (1970). An efficient heuristic procedure for partitioning graphs.
- Shi, J. and Malik, J. (2000). Normalized cuts and image segmentation.
- Kipf, T. N. and Welling, M. (2017). Semi-supervised classification with graph convolutional networks.
- Wu, S. et al. (2020). Graph neural networks in recommender systems: a survey.
- Zhou, J. et al. (2020). Graph neural networks: A review of methods and applications.

See `docs/research_notes.md` for source-based methodology and limitations.
