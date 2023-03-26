import random

# Dataset for EPR Model
def generate_EPR_result():
    AL = [ 0, 0,-1, 0,+1,-1,+1, 0,-1,-1]
    AR = [-1,+1, 0,-1, 0, 0, 0,+1, 0, 0]
    BL = [+1,+1,+1, 0,-1, 0,-1, 0, 0,+1]
    BR = [ 0, 0, 0,+1, 0,-1, 0,-1,+1, 0]
    return (AL, AR, BL, BR)


def generate_EPR_result_(i):
    # Initialize list to store result
    AL, AR, BL, BR = [], [], [], []
    
    # Append measurement outcome to respective list
    for result in range(i):
        outcome1 = random.choice([-1, +1])
        outcome2 = random.choice([-1, +1])
        observable1 = random.randint(0,1)# 1->L
        observable2 = random.randint(0,1)
        if observable1 and observable2:
            AL.append(outcome1)
            BL.append(-outcome1)
            AR.append(0)
            BR.append(0)
        elif not observable1 and not observable2:
            AR.append(outcome2)
            BR.append(-outcome2)
            AL.append(0)
            BL.append(0)
        elif observable1 and not observable2:
            AL.append(outcome1)
            BR.append(outcome2)
            AR.append(0)
            BL.append(0)
        else:
            AR.append(outcome1)
            BL.append(outcome2)
            AL.append(0)
            BR.append(0)
    return (AL, AR, BL, BR)
