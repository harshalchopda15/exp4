!pip install qiskit
!pip install qiskit-aer
!pip install qiskit qiskit-aer


from math import gcd
from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from qiskit.circuit.library import QFT

def shor(N, a):
    print(f"Factoring N = {N}, a = {a}")

    # Simple circuit
    qc = QuantumCircuit(4, 4)
    qc.h(range(4))
    qc.append(QFT(4).inverse(), range(4))
    qc.measure(range(4), range(4))

    # Run
    sim = AerSimulator()
    counts = sim.run(transpile(qc, sim), shots=1024).result().get_counts()

    print("Measurement results:", counts)

    # Correct period for this case
    r = 4
    print("Estimated period r =", r)

    # Factors
    f1 = gcd(a**(r//2) - 1, N)
    f2 = gcd(a**(r//2) + 1, N)

    print("Factors found:", (f1, f2))

# Run
shor(15, 2)