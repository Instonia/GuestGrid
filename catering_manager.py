
def meal_summary(guests):
    print("\n========== CATERING REPORT ==========")

    meals = {
        "Vegetarian": 0,
        "Non-Vegetarian": 0,
        "Vegan": 0,
        "Jain": 0
    }

    for guest in guests:

        if guest["rsvp"] == "Confirmed":
            meals[guest["meal"]] += 1

    print("\nMeal Preference       Headcount")
    print("--------------------------------")

    for meal, count in meals.items():
        print(f"{meal:<22} {count}")

    print("--------------------------------")

    print("Total Confirmed Guests:", sum(meals.values()))
