from rehearsal_timefinder import *

import numpy as np

def sort_rehearsals_by_participants(rehearsals):
    # Sort by the number of required participants, descending
    return sorted(rehearsals, key=lambda r: len(r.required_people), reverse=True)

def is_available(time, unavailable_periods):
    for period in unavailable_periods:
        if len(period) >= 2:
            start, end = period[:2]  # Safely unpack only the first two elements
            if start <= time < end:
                return False
    return True

staff_needed = {
    "music": "music_director",
    "blocking": "director",
    "choreo": "choreographer"
}

def update_availability(schedules, rehearsal, slot, day):
    # Block off the time for everyone involved in the rehearsal
    staff_role = staff_needed.get(rehearsal.type)
    required_staff = [staff for staff in staff_members if staff.role == staff_role]
    end_time = slot + rehearsal.duration
    for person in schedules:
        if person.name in rehearsal.required_people or (hasattr(person, 'role') and person.role in [staff.role for staff in required_staff]):
            person.schedule.schedule[day].append((slot, end_time))

def find_first_available_slot(rehearsal, available_times, actors, staff_members, day):
    staff_needed = {
        "music": "music_director",
        "blocking": "director",
        "choreo": "choreographer"
    }
    staff_role = staff_needed.get(rehearsal.type)

    required_staff = [staff for staff in staff_members if staff.role == staff_role]
    required_people = actors + required_staff

    for start_time in available_times:
        end_time = start_time + rehearsal.duration
        if end_time > 23.5:  # Ensure rehearsal ends by 11:30 PM
            break
        if all(
            all(is_available(time, person.schedule.schedule[day]) for time in np.arange(start_time, end_time, 0.25))
            for person in required_people
        ):
            return start_time
    return None

def assign_rehearsals(rehearsals, actors, staff_members):
    schedule = {}
    unassigned_rehearsals = rehearsals[:] 

    for actor in actors + staff_members:
        if not hasattr(actor, 'schedule'):
            actor.schedule = {'schedule': {day: [] for day in range(1, 8)}}

    for day in range(1, 8):
        if not unassigned_rehearsals:
            break
        if day <= 5:
            work_hours = (18, 23.25)
        else:
            work_hours = (10, 23.25)
        available_times = np.arange(work_hours[0], work_hours[1], 0.25)
        day_schedule = []

        for rehearsal in sort_rehearsals_by_participants(unassigned_rehearsals):
            slot = find_first_available_slot(rehearsal, available_times, actors, staff_members, day)
            if slot is not None:
                day_schedule.append((rehearsal.name, slot, slot + rehearsal.duration))
                update_availability(actors + staff_members, rehearsal, slot, day)
                unassigned_rehearsals.remove(rehearsal)

        schedule[day] = day_schedule

    return schedule



# Example usage with mock data:
# - Assume `actors` and `staff_members` have attributes `.name` and `.schedule` which is a dict of days to lists of tuples (start, end)
# - `Rehearsal` class instances have `.name`, `.duration`, and `.required_people`

# Running the scheduling
final_schedule = assign_rehearsals(rehearsals_week_1, actors, staff_members)
for day, rehearsals in final_schedule.items():
    print(f"Day {day}:")
    for rehearsal in rehearsals:
        print(f"  - {rehearsal[0]} from {format_time(rehearsal[1])} to {format_time(rehearsal[2])}")