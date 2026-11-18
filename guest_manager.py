
def add_guest(guests):
    print("\n========== ADD NEW GUEST ==========")

    name = input("Enter guest name: ").strip()

    if not name:
        print("Guest name cannot be empty.")
        return

    group_type = input("Enter group type (Family/Friends): ").strip().title()

    if group_type not in ["Family", "Friends"]:
        print("Invalid group type.")
        return

    group_name = input("Enter group name (e.g. Sharma Family): ").strip()

    if not group_name:
        print("Group name cannot be empty.")
        return

    meal = input(
        "Enter meal preference (Vegetarian/Non-Vegetarian/Vegan/Jain): "
    ).strip().title().replace("-", "-")

    valid_meals = ["Vegetarian", "Non-Vegetarian", "Vegan", "Jain"]

    if meal not in valid_meals:
        print("Invalid meal preference.")
        return

    guest_id = f"G{len(guests) + 1:03d}"

    guest = {
        "id": guest_id,
        "name": name,
        "group_type": group_type,
        "group_name": group_name,
        "rsvp": "Pending",
        "meal": meal
    }

    guests.append(guest)

    print("\nGuest added successfully!")
    print("Guest ID:", guest_id)


def view_guests(guests):
    print("\n========== GUEST LIST ==========")

    if not guests:
        print("No guests registered yet.")
        return

    for guest in guests:
        print("--------------------------------")
        print("Guest ID :", guest["id"])
        print("Name     :", guest["name"])
        print("Group    :", guest["group_type"])
        print("Group Name:", guest["group_name"])
        print("RSVP     :", guest["rsvp"])
        print("Meal     :", guest["meal"])


def search_guest(guests):
    print("\n========== SEARCH GUEST ==========")

    guest_id = input("Enter Guest ID: ").strip().upper()

    for guest in guests:
        if guest["id"] == guest_id:
            print("\nGuest Found!")
            print("Name:", guest["name"])
            print("Group:", guest["group_name"])
            print("RSVP:", guest["rsvp"])
            print("Meal:", guest["meal"])
            return

    print("Guest not found.")


def update_guest(guests):
    print("\n========== UPDATE GUEST ==========")

    guest_id = input("Enter Guest ID: ").strip().upper()

    for guest in guests:
        if guest["id"] == guest_id:

            print("\n1. Update Name")
            print("2. Update Group")
            print("3. Update Meal Preference")

            choice = input("Enter your choice: ").strip()

            if choice == "1":
                name = input("Enter new name: ").strip()
                if name:
                    guest["name"] = name
                else:
                    print("Name cannot be empty.")
                    return

            elif choice == "2":
                group_type = input("Enter group type (Family/Friends): ").strip().title()

                if group_type not in ["Family", "Friends"]:
                    print("Invalid group type.")
                    return

                group_name = input("Enter new group name: ").strip()

                if not group_name:
                    print("Group name cannot be empty.")
                    return

                guest["group_type"] = group_type
                guest["group_name"] = group_name

            elif choice == "3":
                meal = input(
                    "Enter new meal preference (Vegetarian/Non-Vegetarian/Vegan/Jain): "
                ).strip().title()

                if meal not in ["Vegetarian", "Non-Vegetarian", "Vegan", "Jain"]:
                    print("Invalid meal preference.")
                    return

                guest["meal"] = meal

            else:
                print("Invalid choice.")
                return

            print("Guest details updated successfully!")
            return

    print("Guest not found.")
