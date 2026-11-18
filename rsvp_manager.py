
def update_rsvp(guests):
    print("\n========== UPDATE RSVP ==========")

    guest_id = input("Enter Guest ID: ").strip().upper()

    for guest in guests:
        if guest["id"] == guest_id:

            print("\nCurrent RSVP:", guest["rsvp"])
            print("1. Confirmed")
            print("2. Declined")
            print("3. Pending")

            choice = input("Select new RSVP status: ").strip()

            statuses = {
                "1": "Confirmed",
                "2": "Declined",
                "3": "Pending"
            }

            if choice in statuses:
                guest["rsvp"] = statuses[choice]
                print("RSVP updated successfully!")
            else:
                print("Invalid choice.")

            return

    print("Guest not found.")


def confirmed_headcount(guests):
    confirmed = sum(
        1 for guest in guests
        if guest["rsvp"] == "Confirmed"
    )

    print("\n========== RSVP SUMMARY ==========")

    print("Total Registered Guests:", len(guests))
    print("Confirmed Guests:", confirmed)

    print(
        "Declined Guests:",
        sum(1 for guest in guests if guest["rsvp"] == "Declined")
    )

    print(
        "Pending Guests:",
        sum(1 for guest in guests if guest["rsvp"] == "Pending")
    )

    return confirmed
