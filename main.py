import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import csv
import argparse
import sys

# =========================================================
# OPTIONAL IMPORT (LIVE MODE)
# =========================================================

try:
    from scapy.all import sniff
    SCAPY_AVAILABLE = True
except Exception:
    SCAPY_AVAILABLE = False


# =========================================================
# 1. INPUT LAYER
# =========================================================

def capture_live_packets(packet_count=100):
    """
    Capture live packets WITHOUT filtering (pure real-world input)
    """
    if not SCAPY_AVAILABLE:
        print("[ERROR] Scapy not installed.")
        return None

    connections = {}

    def process_packet(packet):
        if packet.haslayer("IP"):
            src = packet["IP"].src
            dst = packet["IP"].dst

            key = (src, dst)
            connections[key] = connections.get(key, 0) + 1

    try:
        print("[INFO] Capturing packets...")
        sniff(prn=process_packet, count=packet_count, timeout=15)

        if len(connections) == 0:
            print("[WARNING] No packets captured.")
            return None

        return connections

    except Exception as e:
        print(f"[ERROR] Capture failed: {e}")
        return None


def load_from_csv(filename):
    connections = {}

    with open(filename, 'r') as file:
        reader = csv.DictReader(file)

        if reader.fieldnames is None or not {'source', 'target'}.issubset(reader.fieldnames):
            raise ValueError("[ERROR] CSV must contain 'source' and 'target'")

        for row in reader:
            src = row['source']
            dst = row['target']

            try:
                weight = int(row.get('weight', 1) or 1)
            except ValueError:
                weight = 1

            key = (src, dst)
            connections[key] = connections.get(key, 0) + weight

    return connections


def get_connections(mode, filename):
    if mode == "live":
        data = capture_live_packets()
        if data is None:
            print("[INFO] Falling back to CSV...")
            return load_from_csv(filename)
        return data
    return load_from_csv(filename)


# =========================================================
# 2. GRAPH + MATRIX
# =========================================================

def build_graph(connections, directed=False):
    G = nx.DiGraph() if directed else nx.Graph()

    for (src, dst), weight in connections.items():
        if G.has_edge(src, dst):
            G[src][dst]['weight'] += weight
        else:
            G.add_edge(src, dst, weight=weight)

    return G


def graph_to_matrix(G):
    nodes = list(G.nodes())
    mapping = {node: i for i, node in enumerate(nodes)}

    G_num = nx.relabel_nodes(G, mapping)
    A = nx.to_numpy_array(G_num, weight='weight')

    return A, nodes


# =========================================================
# 3. FEATURES
# =========================================================

def compute_degree(A):
    return np.sum(A, axis=1)


def compute_neighbor_importance(A, scores):
    n = len(scores)
    neighbor_score = np.zeros(n)

    for i in range(n):
        neighbors = np.where(A[i] > 0)[0]
        if len(neighbors) > 0:
            neighbor_score[i] = np.mean(scores[neighbors])

    return neighbor_score


def normalize(x):
    min_x, max_x = np.min(x), np.max(x)
    if max_x - min_x == 0:
        return np.zeros_like(x)
    return (x - min_x) / (max_x - min_x)


# =========================================================
# 4. CLASSIFICATION (UNCHANGED LOGIC)
# =========================================================

def classify_nodes(scores, degrees, neighbor_scores):

    if len(scores) == 1:
        return {0: "Isolated"}, {0: 0.0}

    s = normalize(scores)
    d = normalize(degrees)
    n = normalize(neighbor_scores)

    results = {}
    final_scores = {}

    print("\n--- Node Features ---")

    for i in range(len(scores)):

        score = 0.5*s[i] + 0.25*d[i] + 0.25*n[i]
        final_scores[i] = score

        print(f"Node {i}: Score={s[i]:.3f}, Degree={d[i]:.3f}, Neighbor={n[i]:.3f}")

        if s[i] < 0.4 and n[i] > 0.7:
            results[i] = "Suspicious"

        elif d[i] < 0.3 and s[i] < 0.3:
            if n[i] > 0.5:
                results[i] = "Normal"
            else:
                results[i] = "Weak Anomaly"

        else:
            results[i] = "Normal"

    return results, final_scores


# =========================================================
# 5. VISUALIZATION
# =========================================================

def visualize_graph(G, results, node_labels):

    color_map = []

    for i in range(len(node_labels)):
        label = results[i]

        if label == "Normal":
            color_map.append("blue")
        elif label == "Weak Anomaly":
            color_map.append("orange")
        elif label == "Suspicious":
            color_map.append("red")
        else:
            color_map.append("gray")

    pos = nx.spring_layout(G, seed=42)

    nx.draw(G, pos, with_labels=True, node_color=color_map, node_size=800)
    plt.title("Network Anomaly Detection")

    from matplotlib.patches import Patch
    legend = [
        Patch(color="blue", label="Normal"),
        Patch(color="orange", label="Weak"),
        Patch(color="red", label="Suspicious"),
    ]

    plt.legend(handles=legend)
    plt.show()


# =========================================================
# 6. EXPORT
# =========================================================

def export_results(filename, node_labels, results, scores):

    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["node", "label", "score"])

        for i, node in enumerate(node_labels):
            writer.writerow([node, results[i], round(scores[i], 3)])

    print(f"[INFO] Results exported to {filename}")


# =========================================================
# 7. MAIN
# =========================================================

def main():

    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", choices=["live", "file"], default="file")
    parser.add_argument("--input", default="network.csv")
    parser.add_argument("--directed", action="store_true")
    parser.add_argument("--output", default="results.csv")

    args = parser.parse_args()

    try:
        connections = get_connections(args.mode, args.input)
    except Exception as e:
        print(e)
        sys.exit(1)

    if len(connections) == 0:
        print("[ERROR] No data available.")
        sys.exit(1)

    G = build_graph(connections, directed=args.directed)
    A, node_labels = graph_to_matrix(G)

    if args.directed:
        eigenvalues, eigenvectors = np.linalg.eig(A)
        principal_vector = eigenvectors[:, np.argmax(np.real(eigenvalues))]
    else:
        eigenvalues, eigenvectors = np.linalg.eigh(A)
        principal_vector = eigenvectors[:, -1]

    scores = np.abs(principal_vector)

    degrees = compute_degree(A)
    neighbor_scores = compute_neighbor_importance(A, scores)

    results, final_scores = classify_nodes(scores, degrees, neighbor_scores)

    print("\n--- Final Results ---")
    for i, node in enumerate(node_labels):
        print(f"{node} → {results[i]}")

    visualize_graph(G, results, node_labels)
    export_results(args.output, node_labels, results, final_scores)


if __name__ == "__main__":
    main()