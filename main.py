
from guest_manager import (
    add_guest,
    view_guests,
    search_guest,
    update_guest
)

from rsvp_manager import (
    update_rsvp,
    confirmed_headcount
)

from seating_manager import allocate_tables

from catering_manager import meal_summary

from seating_chart import print_seating_chart


# Shared in-memory guest storage
guests = []

# Seating information
tables = None
table_capacity = None


def display_menu():

    print("\n" + "=" * 45)
    print("                  GUESTGRID")
    print("       EVENT GUEST & TABLE SEATING MANAGER")
    print("=" * 45)

    print("1.  Add New Guest")
    print("2.  View All Guests")
    print("3.  Search Guest")
    print("4.  Update Guest Details")
    print("5.  Update RSVP Status")
    print("6.  View Confirmed Headcount")
    print("7.  Allocate Guests to Tables")
    print("8.  View Meal Preference Summary")
    print("9.  Print Seating Chart")
    print("10. Exit")

    print("=" * 45)


def main():

    global tables, table_capacity

    while True:

        display_menu()

        choice = input("Enter your choice (1-10): ").strip()

        if choice == "1":
            add_guest(guests)
            tables = None

        elif choice == "2":
            view_guests(guests)

        elif choice == "3":
            search_guest(guests)

        elif choice == "4":
            update_guest(guests)
            tables = None

        elif choice == "5":
            update_rsvp(guests)
            tables = None

        elif choice == "6":
            confirmed_headcount(guests)

        elif choice == "7":
            result = allocate_tables(guests)

            if result is not None:
                tables, table_capacity = result

        elif choice == "8":
            meal_summary(guests)

        elif choice == "9":

            if tables is None:
                print("\nPlease allocate guests first!")
            else:
                print_seating_chart(tables, table_capacity)

        elif choice == "10":

            print("\nThank you for using GuestGrid!")
            print("Exiting application...")
            break

        else:
            print("\nInvalid choice! Please enter a number between 1 and 10.")


if __name__ == "__main__":
    main()
