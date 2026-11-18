
def print_seating_chart(tables, capacity):
    print("\n" + "=" * 45)
    print("             GUESTGRID")
    print("             SEATING CHART")
    print("=" * 45)

    if not tables:
        print("No seating arrangement available.")
        return

    total_guests = 0

    for i, table in enumerate(tables, start=1):

        print(f"\nTABLE {i}")
        print("-" * 35)

        for seat, guest in enumerate(table, start=1):
            print(f"{seat}. {guest['name']} ({guest['group_name']})")

        occupied = len(table)
        available = capacity - occupied

        total_guests += occupied

        print(f"\nOccupied Seats : {occupied}")
        print(f"Available Seats: {available}")

        if available == 0:
            print("Status: FULL")
        else:
            print("Status: AVAILABLE")

    print("\n" + "=" * 45)
    print("Total Confirmed Guests:", total_guests)
    print("Total Tables Used:", len(tables))
    print("=" * 45)
