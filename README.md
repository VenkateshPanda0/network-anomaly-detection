# Graph-Based Network Anomaly Detection

<p align="center">

**A graph-theoretic network anomaly detection framework that leverages linear algebra and spectral analysis to identify anomalous communication patterns in network traffic.**

Built to explore how graph analytics can complement traditional intrusion detection systems while demonstrating practical applications of graph theory in cybersecurity.

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux-success)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Active%20Development-orange)

</p>

---

# Overview

Graph-Based Network Anomaly Detection is a cybersecurity analysis platform that models network communication as a graph and applies spectral graph analysis to identify suspicious hosts.

Instead of inspecting packet payloads, the system analyzes the communication topology between devices. Each communicating host becomes a graph node while every observed communication forms a graph edge.

Using Eigenvector Centrality and graph connectivity analysis, the project estimates the structural importance of each node and identifies abnormal communication behavior.

The project demonstrates how graph theory and linear algebra can be applied to practical cybersecurity problems.

---

# Why This Project

Traditional intrusion detection systems rely heavily on signatures, payload inspection, or statistical thresholds.

This project explores an alternative approach by asking:

> **Can anomalous network behavior be detected using only communication structure?**

Rather than analyzing packet contents, the detector focuses on graph topology, enabling network analysis even when payload inspection is unavailable or encrypted.

---

# Key Features

## Network Graph Construction

- Builds communication graphs from captured network traffic
- Represents devices as graph nodes
- Represents communication as graph edges
- Automatically generates adjacency matrices

---

## Spectral Analysis

- Eigenvector Centrality computation
- Node importance estimation
- Connectivity analysis
- Graph-based anomaly scoring

---

## Data Sources

Supports

- Live packet capture using Scapy
- Offline CSV datasets

---

## Network Classification

Automatically classifies hosts as

- Normal
- Weak Anomaly
- Suspicious

based on graph connectivity characteristics.

---

## Visualization

Generates

- Network topology graphs
- Node importance visualization
- Color-coded anomaly highlighting

---

## Export

Produces

- CSV analysis reports
- Node classification results
- Centrality scores

---

# System Architecture

```text
                    User
                      │
                      ▼
             Packet Collection
         (Scapy / CSV Datasets)
                      │
                      ▼
          Graph Construction Engine
                      │
                      ▼
             Adjacency Matrix
                      │
                      ▼
         Spectral Analysis Engine
      (Eigenvector Centrality)
                      │
                      ▼
          Anomaly Classification
                      │
          ┌───────────┴───────────┐
          ▼                       ▼
 Visualization Module      CSV Report Export
```

The modular pipeline separates data collection, graph generation, mathematical analysis, visualization, and reporting into independent components, making the project easy to extend with additional graph algorithms.

---

# Engineering Highlights

This project demonstrates

- Graph Theory
- Linear Algebra
- Spectral Graph Analysis
- Network Traffic Processing
- Algorithm Design
- Python Software Engineering
- Cybersecurity
- Data Visualization
- Modular Architecture

---

# Technology Stack

### Language

- Python

### Libraries

- NetworkX
- NumPy
- Scapy
- Matplotlib

---

# Typical Workflow

```text
Capture Network Traffic
         │
         ▼
Build Communication Graph
         │
         ▼
Generate Adjacency Matrix
         │
         ▼
Compute Eigenvector Centrality
         │
         ▼
Classify Network Nodes
         │
         ▼
Visualize Results
         │
         ▼
Export CSV Report
```

---

# Project Structure

```text
network-anomaly-detection/

├── main.py
├── graph_builder.py
├── anomaly_detector.py
├── packet_capture.py
├── visualization.py
├── utils.py
├── test_data/
├── results/
├── docs/
├── requirements.txt
├── README.md
└── LICENSE
```

---

# Why This Project Matters

Modern enterprise networks generate massive amounts of traffic every second.

This project explores how graph-theoretic analysis can reveal suspicious communication patterns without relying on packet payload inspection.

By combining graph construction, adjacency matrix generation, and Eigenvector Centrality, the detector provides an explainable mathematical approach to anomaly detection.

Beyond cybersecurity, the project demonstrates practical applications of

- Graph Theory
- Linear Algebra
- Network Analysis
- Algorithm Design
- Python Engineering

---

# Future Roadmap

Planned improvements include

- PageRank-based anomaly scoring
- Betweenness Centrality comparison
- Closeness Centrality comparison
- Community detection
- PCAP support
- Interactive Plotly visualization
- Real-time dashboard
- Docker deployment
- REST API
- Automated benchmarking
- Unit testing
- CI/CD pipeline

---

# Testing

Current testing includes

- Graph construction
- CSV parsing
- Live packet capture
- Eigenvector computation
- Node classification
- Result generation

Future improvements include

- Automated unit testing
- Integration testing
- Performance benchmarking
- Large-scale dataset evaluation

---

# Installation

```bash
git clone https://github.com/VenkateshPanda0/network-anomaly-detection.git

cd network-anomaly-detection

pip install -r requirements.txt

python main.py
```

---

# License

Released under the MIT License.

---

# Recruiter Notes

This project demonstrates practical experience in

- Graph-Based Network Analysis
- Cybersecurity Engineering
- Linear Algebra Applications
- Spectral Graph Analysis
- Python Software Development
- Network Traffic Processing
- Algorithm Design
- Data Visualization
- Modular Software Architecture

The objective is not to replace traditional intrusion detection systems, but to explore how graph-theoretic techniques can provide an explainable and extensible approach to identifying anomalous communication patterns.
