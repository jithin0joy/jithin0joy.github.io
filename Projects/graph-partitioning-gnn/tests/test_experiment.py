import networkx as nx
import pytest
from src.experiment import metrics, spectral_bisection, synthetic_graph, run


def test_synthetic_graph_is_deterministic():
    assert set(synthetic_graph(42).edges()) == set(synthetic_graph(42).edges())


def test_spectral_bisection_is_valid():
    g = synthetic_graph(42)
    a, b = spectral_bisection(g)
    assert a.isdisjoint(b)
    assert a | b == set(g.nodes())
    assert abs(len(a) - len(b)) <= 1


def test_metrics_nonnegative():
    g = synthetic_graph(42)
    result = metrics(g, spectral_bisection(g))
    assert result["cut_edges"] >= 0
    assert result["normalized_cut"] >= 0
    assert 0 < result["balance_ratio"] <= 1


def test_experiment_writes_artifacts(tmp_path):
    result = run(tmp_path)
    assert result["nodes"] == 36
    assert (tmp_path / "metrics.json").exists()
    assert (tmp_path / "partition_comparison.png").exists()


def test_disconnected_graph_is_rejected():
    with pytest.raises(ValueError):
        spectral_bisection(nx.Graph([(1, 2), (3, 4)]))
