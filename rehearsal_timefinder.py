####### DEFINING FUNCTIONS #######

import numpy as np
from staff_schedules import * # Imports schedules of staff
from cast_schedules import * # Imports schedules of cast
day_names = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

class Rehearsal:
    def __init__(self, name, rehearsal_type, duration, required_people):

        # Initializes a Rehearsal object with its name, type, duration, and the people required for it
        self.name = name
        self.type = rehearsal_type
        self.duration = duration # in hours
        self.required_people = required_people

# Convert decimal hours to 12-hour format with AM/PM
def format_time(decimal_time):
    # Converts time in decimal hours to a 12-hour clock format with AM/PM notation
    hours = int(decimal_time) # Extracts the hour part
    minutes = int((decimal_time - hours) * 60) # Converts the decimal part to minutes
    period = "AM" if hours < 12 else "PM" # Determines AM or PM period
    
    # Adjusts hour format for 12-hour clock
    hours = hours % 12
    if hours == 0:
        hours = 12
    
    # Formats time string
    return f"{hours}:{minutes:02d} {period}"

# Check the availability of time blocks for a rehearsal without schedule conflicts
def check_availability(rehearsal_blocks, day_conflicts, rehearsal_duration):
    
     # Initializes a list to store available time blocks
    available_blocks = []

    # Iterates through each proposed time block
    for block in rehearsal_blocks:
        if all(block + i * 0.25 not in [bc for start, end in day_conflicts for bc in np.arange(start, end, 0.25)]
            for i in range(int(rehearsal_duration / 0.25))):
            
            # Adds block to available_blocks if it's free of conflicts
            available_blocks.append(block)

    # Returns the list of available time blocks
    return available_blocks

# Function to determine if a specific time block is free from conflicts
def is_available(time, unavailable_periods):
    for start, end, _ in unavailable_periods: # Checks each conflict period
        if start <= time < end: # If the time falls within a conflict period
            return False # Returns False, indicating time is not available
    return True # Returns True if no conflicts are found

# Display which actors are missing from available blocks
def display_missing_actors(rehearsal, required_people, day, available_blocks, day_conflicts):
    
    # Prints the rehearsal name and day
    print(f"Rehearsal: {rehearsal.name} on {day_names[day-1]}")
    for block in available_blocks: # For each available time block
        start_time = format_time(block) # Converts start time to human-readable format
        end_time = format_time(block + rehearsal.duration) # Converts end time to human-readable format
        missing_actors = []  # List to hold names of missing actors

        # Check for each required person if they are available during the time block
        for person_name in required_people:
            person = next((actor for actor in actors if actor.name == person_name), None)
            if person and not all(is_available(block + i * 0.25, person.schedule.schedule[day]) for i in range(int(rehearsal.duration / 0.25))):
                missing_actors.append(person.name) # Adds missing actor's name to the list

        if missing_actors:
            print(f"From {start_time} to {end_time}, the following actors would be missing: {', '.join(missing_actors)}")
        else:
            print(f"From {start_time} to {end_time}, all actors are available for {rehearsal.name} rehearsal.")

#############################

####### MAIN FUNCTION #######

def assign_rehearsal_times(rehearsals, actors, staff_members, current_threshold = 100):

    # Set the end time for rehearsals each day in decimal hours (11:30 PM)
    end_time_decimal = 23.5

    # Mapping rehearsal types to the specific staff role required for each type
    required_roles = {"blocking": "director", "music": "music_director", "choreo": "choreographer"}

    # Iterate over each rehearsal to check and assign times based on availability
    for rehearsal in rehearsals:
        print(f"Checking availability for {rehearsal.name}:")

        # Aggregate the names of all required people for the rehearsal, including specific staff roles
        required_people = rehearsal.required_people + [staff.name for staff in staff_members
                                                       if required_roles[rehearsal.type] == staff.role]
        
        print(f"{required_people} must all be present") # just so I can check that it's working

        # Create a dictionary to store conflicts for each day of the week
        all_conflicts = {day: [] for day in range(1, 8)}

        # Collect all scheduling conflicts from required people across all days of the week
        for person in actors + staff_members:
            if person.name in required_people:
                for day in range(1, 8):
                    all_conflicts[day].extend(person.schedule.schedule[day])
        
        # Flag to indicate if any availability was found in the week
        week_availability_found = False

        # Check each day of the week for available rehearsal times
        for day in range(1, 8):
            print(f"\nDay: {day_names[day-1]}")

            # Sort daily conflicts to prepare for checking available time blocks
            day_conflicts = sorted((start, end) for start, end, _ in all_conflicts[day])
            
            # Define time blocks for rehearsals, adjusting for weekends
            if day <= 5:
                # Weekday timing blocks (post typical work hours)
                rehearsal_blocks = [i * 0.25 for i in range(72, int((end_time_decimal - rehearsal.duration) / 0.25))]
            else:
                # Weekend timing blocks (longer available periods)
                rehearsal_blocks = [i * 0.25 for i in range(40, int((end_time_decimal - rehearsal.duration) / 0.25))]

             # Adjust threshold for determining availability based on current settings or defaults
            if current_threshold < 100:
                threshold = max(int(len(rehearsal.required_people) * current_threshold / 100), int(len(required_people) * 0.5))
                available_blocks = [
                    block for block in rehearsal_blocks if sum(is_available(block + i * 0.25, all_conflicts[day]) for i in range(int(rehearsal.duration / 0.25))
                    ) >= threshold]
                
            else:
                # Check availability using default method
                available_blocks = check_availability(rehearsal_blocks, day_conflicts, rehearsal.duration)

             # If available blocks are found, mark week availability as true and display missing actors
            if available_blocks:
                week_availability_found = True
                display_missing_actors(rehearsal, required_people, day, available_blocks, day_conflicts)
            else:
                print(f"No available blocks for {rehearsal.name} on this day.")
        
        # If no availability found all week and threshold adjustments are possible, prompt for user input
        if not week_availability_found:
            if current_threshold == 50:
                print(f"No times with at least 50% actor availability found this week.")
                break

            # Ask user if they want to try finding availability with a reduced threshold
            alternatives = input(f"No {current_threshold}% availability found all week. Would you like to find times with reduced actor availability (yes/no)? ").strip().lower()
            if alternatives == 'yes':
                next_threshold = current_threshold - 10
                print(f"Searching for {next_threshold}% availability...")
                assign_rehearsal_times(rehearsals, actors, staff_members, current_threshold=next_threshold)
            elif alternatives == 'no':
                print("Proceeding without adjusting for lower availability.")
            else:
                print("Invalid input, not checking for lower availability.")

###########################################

####### DEFINING EXAMPLE REHEARSALS #######

##### Week 1 Rehearsals #####
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

# rehearsals_week_1 = [blue_wind_music, touch_me_music_georg, touch_me_music_all, act_1_scene_1, act_1_scene_2_adults,
#                      all_thats_known_blocking, jonah_vocal_review, touch_me_music_mm, touch_me_music_ernst, all_thats_known_music_boys,
#                      all_thats_known_music_all, bitch_of_living_music, touch_me_music_otto, all_thats_known_choreo, mama_who_bore_me_reprise_music,
#                      my_junk_music_girls, mama_who_bore_me_blocking, mama_who_bore_me_reprise_choreo, act_1_scene_2_boys, 
#                      my_junk_music_all, the_word_of_your_body_blocking]

rehearsals_week_1 = [blue_wind_music]

#rehearsals_week_2 = [my_junk_music_girls, all_thats_known_choreo, mama_who_bore_me_reprise_choreo]

##############################

####### TESTING IT OUT #######

#rehearsals_week_1 = [test_rehearsal]

# Fahim_onetime = [[],[],[],[],[],[],[("2:00 PM", "4:00 PM", "other")]]
# Sunday one-time conflict for BachSoc Orchestra

# Fahim.schedule.add_conflicts(Fahim_onetime)

assign_rehearsal_times(rehearsals_week_1, actors, staff_members)

# assign_rehearsal_times(rehearsals_week_2, actors_2, staff_members_2)
##############################

