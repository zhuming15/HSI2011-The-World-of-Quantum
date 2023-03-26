import numpy as np
import random
import math

class QuantumSystem:
    def __init__(self, angle_a0, angle_a1, angle_b0, angle_b1):
        # Define angles
        self.a0 = angle_a0
        self.a1 = angle_a1
        self.b0 = angle_b0
        self.b1 = angle_b1
        
    # Define the probability function
    def cos_prob(self, x, y):
        return math.cos((x-y)/2)**2

    def sin_prob(self, x, y):
        return math.sin((x-y)/2)**2


    # Michelson Interferometer Model to generate data
    def generate_quantum_result(self, i):
        # Initialize list to store result
        QAL, QAR, QBL, QBR = [], [], [], []

        # Define angles 
        a0 = self.a0
        a1 = self.a1
        b0 = self.b0
        b1 = self.b1

        # Define probability function
        cos_prob = self.cos_prob
        sin_prob = self.sin_prob

        # Probability of each possible outcome
        AB00 = cos_prob(a0,b0)
        AB11 = cos_prob(a1,b1)
        AB10 = cos_prob(a1,b0)
        AB01 = cos_prob(a0,b1)
        ab11 = sin_prob(a1,b1)
        ab00 = sin_prob(a0,b0)
        ab10 = sin_prob(a1,b0)
        ab01 = sin_prob(a0,b1)

        # Store all probability in list
        probDistribution = [AB00, AB11, AB10, AB01, ab11, ab00, ab10, ab01]

        # Generate sequence of outcome
        results = random.choices(["LL", "RR", "RL", "LR", "rr", "ll", "rl", "lr"], probDistribution, k = i)

        # Append measurement outcome to respective list
        for result in results:
            outcome = random.choice([-1, +1])
            pair = random.randint(0,1)
            if result == "LL":
                QAL.append(outcome)
                QBL.append(outcome)
                QAR.append(0)
                QBR.append(0)
            elif result == "RR":
                QAR.append(outcome)
                QBR.append(outcome)
                QAL.append(0)
                QBL.append(0)
            elif result == "LR":
                QAL.append(outcome)
                QBR.append(outcome)
                QAR.append(0)
                QBL.append(0)
            elif result == "RL":
                QAR.append(outcome)
                QBL.append(outcome)
                QAL.append(0)
                QBR.append(0)
            elif result == "rr":
                if pair:
                    QAR.append(outcome)
                    QBR.append(-outcome)
                    QAL.append(0)
                    QBL.append(0)
                else:
                    QAR.append(-outcome)
                    QBR.append(outcome)
                    QAL.append(0)
                    QBL.append(0)
            elif result == "ll":
                if pair:
                    QAL.append(outcome)
                    QBL.append(-outcome)
                    QAR.append(0)
                    QBR.append(0)
                else:
                    QAL.append(-outcome)
                    QBL.append(outcome)
                    QAR.append(0)
                    QBR.append(0)
            elif result == "rl":
                if pair:
                    QAR.append(outcome)
                    QBL.append(-outcome)
                    QAL.append(0)
                    QBR.append(0)
                else:
                    QAR.append(-outcome)
                    QBL.append(outcome)
                    QAL.append(0)
                    QBR.append(0)
            else:
                if pair:
                    QAL.append(outcome)
                    QBR.append(-outcome)
                    QAR.append(0)
                    QBL.append(0)
                else:
                    QAL.append(-outcome)
                    QBR.append(outcome)
                    QAR.append(0)
                    QBL.append(0)
        return (QAL, QAR, QBL, QBR)
