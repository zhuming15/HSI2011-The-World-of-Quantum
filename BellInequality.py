import numpy as np

class BellInequality():
    def __init__(self, AL, AR, BL, BR):
        self.AL = np.array(AL);
        self.AR = np.array(AR);
        self.BL = np.array(BL);
        self.BR = np.array(BR);

    def compute_avg_of_event(self, event, string):
        counterN = 0
        counterP = 0
        for outcome in event:
            if outcome == -1:
                counterN += 1
            elif outcome == +1:
                counterP += 1
        total = counterN + counterP
        probSame = counterP/total
        probDiff = counterN/total
        expectation = probSame - probDiff
        print(f"{string} +1 : {probSame}")
        print(f"{string} -1 : {probDiff}")
        print(f"expectation : {expectation}")
        print("----------------------------")
        return expectation

    def compute_Bell_Inequality(self):
        # Calculate the correlations between the observables for each particle
        ABLL = self.AL * self.BL
        ABLR = self.AL * self.BR
        ABRL = self.AR * self.BL
        ABRR = self.AR * self.BR

        # Print dataset
        self.print_dataset()
        print("----------------------------")

        # Print correlations
        print(f"AL * BL : {ABLL}")
        print(f"AL * BR : {ABLR}")
        print(f"AR * BL : {ABRL}")
        print(f"AR * BR : {ABRR}")
        print("----------------------------")

        # Calculate the average correlations
        ABLL_avg = self.compute_avg_of_event(ABLL, "ABLL")
        ABLR_avg = self.compute_avg_of_event(ABLR, "ABLR")
        ABRL_avg = self.compute_avg_of_event(ABRL, "ABRL")
        ABRR_avg = self.compute_avg_of_event(ABRR, "ABRR")

        # Calculate the <S>
        S = ABLL_avg + ABLR_avg + ABRL_avg - ABRR_avg
        print(f"<S> = {ABLL_avg} + {ABLR_avg} + {ABRL_avg} - ({ABRR_avg}) = {S}")
        print(f"The value of <S> is {S}")

        # Check if S violates the Bell inequality
        if S > 2.82:
            print("Invalid result, exceed Bell Inequality boundary")
        elif S > 2:
            print("The system violates the Bell inequality and exhibits quantum behavior.")
        else:
            print("The system satisfies the Bell inequality and exhibits classical behavior.")

    def print_dataset(self):
        print(f"AL : {self.AL}")
        print(f"AR : {self.AR}")
        print(f"BL : {self.BL}")
        print(f"BR : {self.BR}")
