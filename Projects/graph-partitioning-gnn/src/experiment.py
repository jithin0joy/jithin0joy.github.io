
"""Reproducible educational graph-partitioning reconstruction (2026)."""
from __future__ import annotations
import argparse
import json
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
from scipy.linalg import eigh


def synthetic_graph(seed: int = 42) -> nx.Graph:
    """Two planted communities; synthetic, not the original MCA dataset."""
    return nx.stochastic_block_model([18, 18], [[0.45, 0.035], [0.035, 0.45]], seed=seed)


def spectral_bisection(graph: nx.Graph) -> tuple[set, set]:
    """Partition via the second eigenvector of the symmetric normalized Laplacian."""
    nodes = list(graph.nodes())
    adjacency = nx.to_numpy_array(graph, nodelist=nodes, dtype=float)
    degrees = adjacency.sum(axis=1)
    if np.any(degrees == 0):
        raise ValueError("Spectral bisection requires a graph without isolated vertices")
    if not nx.is_connected(graph):
        raise ValueError("Spectral bisection requires a connected graph")
    inv = np.diag(1 / np.sqrt(degrees))
    laplacian = np.eye(len(nodes)) - inv @ adjacency @ inv
    _, vectors = eigh(laplacian)
    # Convert normalized-Laplacian eigenvector to generalized eigenvector.
    fiedler = inv @ vectors[:, 1]
    # Median threshold encourages a balanced split for this demonstration.
    order = np.argsort(fiedler, kind="stable")
    first = {nodes[int(i)] for i in order[:len(nodes) // 2]}
    return first, set(nodes) - first


def metrics(graph: nx.Graph, groups: tuple[set, set]) -> dict:
    a, b = groups
    if not a or not b or a & b or a | b != set(graph.nodes()):
        raise ValueError("Partition must cover all nodes with two nonempty disjoint groups")
    cut = nx.cut_size(graph, a, b)
    va, vb = nx.volume(graph, a), nx.volume(graph, b)
    return {
        "cut_edges": int(cut),
        "normalized_cut": float(cut / va + cut / vb),
        "group_sizes": [len(a), len(b)],
        "balance_ratio": float(min(len(a), len(b)) / max(len(a), len(b))),
    }


def run(output: Path, seed: int = 42) -> dict:
    output.mkdir(parents=True, exist_ok=True)
    graph = synthetic_graph(seed)
    methods = {
        "kernighan_lin": tuple(map(set, nx.community.kernighan_lin_bisection(graph, seed=seed))),
        "spectral": spectral_bisection(graph),
    }
    result = {name: metrics(graph, groups) for name, groups in methods.items()}
    payload = {"seed": seed, "nodes": graph.number_of_nodes(), "edges": graph.number_of_edges(), "methods": result,
               "note": "Synthetic educational reconstruction; not original MCA measurements"}
    (output / "metrics.json").write_text(json.dumps(payload, indent=2) + "\n", encoding="utf8")
    positions = nx.spring_layout(graph, seed=seed)
    fig, axes = plt.subplots(1, 2, figsize=(11, 5))
    for ax, (name, (a, b)) in zip(axes, methods.items()):
        palette = [0 if n in a else 1 for n in graph.nodes()]
        nx.draw_networkx(graph, pos=positions, node_color=palette, cmap=plt.cm.coolwarm,
                         node_size=75, with_labels=False, width=0.45, ax=ax)
        ax.set_title(f"{name.replace('_', ' ').title()} | cut={result[name]['cut_edges']}")
    fig.suptitle("Synthetic graph partitioning — educational reconstruction (2026)")
    fig.tight_layout()
    fig.savefig(output / "partition_comparison.png", dpi=160)
    plt.close(fig)
    return payload


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=Path("results"))
    parser.add_argument("--seed", type=int, default=42)
    args = parser.parse_args()
    print(json.dumps(run(args.output, args.seed), indent=2))
