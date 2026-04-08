📌 Network Anomaly Detection using Linear Algebra
📖 Overview

This project implements a graph-based network anomaly detection system using concepts from Linear Algebra. It analyzes communication patterns between devices in a network and identifies unusual behavior such as:

Weakly connected nodes (potential inactive or isolated devices)
Suspicious nodes (unusual communication patterns)

The system supports both:

Real-time network traffic analysis
Offline analysis using CSV datasets




🎯 Objective

To demonstrate how linear algebra techniques (eigenvalues and eigenvectors) can be applied to solve real-world problems in computer science and cybersecurity, specifically:

Representing networks as graphs
Converting graphs into matrices
Using eigenvector-based metrics to detect anomalies





⚙️ How the System Works

The system follows a structured pipeline:

Network Data → Graph → Matrix → Linear Algebra → Classification
🔹 Step 1: Data Input

Two modes are supported:

Live Mode
Captures real-time network packets
Extracts source and destination IPs
File Mode
Reads data from CSV files

Format:

source,target,weight
A,B,3
B,C,2
🔹 Step 2: Graph Construction
Each device (IP/node) → vertex
Each connection → edge
Edge weight → number of interactions
🔹 Step 3: Matrix Representation

The graph is converted into an adjacency matrix:

A[i][j] = weight of connection between node i and j
🔹 Step 4: Linear Algebra Analysis
Compute eigenvalues and eigenvectors
Extract principal eigenvector
This gives node importance (centrality score)
🔹 Step 5: Feature Extraction

For each node:

Score → eigenvector importance
Degree → number of connections
Neighbor Score → importance of connected nodes

All features are normalized.

🔹 Step 6: Classification

Nodes are classified into:

Type	Meaning
Normal	Regular network behavior
Weak Anomaly	Low connectivity / isolated node
Suspicious	Unusual connection pattern




🚀 How to Run
🔹 1. Install Dependencies
pip install numpy networkx matplotlib scapy
🔹 2. Run with CSV (Recommended for testing)
python main.py --mode file --input test_data/normal.csv
python main.py --mode file --input test_data/weak.csv
python main.py --mode file --input test_data/suspicious.csv
python main.py --mode file --input test_data/mixed.csv
🔹 3. Run in Live Mode (Real Network)
python main.py --mode live




⚠ Requirements:

Run terminal as Administrator
Internet connection required




📊 Expected Output
Terminal Output
--- Node Features ---
Node 0: Score=0.700, Degree=0.800, Neighbor=0.102

--- Final Results ---
A → Normal
B → Weak Anomaly
C → Suspicious
Graph Visualization
🔵 Blue → Normal
🟠 Orange → Weak Anomaly
🔴 Red → Suspicious
CSV Export

Results are saved in:

results.csv

Format:

node,label,score
A,Normal,0.72
B,Weak Anomaly,0.12



🧪 Testing Strategy

The system was tested using:

✔ Synthetic datasets (normal, weak, suspicious, mixed)
✔ Real-world live packet capture
✔ Different traffic conditions


🧠 Key Observations
Real-world traffic includes noise (broadcast/multicast)
Sparse graphs may produce low eigen scores
The system prioritizes reducing false positives



⚠️ Limitations

This is an academic prototype:

❌ Does not inspect packet contents
❌ Not a full intrusion detection system
✔ Focuses on structural anomalies in network graphs
📌 Applications
Network monitoring
Anomaly detection
Graph-based data analysis
Cybersecurity research




🧑‍💻 Project Structure
network-anomaly-detection/
│
├── main.py
├── test_data/
│   ├── normal.csv
│   ├── weak.csv
│   ├── suspicious.csv
│   └── mixed.csv
├── results.csv
└── README.md



🎓 Academic Relevance

This project demonstrates:

Application of Linear Algebra
Use of Eigenvalues & Eigenvectors
Graph theory in computer science
Real-world system design





🧾 Conclusion

This project successfully shows how mathematical concepts from linear algebra can be applied to analyze real-world network data and detect anomalies using a structured and scalable approach.