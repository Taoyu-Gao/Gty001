import matplotlib.pyplot as plt
import numpy as np

print("\n" + "=" * 50)
print("3. POPULATION GROWTH RATE ANALYSIS")
print("=" * 50)

# 人口数据（单位：百万）
population_data = {
    'UK': {'2020': 66.7, '2024': 69.2},
    'China': {'2020': 1426, '2024': 1410},
    'Italy': {'2020': 59.4, '2024': 58.9},
    'Brazil': {'2020': 208.6, '2024': 212.0},
    'USA': {'2020': 331.6, '2024': 340.1}
}

print("\n📊 Population Data (millions):")
print("-" * 50)
print(f"{'Country':<10} {'2020':<12} {'2024':<12} {'Change %':<10}")
print("-" * 50)

# 计算百分比变化
percent_changes = {}

for country, years in population_data.items():
    pop_2020 = years['2020']
    pop_2024 = years['2024']
    
    # 计算百分比变化
    percent_change = ((pop_2024 - pop_2020) / pop_2020) * 100
    percent_changes[country] = percent_change
    
    # 打印结果
    print(f"{country:<10} {pop_2020:<12.1f} {pop_2024:<12.1f} {percent_change:>+8.2f}%")

print("-" * 50)

# 按百分比变化排序（从大到小）
sorted_changes = sorted(percent_changes.items(), key=lambda x: x[1], reverse=True)

print(f"\n📈 Population Changes (sorted from largest increase to largest decrease):")
print("-" * 50)
for country, change in sorted_changes:
    arrow = "▲" if change > 0 else "▼"
    print(f"   {country:<10}: {arrow} {change:>+6.2f}%")

# 找出最大增长和最大下降的国家
largest_increase = sorted_changes[0]      # 第一个是最大增长
largest_decrease = sorted_changes[-1]     # 最后一个是最小增长（最大下降）

print(f"\n🏆 Largest population increase: {largest_increase[0]} ({largest_increase[1]:+.2f}%)")
print(f"📉 Largest population decrease: {largest_decrease[0]} ({largest_decrease[1]:+.2f}%)")

# 创建柱形图
countries = list(percent_changes.keys())
changes = list(percent_changes.values())

plt.figure(figsize=(12, 6))

# 根据正负值设置不同颜色
colors = ['green' if x >= 0 else 'red' for x in changes]
bars = plt.bar(countries, changes, color=colors, edgecolor='black', linewidth=1.2)

# 添加标题和标签
plt.title('Population Growth Rate by Country (2020-2024)', fontsize=16, fontweight='bold')
plt.xlabel('Country', fontsize=12)
plt.ylabel('Population Change (%)', fontsize=12)
plt.axhline(y=0, color='black', linestyle='-', linewidth=0.5)  # 添加零线

# 在柱子上添加数值标签
for bar, change in zip(bars, changes):
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., 
             height + (0.2 if height >= 0 else -0.8),
             f'{change:+.2f}%', ha='center', va='bottom' if height >= 0 else 'top',
             fontsize=10, fontweight='bold')

plt.grid(axis='y', alpha=0.3, linestyle='--')
plt.tight_layout()
plt.savefig('population_growth.png', dpi=300, bbox_inches='tight')
plt.show()
print("\n✅ Bar chart saved as 'population_growth.png'")

print("\n" + "=" * 50)
print("🎉 PRACTICAL 5 COMPLETED!")
print("=" * 50)