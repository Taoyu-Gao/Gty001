# infection
from math import ceil
total_students=float(input("total student:"))
infected=float(input(f"\noriginal infected:"))
growth_rate=float(input(f"\nrate:"))
day=1
print("Simulating infection spread:")
print("Day 1: Infected =",(infected))
while infected<total_students:
    day=day+1
    new_infected=infected*(1+growth_rate)
    infected=ceil(new_infected)
    if infected>total_students:
        infected=total_students
    print(f"Day:{day}: infected={infected:.0f}")
print("\nIt took {day} days for all {total_students} students to become infected.")
print("(Final infected count: {infected})")
    
