# GuestGrid
Event Guest and Table Seating Manager

# CP-068 TrackPoint: GuestGrid: Event Guest and Table Seating Manager
## Team
Ravi K (1AT23CS045), Asha M (1AT23CS051), Java track

## How to run
python3 main.py

## Features that work

1. Guest Management: Add new guests, view all registered guests, search guests using their unique Guest ID and update guest details.

2. RSVP Management: Update guest RSVP status as Confirmed, Declined or Pending and calculate the total confirmed headcount.

3. Group-Based Table Allocation: Allocate confirmed guests to tables using a user-defined seating capacity. The system attempts to keep family and friends groups together while respecting table capacity constraints.

4. Seating Allocation Summary: Display total confirmed guests, table capacity, number of tables required, guest count by group, groups split across tables and table utilization.

5. Meal Preference Summary: Generate a catering headcount by calculating confirmed guests belonging to Vegetarian, Non-Vegetarian, Vegan and Jain categories.

6. Seating Chart: Display the final seating arrangement with table numbers, guest names, group names, occupied seats and available seats.

7. Input Validation: Handle invalid menu choices, invalid table capacities, incorrect RSVP statuses and invalid guest information.

## Sample run

=============================================
                  GUESTGRID
       EVENT GUEST & TABLE SEATING MANAGER
=============================================
1. Add New Guest
2. View All Guests
3. Search Guest
4. Update Guest Details
5. Update RSVP Status
6. View Confirmed Headcount
7. Allocate Guests to Tables
8. View Meal Preference Summary
9. Print Seating Chart
10. Exit
=============================================

Enter your choice (1-10): 1

========== ADD NEW GUEST ==========

Enter guest name: Rahul
Enter group type (Family/Friends): Family
Enter group name (e.g. Sharma Family): Sharma Family
Enter meal preference (Vegetarian/Non-Vegetarian/Vegan/Jain): Vegetarian

Guest added successfully!
Guest ID: G001

Enter your choice (1-10): 5

========== UPDATE RSVP ==========

Enter Guest ID: G001

Current RSVP: Pending
1. Confirmed
2. Declined
3. Pending

Select new RSVP status: 1
RSVP updated successfully!

Enter your choice (1-10): 6

========== RSVP SUMMARY ==========

Total Registered Guests: 1
Confirmed Guests: 1
Declined Guests: 0
Pending Guests: 0

Enter your choice (1-10): 8

========== CATERING REPORT ==========

Meal Preference       Headcount
--------------------------------
Vegetarian             1
Non-Vegetarian         0
Vegan                  0
Jain                   0
--------------------------------
Total Confirmed Guests: 1

Enter your choice (1-10): 10

Thank you for using GuestGrid!
Exiting application...
