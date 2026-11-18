
def allocate_tables(guests):
    print("\n========== TABLE ALLOCATION ==========")

    confirmed_guests = [
        guest for guest in guests
        if guest["rsvp"] == "Confirmed"
    ]

    if not confirmed_guests:
        print("No confirmed guests available for seating.")
        return None

    try:
        capacity = int(input("Enter table capacity: "))

        if capacity <= 0:
            print("Table capacity must be greater than zero.")
            return None

    except ValueError:
        print("Please enter a valid number.")
        return None

    # Group guests by group name
    groups = {}

    for guest in confirmed_guests:
        group_name = guest["group_name"]

        if group_name not in groups:
            groups[group_name] = []

        groups[group_name].append(guest)

    tables = []

    # Track groups that are split across tables
    split_groups = []

    # Allocate guests group by group
    for group_name, members in groups.items():

        remaining_members = members.copy()

        while remaining_members:

            # Find an existing table with enough space
            available_table = None

            for table in tables:
                if len(table) < capacity:
                    available_table = table
                    break

            if available_table is not None:

                seats_available = capacity - len(available_table)

                guests_to_add = remaining_members[:seats_available]

                available_table.extend(guests_to_add)

                remaining_members = remaining_members[len(guests_to_add):]

                if remaining_members and group_name not in split_groups:
                    split_groups.append(group_name)

            else:

                guests_to_add = remaining_members[:capacity]

                tables.append(guests_to_add)

                remaining_members = remaining_members[len(guests_to_add):]

                if remaining_members and group_name not in split_groups:
                    split_groups.append(group_name)

    print("\nTable allocation completed successfully!")

    # Display allocation summary
    print("\n========== ALLOCATION SUMMARY ==========")

    total_guests = len(confirmed_guests)
    total_tables = len(tables)

    print("Total Confirmed Guests :", total_guests)
    print("Table Capacity         :", capacity)
    print("Tables Required        :", total_tables)

    print("\nGroup Allocation:")
    print("----------------------------------------")

    for group_name, members in groups.items():
        print(f"{group_name:<25}: {len(members)} Guests")

    print("----------------------------------------")

    print("Groups Split Across Tables:", len(split_groups))

    if split_groups:
        print("\nSplit Groups:")
        for group_name in split_groups:
            print("-", group_name)
    else:
        print("All groups were kept together.")

    print("\nTable Utilization:")
    print("----------------------------------------")

    for i, table in enumerate(tables, start=1):
        occupied = len(table)
        available = capacity - occupied

        print(
            f"Table {i}: {occupied}/{capacity} occupied "
            f"| {available} seats available"
        )

    print("----------------------------------------")

    print("Total Seats Available:", total_tables * capacity)
    print("Total Empty Seats    :", total_tables * capacity - total_guests)

    print("All tables are within capacity.")
    print("========================================")

    return tables, capacity
