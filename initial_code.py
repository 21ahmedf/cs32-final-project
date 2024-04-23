from datetime import datetime

# Function to convert time from 12-hour format to decimal hour military time
def convert_to_military(time_str):
    # Parse the time string into a datetime object
    time_obj = datetime.strptime(time_str, "%I:%M %p")
    # Convert to military time in decimal hours
    return time_obj.hour + time_obj.minute / 60

# input each actor's schedules manually, this part of the code will vary each week, but recurring conflicts will stay
    # schedules for each person can be split by day
    # conflict type should either be "academic" or "other"

class Schedule:
    def __init__(self, actor_name):
        self.actor_name = actor_name
        self.schedule = {day: [] for day in range(1, 8)}  # 7 days in a week

    def add_conflicts(self, conflicts_per_day):
        if len(conflicts_per_day) != 7:
            raise ValueError("Conflicts per day should be provided for all 7 days")
        for day, conflicts in enumerate(conflicts_per_day, start=1):
            # Convert and add conflicts
            self.schedule[day].extend([(convert_to_military(start), convert_to_military(end), conflict_type) for start, end, conflict_type in conflicts])

# input each rehearsal staff member's schedules manually as well
    # music director's schedule is relevant to music rehearsals
    # choreographer's schedule is relevant to choreo rehearsals
    # director's schedule is relevant to all types of rehearsals, but essential for staging rehearsals

class Staff:
    def __init__(self, name, role, max_hours_per_week):
        self.name = name
        self.role = role
        self.schedule = Schedule(name)
        self.max_hours_per_week = max_hours_per_week
    
    def __str__(self):
        staff_info = f"Staff Member: {self.name}\n"
        staff_info += "Schedule:\n"
        for day, conflicts in self.schedule.schedule.items():
            staff_info += f"Day {day}:\n"
            for conflict in conflicts:
                start_time, end_time, conflict_type = conflict
                staff_info += f"    - {start_time} to {end_time}: {conflict_type}\n"
        return staff_info

Fahim = Staff("Fahim", "music_director", 20)
Fahim_conflicts = [
    [("10:30 AM", "12:00 PM", "academic"), ("12:30 PM", "2:00 PM", "academic"), ("3:00 PM", "4:00 PM", "other")],  # Monday
    [("9:00 AM", "12:00 PM", "academic"), ("12:00 PM", "1:00 PM", "other"), ("1:30 PM", "3:00 PM", "academic"), ("5:00 PM", "6:30 PM", "other"), ("7:30 PM", "9:30 PM", "other")],  # Tuesday
    [("9:00 AM", "12:00 PM", "academic"), ("12:30 PM", "2:00 PM", "academic"), ("3:00 PM", "6:00 PM", "academic")],  # Wednesday
    [("9:00 AM", "12:00 PM", "academic"), ("1:30 PM", "3:00 PM", "academic"), ("5:00 PM", "6:30 PM", "other")],  # Thursday
    [("10:30 PM", "12:00 PM", "academic"), ("12:30 PM", "2:00 PM", "academic")],  # Friday
    [("11:30 AM", "12:30 PM", "other"), ("1:00 PM", "2:00 PM", "other")],  # Saturday
    [("9:30 AM", "12:30 PM", "other"), ("4:00 PM", "6:00 PM", "other")],  # Sunday
]

Fahim.schedule.add_conflicts(Fahim_conflicts)

Grace = Staff("Grace", "director", 20)
Grace_conflicts = [
    [("9:00 AM", "10:30 AM", "academic"), ("12:00 PM", "1:00 PM", "academic")],  # Monday
    [("10:30 AM", "12:00 PM", "academic"), ("1:30 PM", "3:00 PM", "academic")],  # Tuesday
    [("9:00 AM", "10:30 AM", "academic")],  # Wednesday
    [("10:30 AM", "12:00 PM", "academic"), ("1:30 PM", "4:30 PM", "academic")],  # Thursday
    [("10:30 PM", "12:00 PM", "academic"), ("12:30 PM", "2:00 PM", "academic")],  # Friday
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

class Actor:
    def __init__(self, name, max_hours_per_week):
        self.name = name
        self.max_hours_per_week = max_hours_per_week
        self.schedule = Schedule(name)

    def __str__(self):
        actor_info = f"Actor: {self.name}\n"
        actor_info += f"Max Hours per Week: {self.max_hours_per_week}\n"
        actor_info += "Schedule:\n"
        for day, conflicts in self.schedule.schedule.items():
            actor_info += f"Day {day}:\n"
            for conflict in conflicts:
                start_time, end_time, conflict_type = conflict
                actor_info += f"    - {start_time} to {end_time}: {conflict_type}\n"
        return actor_info

Hannah = Actor("Hannah", 10)

Hannah_conflicts = [
    [("12:00 PM", "1:15 PM", "academic"), ("3:00 PM", "6:00 PM", "academic"), ("6:00 PM", "7:00 PM", "other")],  # Monday
    [("10:30 AM", "12:00 PM", "academic"), ("1:30 PM", "3:00 PM", "academic"), ("4:30 PM", "7:30 PM", "other")],  # Tuesday
    [],  # Wednesday (no conflicts)
    [("10:30 AM", "6:00 PM", "academic")],  # Thursday
    [],  # Friday (no conflicts)
    [],  # Saturday (no conflicts)
    [("12:30 PM", "3:00 PM", "other")],  # Sunday
]
Hannah.schedule.add_conflicts(Hannah_conflicts)

Shannon = Actor("Shannon", 10)

Shannon_conflicts = [
    [("10:30 AM", "12:00 PM", "academic"), ("1:30 PM", "3:00 PM", "academic")],  # Monday
    [("10:30 AM", "1:00 PM", "academic"), ("8:30 PM", "10:00 PM", "other")],  # Tuesday
    [("10:30 AM", "12:00 PM", "academic"), ("1:30 PM", "2:30 PM", "academic"), ("4:00 PM", "6:30 PM", "academic")],  # Wednesday
    [("10:30 AM", "2:00 PM", "academic"), ("3:00 PM", "6:00 PM", "academic"), ("7:30 PM", "9:00 PM", "other")],  # Thursday
    [("10:30 AM", "12:00 PM", "academic"), ("4:00 PM", "5:30 PM", "academic")],  # Friday
    [("2:00 PM", "4:00 PM", "other")],  # Saturday
    [("2:00 PM", "4:00 PM", "other")],  # Sunday
]
Shannon.schedule.add_conflicts(Shannon_conflicts)

Jonah = Actor("Jonah", 10)

Jonah_conflicts = [
    [("10:30 AM", "3:00 PM", "academic")],  # Monday
    [("10:30 AM", "12:00 PM", "academic"), ("2:00 PM", "6:00 PM", "other")],  # Tuesday
    [("10:30 AM", "3:00 PM", "academic")],  # Wednesday
    [("9:00 AM", "10:00 AM", "academic"), ("10:30 AM", "12:00 PM", "academic"), ("1:30 PM", "2:30 PM", "academic"), ("3:00 PM", "6:00 PM", "academic")],  # Thursday
    [("3:00 PM", "4:00 PM", "academic")],  # Friday
    [],  # Saturday
    [("2:00 PM", "7:00 PM", "other")],  # Sunday
]
Jonah.schedule.add_conflicts(Jonah_conflicts)

Kiesse = Actor("Kiesse", 10)

Kiesse_conflicts = [
    [],  # Monday
    [],  # Tuesday
    [],  # Wednesday
    [],  # Thursday
    [],  # Friday
    [],  # Saturday
    [],  # Sunday
]
Kiesse.schedule.add_conflicts(Kiesse_conflicts)

Riley = Actor("Riley", 10)

Riley_conflicts = [
    [],  # Monday
    [],  # Tuesday
    [],  # Wednesday
    [],  # Thursday
    [],  # Friday
    [],  # Saturday
    [],  # Sunday
]
Riley.schedule.add_conflicts(Riley_conflicts)

Andreea = Actor("Andreea", 10)

Andreea_conflicts = [
    [],  # Monday
    [],  # Tuesday
    [],  # Wednesday
    [],  # Thursday
    [],  # Friday
    [],  # Saturday
    [],  # Sunday
]
Andreea.schedule.add_conflicts(Andreea_conflicts)

Ria = Actor("Ria", 10)

Ria_conflicts = [
    [],  # Monday
    [],  # Tuesday
    [],  # Wednesday
    [],  # Thursday
    [],  # Friday
    [],  # Saturday
    [],  # Sunday
]
Ria.schedule.add_conflicts(Ria_conflicts)

# input all the necessary rehearsals for the full rehearsal period (estimate as 4 weeks)
    # this can be a class so that each rehearsal name has a type (staging, music, choreo), how long it'll take
    # and which people are needed for the rehearsal

class Rehearsal:
    def __init__(self, name, rehearsal_type, duration, required_people):
        self.name = name
        self.type = rehearsal_type
        self.duration = duration # in hours
        self.required_people = required_people

# set limit for how many hours an actor can be called per week
    # most likely 10 hours

# assign rehearsal times based on minimum 80% actor availability for group rehearsals, 100% availability for
# small group or solo rehearsals 
    # raise an error that says that an actor has been called for too many hours if necessary

rehearsal_blocks = [i * 0.25 for i in range(36, int(24 / 0.25))]

def is_available(time, unavailable_periods):
    for start, end in unavailable_periods:
        if start <= time < end:
            return False
    return True

# Convert decimal hours to 12-hour format with AM/PM
def format_time(decimal_time):
    hours = int(decimal_time)
    minutes = int((decimal_time - hours) * 60)
    period = "AM" if hours < 12 else "PM"
    hours = hours % 12
    if hours == 0:
        hours = 12
    return f"{hours}:{minutes:02d} {period}"

def assign_rehearsal_times(rehearsals, actors, staff_members):
    rehearsal_blocks_weekdays = [i * 0.25 for i in range(72, int(24 / 0.25))]  # From 6 PM to midnight
    day_names = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    rehearsal_blocks_weekends = [i * 0.25 for i in range(40, int(24 / 0.25))] # From 10 AM to midnight

    for rehearsal in rehearsals:
        print(f"Checking availability for {rehearsal.name}:")
        required_roles = {"staging": "director", "music": "music_director", "choreo": "choreographer"}
        required_people = rehearsal.required_people[:]
        
        if rehearsal.type in required_roles:
            # Assume director, music_director, choreographer are names of the staff objects
            role_name = required_roles[rehearsal.type]
            for staff in staff_members:
                if staff.role == role_name:
                    required_people.append(staff.name)
        
        print(f"{required_people} must all be present") # just so I can check that it's working

        # Gather all conflicts from required participants
        all_conflicts = {day: [] for day in range(1, 8)}
        for person in actors + staff_members:
            if person.name in required_people:
                for day in range(1, 8):
                    all_conflicts[day].extend(person.schedule.schedule[day])

        # Determine available times for each day
        for day in range(1, 6):
            day_conflicts = [(start, end) for start, end, _ in all_conflicts[day]]
            available_times = [format_time(time) for time in rehearsal_blocks_weekdays if is_available(time, day_conflicts)]
            print(f"Available times on {day_names[day-1]}: {available_times}")

        for day in range(6, 8):
            day_conflicts = [(start, end) for start, end, _ in all_conflicts[day]]
            available_times = [format_time(time) for time in rehearsal_blocks_weekends if is_available(time, day_conflicts)]
            print(f"Available times on {day_names[day-1]}: {available_times}")

# Define participants, their schedules, and rehearsals, then call assign_rehearsal_times

blue_wind_music = Rehearsal("Blue Wind Music", "music", 1, ["Hannah"])
word_of_your_body_staging = Rehearsal("Word of Your Body Staging", "staging", 1, ["Shannon", "Jonah"])
mama_who_bore_me_reprise_choreo = Rehearsal("Mama Who Bore Me Reprise Choreo", "choreo", 1, ["Shannon", "Kiesse", "Ria", "Riley", "Andreea", "Hannah"])

rehearsals = [blue_wind_music, word_of_your_body_staging, mama_who_bore_me_reprise_choreo]
actors = [Hannah, Shannon, Jonah, Kiesse, Ria, Riley, Andreea]
staff_members = [Fahim, Grace, Caron, Adrienne]
assign_rehearsal_times(rehearsals, actors, staff_members)

