# GuestGrid
Event Guest and Table Seating Manager

# CP-068 GuestGrid: Event Guest and Table Seating Manager
## Team
Sethuram P (1AT24CS197)

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

<img width="749" height="650" alt="image" src="https://github.com/user-attachments/assets/f1551e76-6d54-4941-9056-a8b094466725" />
<img width="743" height="498" alt="image" src="https://github.com/user-attachments/assets/17ec542a-fd16-436c-9844-cc897c356632" />
<img width="726" height="642" alt="image" src="https://github.com/user-attachments/assets/5e878398-958d-46b5-b49e-baec2c0d9669" />

Note: The above is an illustrative sample execution showing the menu, guest registration, RSVP update and catering report. The actual output depends on the data entered by the user.
