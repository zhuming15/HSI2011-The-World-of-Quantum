from BellInequality import *
from QuantumSystem import *
from EPRSystem import *

############# EPR Model #################
print("---EPR Model---")

# Define the measurement outcomes for each particle and observable
AL, AR, BL, BR = generate_EPR_result()

# Run model and compute Bell Inequality
EPR_Model = BellInequality(AL, AR, BL, BR)
EPR_Model.compute_Bell_Inequality()
print("\n")

############# Quantum Model #################
print("---Quantum Model---")

# Define the measurement outcomes for each particle and observable
QAL, QAR, QBL, QBR = generate_quantum_result(1000)

# Run Model and compute Bell Inequality
Q_Model = BellInequality(QAL, QAR, QBL, QBR)
Q_Model.compute_Bell_Inequality()

