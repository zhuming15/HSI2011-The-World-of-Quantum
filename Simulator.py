from BellInequality import *
from QuantumSystem import *
from EPRSystem import *

############# EPR Model #################
print("---EPR Model---")

#Initialize EPR Model
EPRModel = EPRSystem()

# Define the measurement outcomes for each particle and observable
AL, AR, BL, BR = EPRModel.generate_EPR_result()

# Compute Bell Inequality of the dataset
EPR_Model = BellInequality(AL, AR, BL, BR)
EPR_Model.compute_Bell_Inequality()
print("\n")

############# Quantum Model #################
print("---Quantum Model---")

# Initialize Quantum Model
QuantumModel = QuantumSystem(0, math.pi/3, math.pi/4, -math.pi/4)

# Define the measurement outcomes for each particle and observable
QAL, QAR, QBL, QBR = QuantumModel.generate_quantum_result(1000)

# Compute Bell Inequality of the dataset
Q_Model = BellInequality(QAL, QAR, QBL, QBR)
Q_Model.compute_Bell_Inequality()
