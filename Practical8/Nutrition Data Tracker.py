class food_item:
    def __init__(self, name, calories, protein, carbs, fat):
        self.name = name
        self.calories = calories
        self.protein = protein
        self.carbs = carbs
        self.fat = fat
    
    def __repr__(self):
        return f"{self.name}: {self.calories} kcal, P:{self.protein}g, C:{self.carbs}g, F:{self.fat}g"


def calculate_nutrition(consumed_items):
    total_calories = sum(item.calories for item in consumed_items)
    total_protein = sum(item.protein for item in consumed_items)
    total_carbs = sum(item.carbs for item in consumed_items)
    total_fat = sum(item.fat for item in consumed_items)

    print("=" * 50)
    print("NUTRITION REPORT (24-hour period)")
    print("=" * 50)
    print(f"Total calories:     {total_calories} kcal")
    print(f"Total protein:      {total_protein} g")
    print(f"Total carbohydrates: {total_carbs} g")
    print(f"Total fat:          {total_fat} g")
    print("-" * 50)
    
    warnings = []
    if total_calories > 2500:
        warnings.append(f"WARNING: Exceeded 2500 calories (Current: {total_calories} kcal)")
    if total_fat > 90:
        warnings.append(f"WARNING: Exceeded 90g fat (Current: {total_fat} g)")
    
    if warnings:
        print("WARNINGS:")
        for w in warnings:
            print(f"  ⚠️ {w}")
    else:
        print("✅ No warnings. Intake is within recommended limits.")
    print("=" * 50)
    
    return {
        'calories': total_calories,
        'protein': total_protein,
        'carbs': total_carbs,
        'fat': total_fat
    }

#示例
if __name__ == "__main__":
    
    print("\n" + "=" * 50)
    print("EXAMPLE: Daily Meal Tracking")
    print("=" * 50 + "\n")
    
    breakfast = food_item("Apple", 60, 0.3, 15, 0.5)
    lunch = food_item("Chicken Sandwich", 450, 30, 40, 15)
    dinner = food_item("Pasta with Sauce", 700, 20, 90, 10)
    snack = food_item("Protein Bar", 220, 15, 25, 7)
    
    consumed_today = [breakfast, lunch, dinner, snack]
    
    print("Food items consumed today:")
    for food in consumed_today:
        print(f"  - {food}")
    
    print("\n" + "-" * 50 + "\n")
  
    result = calculate_nutrition(consumed_today)
    