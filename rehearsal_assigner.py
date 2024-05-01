# Imports relevant classes and functions
from rehearsal_timefinder import *

import numpy as np

def sort_rehearsals_by_participants(rehearsals):
    # Sorts the rehearsals list by the number of required participants in descending order
    return sorted(rehearsals, key=lambda r: len(r.required_people), reverse=True)

def is_available(time, unavailable_periods):
    # Checks if a specific time is available by looping through periods where it may be unavailable
    for period in unavailable_periods:
        if len(period) >= 2: # Ensures the period has at least two elements (start and end times)
            start, end = period[:2]  # Extracts start and end times
            if start <= time < end: # Checks if the given time falls within this period
                return False # Time is not available
    return True # All checks passed; time is available

staff_needed = {
    "music": "music_director", # Maps 'music' rehearsals to needing a 'music_director'
    "blocking": "director", # Maps 'blocking' rehearsals to needing a 'director'
    "choreo": "choreographer" # Maps 'choreo' rehearsals to needing a 'choreographer'
}

def update_availability(schedules, rehearsal, slot, day):
    # Blocks off the time for everyone involved in the rehearsal on a given day
    # Gets the required staff role for the rehearsal type
    staff_role = staff_needed.get(rehearsal.type)

    # Filters staff members who fit the required role
    required_staff = [staff for staff in staff_members if staff.role == staff_role]
    
    # Calculates the end time of the rehearsal
    end_time = slot + rehearsal.duration
    for person in schedules:
        if person.name in rehearsal.required_people or (hasattr(person, 'role') and person.role in [staff.role for staff in required_staff]):
            person.schedule.schedule[day].append((slot, end_time)) # Blocks the time in the person's schedule

def find_first_available_slot(rehearsal, available_times, actors, staff_members, day):
    # Tries to find the first available slot for a rehearsal that fits all participants' schedules 
    staff_role = staff_needed.get(rehearsal.type)  # Retrieves the specific staff role required for this rehearsal

    required_staff = [staff for staff in staff_members if staff.role == staff_role]  # Gets the required staff members for the rehearsal
    required_people = actors + required_staff # Combines actors and required staff members into one list

    # Iterates through each possible start time to find an available slot
    for start_time in available_times:

        # Calculates potential end time
        end_time = start_time + rehearsal.duration
        if end_time > 23.5:  # Checks if the rehearsal would end later than 11:30 PM
            break # Stop checking if it would

        # Checks if the entire duration of the rehearsal is available for all required participants
        if all(
            all(is_available(time, person.schedule.schedule[day]) for time in np.arange(start_time, end_time, 0.25))
            for person in required_people
        ):
            # Returns the starting time if suitable
            return start_time
        
     # Returns None if no suitable time slot is found
    return None 

# Function to assign rehearsals to available times
def assign_rehearsals(rehearsals, actors, staff_members):

    # Initializes the final schedule dictionary
    schedule = {}

    # Creates a copy of the rehearsals list to keep track of unassigned ones
    unassigned_rehearsals = rehearsals[:] 

    # Ensures all participants have a schedule attribute
    for actor in actors + staff_members:
        if not hasattr(actor, 'schedule'):
            actor.schedule = {'schedule': {day: [] for day in range(1, 8)}}

    # Tries to schedule each rehearsal on each day
    for day in range(1, 8):
        if not unassigned_rehearsals:
            break # Breaks the loop if all rehearsals are assigned
        
        # Defines work hours based on day of the week
        if day <= 5:
            work_hours = (18, 23.25)
        else:
            work_hours = (10, 23.25)

        # Creates a list of quarter-hour intervals within work hours
        available_times = np.arange(work_hours[0], work_hours[1], 0.25)
        
        # List to store the day's schedule
        day_schedule = []

        # Sorts and tries to assign each unassigned rehearsal
        for rehearsal in sort_rehearsals_by_participants(unassigned_rehearsals):
            slot = find_first_available_slot(rehearsal, available_times, actors, staff_members, day)
            
            # If a slot is found
            if slot is not None:
                
                # Add it to the day's schedule
                day_schedule.append((rehearsal.name, slot, slot + rehearsal.duration))
                
                # Update the availability for all required participants
                update_availability(actors + staff_members, rehearsal, slot, day)
                
                # Remove the rehearsal from the unassigned list
                unassigned_rehearsals.remove(rehearsal)

        # Assigns the day's schedule to the final schedule
        schedule[day] = day_schedule

    for day, rehearsals in schedule.items():
        print(f"Day {day}:")
        for rehearsal in rehearsals:
            print(f"  - {rehearsal[0]} from {format_time(rehearsal[1])} to {format_time(rehearsal[2])}")
    #return schedule # Returns the complete schedule

# Running the scheduling
final_schedule = assign_rehearsals(rehearsals_week_1, actors, staff_members)
# for day, rehearsals in final_schedule.items():
#     print(f"Day {day}:")
#     for rehearsal in rehearsals:
#         print(f"  - {rehearsal[0]} from {format_time(rehearsal[1])} to {format_time(rehearsal[2])}")