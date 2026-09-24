from qiskit import QuantumCircuit
from qiskit.quantum_info import SparsePauliOp
from qiskit.transpiler import generate_preset_pass_manager
from qiskit_ibm_runtime import qiskit_runtime_service
from qiskit_ibm_runtime import EstimatorOptions
from qiskit_ibm_runtime import EstimatorV2 as Estimator
from matplotlib import pyplot as plt

#Criando Qubit
qc = QuantumCircuit(2)

#Aplicando porta Hadamard
qc.h(0)


qc.cx(0,1)

qc.draw("mpl").savefig("circuito.png")

observable_labels = ["IZ", "IX", "ZI", "XI", "ZZ", "XX"]
observable = [SparsePauliOp(label) for label in observable_labels]


