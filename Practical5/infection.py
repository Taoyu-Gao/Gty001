# infection
from math import ceil
total_students=91
infected=5.0
growth_rate=0.40
day=1
print("Simulating infection spread:")
print("Day 1: Infected =",(infected))
while infected<total_students:
    day=day+1
    new_infected=infected*(1+growth_rate)
    infected=ceil(new_infected)
    if infected>total_students:
        infected=total_students
    print(f"Day:",day,"infected=",infected)
print(f"\nIt took {day} days for all {total_students} students to become infected.")
print(f"(Final infected count: {infected})")
    
