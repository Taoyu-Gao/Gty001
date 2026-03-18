# creatine_clearance.py
# Cockcroft-Gault Equation for kidney function assessment

# PSEUDOCODE:
# 1. Store input values: age, weight, gender, creatine concentration
# 2. Check if all inputs are within valid ranges:
#    - age < 100
#    - 20 < weight < 80
#    - 0 < creatine < 100
#    - gender is either 'male' or 'female'
# 3. If any input is invalid:
#    - Print error message specifying which variable needs correction
# 4. If all inputs are valid:
#    - Calculate CrCl using formula
#    - Apply 0.85 factor if female
#    - Print result

# Input values (you can change these to test)
age = 25           # years
weight = 70        # kg
gender = "male"    # "male" or "female"
creatine = 80      # μmol/l

print("Creatine Clearance Calculator")
print("-" * 30)
print(f"Age: {age} years")
print(f"Weight: {weight} kg")
print(f"Gender: {gender}")
print(f"Creatine: {creatine} μmol/l")
print("-" * 30)

# Check for valid inputs
valid = True
error_messages = []

# Check age
if age >= 100:
    valid = False
    error_messages.append("Age must be less than 100 years")

# Check weight
if weight <= 20:
    valid = False
    error_messages.append("Weight must be greater than 20 kg")
elif weight >= 80:
    valid = False
    error_messages.append("Weight must be less than 80 kg")

# Check creatine concentration
if creatine <= 0:
    valid = False
    error_messages.append("Creatine concentration must be greater than 0 μmol/l")
elif creatine >= 100:
    valid = False
    error_messages.append("Creatine concentration must be less than 100 μmol/l")

# Check gender
if gender != "male" and gender != "female":
    valid = False
    error_messages.append("Gender must be either 'male' or 'female'")

# If inputs are invalid, print errors
if not valid:
    print("ERROR: Invalid input(s) detected!")
    for message in error_messages:
        print(f"- {message}")
    print("Cannot calculate CrCl. Please correct the above values.")

# If inputs are valid, calculate CrCl
else:
    # Calculate CrCl using formula: (140 - age) * weight / (72 * creatine)
    crcl = (140 - age) * weight / (72 * creatine)
    
    # Apply gender factor (0.85 if female)
    if gender == "female":
        crcl = crcl * 0.85
        print("Gender factor applied: 0.85")
    
    print(f"\nCreatine Clearance Rate (CrCl) = {crcl:.2f} ml/min")
    
    # Optional: Add interpretation
    print("\nInterpretation:")
    if crcl > 90:
        print("Normal kidney function")
    elif crcl > 60:
        print("Mild decrease in kidney function")
    elif crcl > 30:
        print("Moderate decrease in kidney function")
    elif crcl > 15:
        print("Severe decrease in kidney function")
    else:
        print("Kidney failure")
