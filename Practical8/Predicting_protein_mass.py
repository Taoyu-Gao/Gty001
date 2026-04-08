import matplotlib.pyplot as plt
import numpy as np  
import os

mass_table = {
    'G': 57.02,
    'A': 71.04,
    'S': 87.03,
    'P': 97.05,
    'V': 99.07,
    'T': 101.05,
    'C': 103.01,
    'L': 113.08,
    'I': 113.08,
    'N': 114.04,
    'D': 115.03,
    'Q': 128.06,
    'K': 128.09,
    'E': 129.04,
    'M': 131.04,
    'H': 137.06,
    'F': 147.07,
    'R': 156.10,
    'Y': 163.06,
    'W': 186.08
}


def calculate_protein_mass(sequence):
    total_mass = sum(mass_table.get(aa, 0) for aa in sequence)
    return total_mass

protein_sequence = input("请输入蛋白质序列: ").strip().upper()
mass = calculate_protein_mass(protein_sequence)
print(f"蛋白质序列: {protein_sequence}")
print(f"蛋白质质量: {mass}")