# ⚛️ Mdaedalus Quantum Bell State Experiment

**Mdaedalus Quantum Bell State Experiment** demonstrates a simple **two-qubit quantum circuit** executed on an **IBM Quantum computer** using **Qiskit**.

The circuit prepares a **Bell state**, executes it on the selected IBM Quantum backend, and visualizes the measurement results as a histogram.

---

## 🚀 Features

- Uses **Qiskit** to construct a 2-qubit entangled circuit
- Executes the experiment on **IBM Quantum backends** (real or simulated)
- Visualizes the measurement histogram
- Displays available devices and their qubit counts
- Automatically reads your IBM Quantum **API token** from `token.txt`

---

## 📂 Project Structure

mdaedalus_quantum_bell/
├── mdaedalus_quantum_bell.py
├── token.txt
└── README.md


---

## ⚙️ Requirements

Install dependencies using pip:

```bash
pip install qiskit matplotlib
