from datetime import datetime

# Function to convert time from 12-hour format to decimal hour military time
# Since decimals are easier to consider on a continuous scale
def convert_to_military(time_str):

    # Parse the time string into a datetime object using the specified format (12-hour clock with AM/PM)
    time_obj = datetime.strptime(time_str, "%I:%M %p")

    # Convert to military time in decimal hours, where minutes are a fraction of an hour
    return time_obj.hour + time_obj.minute / 60

class Schedule:
    def __init__(self, actor_name):

        # Initializes a Schedule with an actor's name and an empty schedule for each day of the week
        self.actor_name = actor_name

        # Dictionary comprehension to initialize each day
        self.schedule = {day: [] for day in range(1, 8)}  # 7 days in a week

    def add_conflicts(self, conflicts_per_day):

        # Ensure conflicts data is provided for all 7 days, raise an error if not
        if len(conflicts_per_day) != 7:
            raise ValueError("Conflicts per day should be provided for all 7 days")
        
        # Loop through each day's conflicts and add them to the schedule
        for day, conflicts in enumerate(conflicts_per_day, start=1):

            # Convert start and end times to military format and add the conflict type
            self.schedule[day].extend([(convert_to_military(start), convert_to_military(end), conflict_type) for start, end, conflict_type in conflicts])

# input each rehearsal staff member's schedules manually
    # music director's schedule is relevant to music rehearsals
    # choreographer's schedule is relevant to choreo rehearsals
    # director's schedule is relevant to blocking rehearsals

# Example class for staff members, including scheduling based on their role
class Staff:
    def __init__(self, name, role, max_hours_per_week):

        # Constructor for Staff class, initializing with name, role, and maximum weekly hours
        self.name = name
        self.role = role
        self.schedule = Schedule(name) # Each staff member has their own schedule
        self.max_hours_per_week = max_hours_per_week 
    
    def __str__(self):

        # Generate a string representation of a staff member, including their schedule
        staff_info = f"Staff Member: {self.name}\n" # Start with staff name
        staff_info += "Schedule:\n"

        # Iterate over each day in the staff member's schedule to display conflicts
        for day, conflicts in self.schedule.schedule.items():
            staff_info += f"Day {day}:\n"
            for conflict in conflicts:
                start_time, end_time, conflict_type = conflict

                # Display conflict details including times and types
                staff_info += f"    - {start_time} to {end_time}: {conflict_type}\n"
                
        return staff_info

Fahim = Staff("Fahim", "music_director", 20)
Fahim_conflicts = [
    [("10:30 AM", "12:00 PM", "academic"), ("12:30 PM", "2:00 PM", "academic"), ("3:00 PM", "4:00 PM", "other")],  # Monday
    [("9:00 AM", "12:00 PM", "academic"), ("12:00 PM", "1:00 PM", "other"), ("1:30 PM", "3:00 PM", "academic"),
     ("5:00 PM", "6:30 PM", "other"), ("7:30 PM", "9:30 PM", "other")],  # Tuesday
    [("9:00 AM", "12:00 PM", "academic"), ("12:30 PM", "2:00 PM", "academic"), ("3:00 PM", "6:00 PM", "academic")],  # Wednesday
    [("9:00 AM", "12:00 PM", "academic"), ("1:30 PM", "3:00 PM", "academic"), ("5:00 PM", "6:30 PM", "other")],  # Thursday
    [("10:30 AM", "12:00 PM", "academic"), ("12:30 PM", "2:00 PM", "academic")],  # Friday
    [("11:30 AM", "12:30 PM", "other"), ("1:00 PM", "2:00 PM", "other")],  # Saturday
    [("9:30 AM", "12:30 PM", "other"), ("4:00 PM", "6:00 PM", "other"), ("7:30 PM", "10:30 PM", "other")],  # Sunday
]

Fahim.schedule.add_conflicts(Fahim_conflicts)

Joe = Staff("Joe", "music_director", 20)
Joe_conflicts = [
    [("1:30 PM", "5:30 PM", "academic")],  # Monday
    [("9:00 AM", "10:30 AM", "academic"), ("12:30 PM", "3:00 PM", "academic")],  # Tuesday
    [("1:30 PM", "5:30 PM", "academic"), ("8:00 PM", "10:00 PM", "other")],  # Wednesday
    [("9:00 AM", "12:00 PM", "academic"), ("8:00 PM", "10:00 PM", "other")],  # Thursday
    [("1:30 PM", "3:00 PM", "academic")],  # Friday
    [("11:30 AM", "12:30 PM", "other")],  # Saturday
    [("12:00 PM", "2:00 PM", "other")],  # Sunday
]

Joe.schedule.add_conflicts(Joe_conflicts)

Henry = Staff("Henry", "music_director", 20)
Henry_conflicts = [
    [("10:30 AM", "12:00 PM", "academic"), ("1:30 PM", "4:30 PM", "academic")],  # Monday
    [("11:00 AM", "1:00 PM", "academic"), ("4:00 PM", "6:00 PM", "academic")],  # Tuesday
    [("10:30 AM", "12:00 PM", "academic"), ("1:30 PM", "4:30 PM", "academic")],  # Wednesday
    [("10:30 AM", "11:30 AM", "academic"), ("3:00 PM", "5:00 PM", "academic"), ("7:00 PM", "9:00 PM", "other")],  # Thursday
    [("10:30 AM", "11:30 AM", "academic"), ("1:30 PM", "3:00 PM", "other")],  # Friday
    [("11:30 AM", "12:30 PM", "other")],  # Saturday
    [("7:30 PM", "10:30 PM", "other")],  # Sunday
]

Henry.schedule.add_conflicts(Henry_conflicts)

Grace = Staff("Grace", "director", 20)
Grace_conflicts = [
    [("9:00 AM", "10:30 AM", "academic"), ("12:00 PM", "1:00 PM", "academic")],  # Monday
    [("10:30 AM", "12:00 PM", "academic"), ("1:30 PM", "3:00 PM", "academic")],  # Tuesday
    [("9:00 AM", "10:30 AM", "academic")],  # Wednesday
    [("10:30 AM", "12:00 PM", "academic"), ("1:30 PM", "4:30 PM", "academic")],  # Thursday
    [("10:30 AM", "12:00 PM", "academic"), ("12:30 PM", "2:00 PM", "academic")],  # Friday
    [("11:30 AM", "12:30 PM", "other")],  # Saturday
    [],  # Sunday
]

Grace.schedule.add_conflicts(Grace_conflicts)

Caron = Staff("Caron", "choreographer", 20)
Caron_conflicts = [
    [("4:30 PM", "5:45 PM", "academic"), ("9:45 PM", "11:45 PM", "other")],  # Monday
    [("10:00 AM", "12:00 PM", "other"), ("1:30 PM", "2:45 PM", "academic"), ("3:00 PM", "4:45 PM", "other"), ("7:30 PM", "9:00 PM", "other")],  # Tuesday
    [("3:00 PM", "4:00 PM", "academic"), ("4:30 PM", "5:45 PM", "academic"), ("7:00 PM", "9:00 PM", "other")],  # Wednesday
    [("1:30 PM", "2:45 PM", "academic"), ("3:00 PM", "4:30 PM", "academic")],  # Thursday
    [("1:00 PM", "4:00 PM", "academic")],  # Friday
    [("11:30 AM", "12:30 PM", "other"), ("1:00 PM", "2:00 PM", "other")],  # Saturday
    [("9:00 AM", "10:00 AM", "other"), ("11:30 AM", "1:00 PM", "other"), ("12:00 PM", "5:00 PM", "other"), ("7:00 PM", "9:00 PM", "other")],  # Sunday
]

Caron.schedule.add_conflicts(Caron_conflicts)

Adrienne = Staff("Adrienne", "choreographer", 20)
Adrienne_conflicts = [
    [("12:00 PM", "1:15 PM", "academic"), ("9:45 PM", "11:45 PM", "other")],  # Monday
    [("12:00 PM", "2:45 PM", "academic")],  # Tuesday
    [("12:00 PM", "1:15 PM", "academic"), ("3:00 PM", "5:15 PM", "academic")],  # Wednesday
    [("9:45 AM", "11:45 AM", "academic"), ("12:00 PM", "1:00 PM", "academic")],  # Thursday
    [("1:00 PM", "4:00 PM", "other")],  # Friday
    [("5:00 PM", "6:00 PM", "other")],  # Saturday
    [],  # Sunday
]

Adrienne.schedule.add_conflicts(Adrienne_conflicts)

staff_members = [Fahim, Joe, Henry, Grace, Caron, Adrienne]