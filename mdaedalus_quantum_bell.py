# =====================================================
#  Mdaedalus Quantum Bell State Experiment (Qiskit)
# =====================================================

import qiskit as q
from qiskit import IBMQ
from qiskit.tools.monitor import job_monitor
from qiskit.visualization import plot_histogram
from matplotlib import style

# Display matplotlib output inline
# (In Jupyter notebooks, uncomment the following line)
# %matplotlib inline

# === Step 1: Define the Quantum Circuit ===
circuit = q.QuantumCircuit(2, 2)  # 2 qubits, 2 classical bits

# Apply quantum gates
circuit.x(0)        # Apply X (NOT) gate on the first qubit
circuit.cx(0, 1)    # Apply controlled-NOT gate (entangles qubits)
circuit.measure([0, 1], [0, 1])  # Measure qubits into classical bits

# Draw circuit
print("\nQuantum Circuit Structure:")
print(circuit.draw())
circuit.draw(output="mpl")  # matplotlib visualization

# === Step 2: Load IBM Quantum Account ===
try:
    with open("token.txt", "r") as token_file:
        IBMQ.save_account(token_file.read().strip(), overwrite=True)
except FileNotFoundError:
    print("[ERROR] token.txt not found. Please place your IBM Quantum API token in this file.")
    exit(1)

IBMQ.load_account()

# Get provider
provider = IBMQ.get_provider("ibm-q")

# Display available backends
print("\nAvailable IBM Quantum Backends:\n")
for backend in provider.backends():
    try:
        qubit_count = len(backend.properties().qubits)
    except Exception:
        qubit_count = "simulated"
    print(f"{backend.name():15} | Jobs Queued: {backend.status().pending_jobs:3} | Qubits: {qubit_count}")

# === Step 3: Select Backend and Execute ===
backend_name = "ibmq_quito"
backend = provider.get_backend(backend_name)
print(f"\nRunning on backend: {backend_name}\n")

job = q.execute(circuit, backend=backend, shots=500)
job_monitor(job)

# === Step 4: Retrieve Results and Visualize ===
result = job.result()
counts = result.get_counts(circuit)

# Use dark mode for visualization
style.use("dark_background")

print("\nMeasurement Results:")
print(counts)

plot_histogram([counts], legend=["Quantum Device"])

print("\nExecution Complete ✅")
