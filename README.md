# 📌 Network Anomaly Detection using Linear Algebra

## 🚀 Features
- Graph-based anomaly detection using linear algebra  
- Eigenvector centrality for node importance  
- Supports live packet capture (Scapy) and CSV input  
- Classifies nodes as Normal, Weak Anomaly, or Suspicious  

---

## 📖 Overview
This project models network communication as a graph and applies **eigenvector-based analysis** to detect structural anomalies in network traffic.

---

## ⚙️ How It Works
```
Network Data → Graph → Adjacency Matrix → Eigenvector Analysis → Classification
```

- Nodes = devices/IPs  
- Edges = connections  
- Eigenvector centrality → importance score  
- Abnormal patterns → anomalies  

---

## 📦 Requirements
```
pip install numpy networkx matplotlib scapy
```

---

## 🚀 Usage

### CSV Mode
```
python main.py --mode file --input test_data/normal.csv
python main.py --mode file --input test_data/weak.csv
python main.py --mode file --input test_data/suspicious.csv
python main.py --mode file --input test_data/mixed.csv
```

### Live Mode
```
python main.py --mode live
```

*(Run as Administrator for live mode)*

---

## 📊 Output
- 🔵 Normal  
- 🟠 Weak Anomaly  
- 🔴 Suspicious  

Results are saved to `results.csv`.

---

## ⚠️ Limitations
- Uses network structure (no packet payload analysis)  
- Not a full intrusion detection system  

---

## 🎯 Key Idea
Uses **eigenvector centrality (linear algebra)** to identify abnormal connectivity patterns in network graphs.
