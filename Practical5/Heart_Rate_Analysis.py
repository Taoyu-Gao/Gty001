import matplotlib.pyplot as plt

print("\n" + "=" * 50)
print("2. HEART RATE ANALYSIS")
print("=" * 50)

heart_rates = [72, 60, 126, 85, 90, 59, 76, 131, 88, 121, 64]

num_patients = len(heart_rates)
mean_heart_rate = sum(heart_rates) / num_patients
print(f"\n Dataset Statistics:")
print(f"   Number of patients: {num_patients}")
print(f"   Mean heart rate: {mean_heart_rate:.1f} bpm")
low_hr = []     
normal_hr = []  
high_hr = []     

for hr in heart_rates:
    if hr < 60:
        low_hr.append(hr)
    elif 60 <= hr <= 120:
        normal_hr.append(hr)
    else:
        high_hr.append(hr)
categories = {
    'Low (<60 bpm)': len(low_hr),
    'Normal (60-120 bpm)': len(normal_hr),
    'High (>120 bpm)': len(high_hr)
}

print(f"\n📈 Heart Rate Categories:")
for category, count in categories.items():
    print(f"   {category}: {count} patients")

largest_category = max(categories, key=categories.get)
print(f"\n Largest category: {largest_category} ({categories[largest_category]} patients)")

plt.figure(figsize=(8, 8))
colors = ['#ff9999', '#66b3ff', '#99ff99']
explode = (0.05, 0, 0.05) 
plt.pie(categories.values(), labels=categories.keys(), autopct='%1.1f%%', colors=colors, explode=explode, startangle=90, shadow=True)
plt.title('Heart Rate Distribution by Category', fontsize=16, fontweight='bold')
plt.axis('equal')  # 确保饼图是圆的

plt.tight_layout()
plt.savefig('heart_rate_pie_chart.png', dpi=300, bbox_inches='tight')
plt.show()
print("\n✅ Pie chart saved as 'heart_rate_pie_chart.png'")
