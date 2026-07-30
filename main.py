# Gym-diet-and-protien-tracker
import json

# Food protein data (per 100g or per unit approx)
food_data = {
    "milk": 3.4,
    "roti": 3,
    "dal": 9,
    "rice": 2.7,
    "soy_chunks": 52,
    "peanut": 26,
    "oats": 13,
    "banana": 1.1
}

FILE = "data.json"


# Load previous data
def load_data():
    try:
        with open(FILE, "r") as f:
            return json.load(f)
    except:
        return []


# Save data
def save_data(data):
    with open(FILE, "w") as f:
        json.dump(data, f, indent=4)


# Add meal
def add_meal():
    data = load_data()

    food = input("Enter food name: ").lower()

    if food not in food_data:
        print("❌ Food not found in database!")
        return

    qty = float(input("Enter quantity (in grams): "))

    protein = (food_data[food] * qty) / 100

    entry = {
        "food": food,
        "quantity": qty,
        "protein": protein
    }

    data.append(entry)
    save_data(data)

    print(f"✅ Added! Protein: {protein:.2f}g")


# View all meals
def view_meals():
    data = load_data()

    if not data:
        print("No data found!")
        return

    total = 0

    print("\n📋 Daily Meals:\n")

    for item in data:
        print(f"{item['food']} - {item['quantity']}g → {item['protein']:.2f}g protein")
        total += item['protein']

    print(f"\n💪 Total Protein: {total:.2f}g")


# Set goal & check remaining
def protein_goal():
    goal = float(input("Enter your daily protein goal: "))
    data = load_data()

    total = sum(item["protein"] for item in data)

    remaining = goal - total

    print(f"\n🎯 Goal: {goal}g")
    print(f"💪 Consumed: {total:.2f}g")

    if remaining > 0:
        print(f"⚠️ Remaining: {remaining:.2f}g")
    else:
        print("🔥 Goal Achieved!")


# Main menu
def main():
    while True:
        print("\n===== GYM DIET TRACKER =====")
        print("1. Add Meal")
        print("2. View Meals")
        print("3. Check Protein Goal")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_meal()
        elif choice == "2":
            view_meals()
        elif choice == "3":
            protein_goal()
        elif choice == "4":
            print("👋 Exiting...")
            break
        else:
            print("❌ Invalid choice!")


main()
