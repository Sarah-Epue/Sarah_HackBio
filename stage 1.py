def translate_codon(input_codon):
    """
    Translates a RNA codon sequence into a protein sequence.

    Args:
        input_codon: A string representing the RNA codon sequence.

    Returns:
        A list of strings representing the protein sequence, or None if an
        error occurs.
    """

    codon_db = {
        "UUU": "Phe", "UUC": "Phe", "UUA": "Leu", "UUG": "Leu",
        "UCU": "Ser", "UCC": "Ser", "UCA": "Ser", "UCG": "Ser",
        "UAU": "Tyr", "UAC": "Tyr", "UAA": "Stop", "UAG": "Stop",
        "UGU": "Cys", "UGC": "Cys", "UGA": "Stop", "UGG": "Trp",
        "CUU": "Leu", "CUC": "Leu", "CUA": "Leu", "CUG": "Leu",
        "CCU": "Pro", "CCC": "Pro", "CCA": "Pro", "CCG": "Pro",
        "CAU": "His", "CAC": "His", "CAA": "Gln", "CAG": "Gln",
        "CGU": "Arg", "CGC": "Arg", "CGA": "Arg", "CGG": "Arg",
        "AUU": "Ile", "AUC": "Ile", "AUA": "Ile", "AUG": "Met",
        "ACU": "Thr", "ACC": "Thr", "ACA": "Thr", "ACG": "Thr",
        "AAU": "Asn", "AAC": "Asn", "AAA": "Lys", "AAG": "Lys",
        "AGU": "Ser", "AGC": "Ser", "AGA": "Arg", "AGG": "Arg",
        "GUU": "Val", "GUC": "Val", "GUA": "Val", "GUG": "Val",
        "GCU": "Ala", "GCC": "Ala", "GCA": "Ala", "GCG": "Ala",
        "GAU": "Asp", "GAC": "Asp", "GAA": "Glu", "GAG": "Glu",
        "GGU": "Gly", "GGC": "Gly", "GGA": "Gly", "GGG": "Gly"
    }

    if len(input_codon) % 3 != 0:
        return None  # Invalid input length

    protein_sequence = []
    for i in range(0, len(input_codon), 3):
        codon = input_codon[i:i + 3]
        if codon in codon_db:
            protein_sequence.append(codon_db[codon])
        else:
            return None  # Invalid codon found

    return protein_sequence

# Example usage
test_codon = "UUAUUAUUAUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUCUUCUUCUUCUUC"
result = translate_codon(test_codon)

if result:
    print(result)
else:
    print("Invalid codon sequence.")

import numpy as np
import matplotlib.pyplot as plt

def population_maker(k=2, x_mid=5, x=None):
    """
    Simulates population growth using a logistic function.

    Args:
        k: The growth rate parameter.
        x_mid: The midpoint of the growth curve.
        x: The input value(s) for the function. Can be a single number or a NumPy array.

    Returns:
        The population size(s) calculated by the logistic function.
    """
    if x is None:
        return None  # Handle case where x is not provided
    return 1 / (1 + np.exp(-k * (x - x_mid)))

od_600 = []
time_points = np.arange(0, 25) #creates an array from 0 to 24

for i in time_points:
    curr_od = population_maker(k=0.25, x_mid=10, x=i)
    od_600.append(curr_od)

# Plotting the results
plt.plot(time_points, od_600)
plt.xlabel("Time")
plt.ylabel("OD_600")
plt.title("Logistic Population Growth")
plt.show()

import math
import seaborn as sns
import matplotlib.pyplot as plt

def population_maker(x, k=2, x_mid=5):
    """
    Simulates population growth using a logistic function.

    Args:
        x: The input value for the function.
        k: The growth rate parameter.
        x_mid: The midpoint of the growth curve.

    Returns:
        The population size calculated by the logistic function.
    """
    solution = 1 / (1 + math.exp(-k * (x - x_mid)))
    return solution

od_600 = []

for i in range(0, 24):
    od_600.append(population_maker(x=i, k=0.5, x_mid=10))

#print(od_600)  # Optional: Print the OD values

sns.lineplot(x=range(0, 24), y=od_600)
plt.xlabel("Time") #add x label
plt.ylabel("OD_600") #add y label
plt.title("Logistic Growth Curve") #add graph title
plt.show() #show the plot
