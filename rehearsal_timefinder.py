####### DEFINING FUNCTIONS #######

import numpy as np
from staff_schedules import *
from cast_schedules import *
day_names = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

class Rehearsal:
    def __init__(self, name, rehearsal_type, duration, required_people):
        self.name = name
        self.type = rehearsal_type
        self.duration = duration # in hours
        self.required_people = required_people

    # raise an error that says that an actor has been called for too many hours if necessary

# Convert decimal hours to 12-hour format with AM/PM
def format_time(decimal_time):
    # Ensure the time wraps correctly by taking modulo 24
    hours = int(decimal_time)
    minutes = int((decimal_time - hours) * 60)
    period = "AM" if hours < 12 else "PM"
    hours = hours % 12
    if hours == 0:
        hours = 12
    return f"{hours}:{minutes:02d} {period}"


def check_availability(rehearsal_blocks, day_conflicts, rehearsal_duration):
    available_blocks = []
    for block in rehearsal_blocks:
        if all(block + i * 0.25 not in [bc for start, end in day_conflicts for bc in np.arange(start, end, 0.25)]
            for i in range(int(rehearsal_duration / 0.25))):
            available_blocks.append(block)
    return available_blocks

def is_available(time, unavailable_periods):
    for start, end, _ in unavailable_periods:
        if start <= time < end:
            return False
    return True

def display_missing_actors(rehearsal, required_people, day, available_blocks, day_conflicts):
    print(f"Rehearsal: {rehearsal.name} on {day_names[day-1]}")
    for block in available_blocks:
        start_time = format_time(block)
        end_time = format_time(block + rehearsal.duration)
        missing_actors = []

        for person_name in required_people:
            person = next((actor for actor in actors if actor.name == person_name), None)
            if person and not all(is_available(block + i * 0.25, person.schedule.schedule[day]) for i in range(int(rehearsal.duration / 0.25))):
                missing_actors.append(person.name)

        if missing_actors:
            print(f"From {start_time} to {end_time}, the following actors would be missing: {', '.join(missing_actors)}")
        else:
            print(f"From {start_time} to {end_time}, all actors are available for {rehearsal.name} rehearsal.")

#############################

####### MAIN FUNCTION #######

# def assign_rehearsal_times(rehearsals, actors, staff_members, current_threshold = 100):

#     # Define end time in decimal for 11:30 PM
#     end_time_decimal = 23.5

#     required_roles = {"blocking": "director", "music": "music_director", "choreo": "choreographer"}

#     for rehearsal in rehearsals:
#         print(f"Checking availability for {rehearsal.name}:")
#         required_people = rehearsal.required_people + [staff.name for staff in staff_members
#                                                        if required_roles[rehearsal.type] == staff.role]
        
#         print(f"{required_people} must all be present") # just so I can check that it's working

#         # # Gather all conflicts from required participants
#         all_conflicts = {day: [] for day in range(1, 8)}

#         for person in actors + staff_members:
#             if person.name in required_people:
#                 for day in range(1, 8):
#                     all_conflicts[day].extend(person.schedule.schedule[day])
        
#         week_availability_found = False

#         for day in range(1, 8):
#             print(f"\nDay: {day_names[day-1]}")
#             day_conflicts = sorted((start, end) for start, end, _ in all_conflicts[day])
#             if day <= 5:
#                 # Adjusted to subtract rehearsal duration from the last block
#                 rehearsal_blocks = [i * 0.25 for i in range(72, int((end_time_decimal - rehearsal.duration) / 0.25))]
#             else:
#                 rehearsal_blocks = [i * 0.25 for i in range(40, int((end_time_decimal - rehearsal.duration) / 0.25))]

#             if current_threshold < 100:
#                 threshold = max(int(len(rehearsal.required_people) * current_threshold / 100), int(len(required_people) * 0.5))
#                 available_blocks = [
#                     block for block in rehearsal_blocks if sum(is_available(block + i * 0.25, all_conflicts[day]) for i in range(int(rehearsal.duration / 0.25))
#                     ) >= threshold]
                
#             else:
#                 available_blocks = check_availability(rehearsal_blocks, day_conflicts, rehearsal.duration)

#             if available_blocks:
#                 week_availability_found = True
#                 display_missing_actors(rehearsal, required_people, day, available_blocks, day_conflicts)
#             else:
#                 print(f"No available blocks for {rehearsal.name} on this day.")
        
#         if not week_availability_found:

#             if current_threshold == 50:
#                 print("Yikes, tough.")
#                 break

#             alternatives = input(f"No {current_threshold}% availability found all week. Would you like to find times with reduced actor availability (yes/no)? ").strip().lower()
#             if alternatives == 'yes':
#                 next_threshold = current_threshold - 10
#                 print(f"Searching for {next_threshold}% availability...")
#                 assign_rehearsal_times(rehearsals, actors, staff_members, current_threshold=next_threshold)
#             elif alternatives == 'no':
#                 print("Proceeding without adjusting for lower availability.")
#             else:
#                 print("Invalid input, not checking for lower availability.")

###########################################

####### DEFINING EXAMPLE REHEARSALS #######

# Define participants, their schedules, and rehearsals, then call assign_rehearsal_times

# Week 1 Rehearsals
blue_wind_music = Rehearsal("[Vocal] Blue Wind", "music", 1, ["Hannah"])
touch_me_music_georg = Rehearsal("[Vocal] Touch Me - Georg", "music", .5, ["Sean"])
act_1_scene_1 = Rehearsal("[Blocking] Act 1, Scene 1", "blocking", 1, ["Texaco", "Shannon"])
act_1_scene_2_adults = Rehearsal("[Blocking] Act 1, Scene 2 - Adults", "blocking", .5, ["Daniela", "Rob"])
all_thats_known_blocking = Rehearsal("[Blocking] All That's Known", "blocking", 1, ["Jonah"])
jonah_vocal_review = Rehearsal("[Vocal] Jonah Review", "music", .5, ["Jonah"])
touch_me_music_mm = Rehearsal("[Vocal] Touch Me - Melchior, Moritz", "music", .5, ["Jonah", "Nikhil"])
touch_me_music_ernst = Rehearsal("[Vocal] Touch Me - Ernst", "music", .5, ["Jared"])
all_thats_known_music_boys = Rehearsal("[Vocal] All That's Known - Boys", "music", .25, ["Nikhil", "Jared", "Sean", "Andrew", "Ben"])
all_thats_known_music_all = Rehearsal("[Vocal] All That's Known - All Boys", "music", .25, ["Jonah", "Nikhil", "Jared", "Sean", "Andrew", "Ben"])
bitch_of_living_music = Rehearsal("[Vocal] Bitch of Living Music", "music", 1, ["Jonah", "Nikhil", "Jared", "Sean", "Andrew", "Ben"])
touch_me_music_otto = Rehearsal("[Vocal] Touch Me - Otto", "music", .25, ["Ben"])
all_thats_known_choreo = Rehearsal("[Choreo] All That's Known", "choreo", 1, ["Jonah", "Nikhil", "Jared", "Sean", "Andrew", "Ben"])
mama_who_bore_me_reprise_music = Rehearsal("[Vocal] Mama Who Bore Me Reprise", "music", 1, ["Shannon", "Kiesse", "Ria", "Riley", "Andreea", "Hannah"])
my_junk_music_girls = Rehearsal("[Vocal] My Junk - Girls", "music", .5, ["Shannon", "Kiesse", "Ria", "Riley", "Andreea", "Hannah"])
mama_who_bore_me_blocking = Rehearsal("[Blocking] Mama Who Bore Me", "blocking", .5, ["Shannon", "Kiesse", "Ria", "Riley", "Andreea", "Hannah"])
mama_who_bore_me_reprise_choreo = Rehearsal("[Choreo] Mama Who Bore Me Reprise", "choreo", 1.5, ["Shannon", "Kiesse", "Ria", "Riley", "Andreea", "Hannah"])
act_1_scene_2_boys = Rehearsal("[Blocking] Act 1, Scene 2 - Boys", "blocking", 1, ["Jonah", "Nikhil"])
my_junk_music_all = Rehearsal("[Vocal] My Junk - All", "music", 1, ALL)
touch_me_music_all = Rehearsal("[Vocal] Touch Me - All", "music", 1, ALL)
the_word_of_your_body_blocking = Rehearsal("[Blocking] The Word of Your Body", "blocking", .75, ["Shannon", "Jonah"])

test_rehearsal = Rehearsal("[Vocal] Something Crazy", "music", 5, ALL)

rehearsals_week_1 = [blue_wind_music, touch_me_music_georg, touch_me_music_all, act_1_scene_1, act_1_scene_2_adults,
                     all_thats_known_blocking, jonah_vocal_review, touch_me_music_mm, touch_me_music_ernst, all_thats_known_music_boys,
                     all_thats_known_music_all, bitch_of_living_music, touch_me_music_otto, all_thats_known_choreo, mama_who_bore_me_reprise_music,
                     my_junk_music_girls, mama_who_bore_me_blocking, mama_who_bore_me_reprise_choreo, act_1_scene_2_boys, 
                     my_junk_music_all, the_word_of_your_body_blocking]

#rehearsals_week_1 = [blue_wind_music]

##############################

####### TESTING IT OUT #######

#rehearsals_week_1 = [test_rehearsal]

actors = [Jonah, Shannon, Nikhil, Hannah, Andreea, Andrew, Jared, Sean, Ben, Kiesse, Riley,
          Ria, Daniela, Texaco, Anna, Lindsay, Rob, Alvin, Saswato, Mattheus]

#staff_members = [Fahim, Joe, Henry, Grace, Caron, Adrienne]
staff_members = [Fahim, Grace, Caron, Adrienne]

# assign_rehearsal_times(rehearsals_week_1, actors, staff_members)

##############################