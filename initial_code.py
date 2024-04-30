from datetime import datetime
import numpy as np

# Function to convert time from 12-hour format to decimal hour military time
def convert_to_military(time_str):
    # Parse the time string into a datetime object
    time_obj = datetime.strptime(time_str, "%I:%M %p")
    # Convert to military time in decimal hours
    return time_obj.hour + time_obj.minute / 60

day_names = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

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
    # director's schedule is relevant to all types of rehearsals, but essential for blocking rehearsals

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

Nikhil = Actor("Nikhil", 10)

Nikhil_conflicts = [
    [("9:00 AM", "3:00 PM", "academic"), ("7:30 PM", "9:30 PM", "other")],  # Monday
    [("10:30 AM", "12:00 PM", "academic"), ("1:30 PM", "3:00 PM", "academic")],  # Tuesday
    [("9:00 AM", "12:00 PM", "academic"), ("3:00 PM", "5:00 PM", "academic")],  # Wednesday
    [("10:30 AM", "12:00 PM", "academic")],  # Thursday
    [("10:30 AM", "12:00 PM", "academic"), ("4:30 PM", "5:00 PM", "other")],  # Friday
    [("12:00 PM", "1:00 PM", "other"), ("5:00 PM", "6:00 PM", "other")],  # Saturday
    [],  # Sunday
]
Nikhil.schedule.add_conflicts(Nikhil_conflicts)

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

Andreea = Actor("Andreea", 10)

Andreea_conflicts = [
    [("12:00 PM", "1:30 PM", "academic")],  # Monday
    [("9:30 AM", "11:00 AM", "academic"), ("1:30 PM", "5:00 PM", "academic"), ("7:30 PM", "10:00 PM", "other")],  # Tuesday
    [("12:00 PM", "1:30 PM", "academic"), ("3:00 PM", "4:30 PM", "academic"), ("7:30 PM", "10:00 PM", "other")],  # Wednesday
    [("9:30 AM", "11:00 AM", "academic"), ("1:30 PM", "5:00 PM", "academic")],  # Thursday
    [("1:00 PM", "3:30 PM", "academic")],  # Friday
    [],  # Saturday
    [("6:15 PM", "8:45 PM", "other")],  # Sunday
]
Andreea.schedule.add_conflicts(Andreea_conflicts)

Kiesse = Actor("Kiesse", 10)

Kiesse_conflicts = [
    [("9:00 AM", "2:00 PM", "academic"), ("6:00 PM", "8:00 PM", "other")],  # Monday
    [("12:00 PM", "1:30 PM", "academic"), ("5:00 PM", "6:30 PM", "other"), ("8:30 PM", "10:00 PM", "other")],  # Tuesday
    [("9:00 AM", "2:00 PM", "academic")],  # Wednesday
    [("12:00 PM", "1:30 PM", "academic"), ("3:00 PM", "4:00 PM", "academic"), ("5:00 PM", "6:30 PM", "other"), ("7:30 PM", "9:00 PM", "other")],  # Thursday
    [("12:30 PM", "2:00 PM", "academic"), ("4:30 PM", "6:30 PM", "other")],  # Friday
    [("2:00 PM", "4:00 PM", "other")],  # Saturday
    [("9:30 AM", "12:30 PM", "other"), ("2:00 PM", "4:00 PM", "other")],  # Sunday
]
Kiesse.schedule.add_conflicts(Kiesse_conflicts)

Riley = Actor("Riley", 10)

Riley_conflicts = [
    [("10:30 AM", "1:30 PM", "academic"), ("4:30 PM", "6:00 PM", "academic")],  # Monday
    [("1:00 PM", "6:00 PM", "academic")],  # Tuesday
    [("10:30 AM", "3:00 PM", "academic"), ("4:30 PM", "6:00 PM", "academic")],  # Wednesday
    [("10:30 AM", "11:30 AM", "academic"), ("1:30 PM", "2:30 PM", "academic"), ("3:00 PM", "5:00 PM", "academic")],  # Thursday
    [],  # Friday
    [],  # Saturday
    [],  # Sunday
]
Riley.schedule.add_conflicts(Riley_conflicts)

Ria = Actor("Ria", 10)

Ria_conflicts = [
    [("9:00 AM", "10:30 AM", "academic"), ("12:00 PM", "3:00 PM", "academic"), ("6:00 PM", "8:00 PM", "other")],  # Monday
    [("9:30 AM", "1:00 PM", "academic"), ("8:30 PM", "10:00 PM", "other")],  # Tuesday
    [("9:00 AM", "10:30 AM", "academic"), ("12:00 PM", "9:00 PM", "academic")],  # Wednesday
    [("12:00 PM", "1:00 PM", "academic"), ("7:30 PM", "9:00 PM", "other")],  # Thursday
    [("12:00 PM", "1:00 PM", "academic")],  # Friday
    [("2:00 PM", "4:00 PM", "other")],  # Saturday
    [("11:30 AM", "12:30 PM", "academic"), ("2:00 PM", "5:00 PM", "other")],  # Sunday
]
Ria.schedule.add_conflicts(Ria_conflicts)

Andrew = Actor("Andrew", 10)

Andrew_conflicts = [
    [("3:00 PM", "4:30 PM", "academic"), ("6:30 PM", "8:30 PM", "other")],  # Monday
    [("10:30 AM", "12:00 PM", "academic"), ("1:30 PM", "3:00 PM", "academic")],  # Tuesday
    [("3:00 PM", "4:30 PM", "academic")],  # Wednesday
    [("10:30 AM", "12:00 PM", "academic"), ("1:30 PM", "5:00 PM", "academic")],  # Thursday
    [],  # Friday
    [],  # Saturday
    [],  # Sunday
]
Andrew.schedule.add_conflicts(Andrew_conflicts)

Jared = Actor("Jared", 10)

Jared_conflicts = [
    [("10:30 AM", "1:30 PM", "academic"), ("3:00 PM", "4:30 PM", "academic"), ("5:00 PM", "6:00 PM", "other"), ("8:30 PM", "10:30 PM", "other")],  # Monday
    [("9:00 AM", "12:00 PM", "academic"), ("1:30 PM", "4:30 PM", "academic")],  # Tuesday
    [("10:30 AM", "1:30 PM", "academic"), ("3:00 PM", "5:00 PM", "academic")],  # Wednesday
    [("9:00 AM", "10:30 AM", "academic"), ("1:30 PM", "6:00 PM", "academic")],  # Thursday
    [("12:00 PM", "1:30 PM", "academic")],  # Friday
    [],  # Saturday
    [("11:00 AM", "12:00 PM", "other")],  # Sunday
]
Jared.schedule.add_conflicts(Jared_conflicts)

Sean = Actor("Sean", 10)

Sean_conflicts = [
    [("1:30 PM", "3:00 PM", "academic"), ("6:00 PM", "8:00 PM", "other")],  # Monday
    [("10:30 AM", "4:00 PM", "academic"), ("7:00 PM", "8:00 PM", "other"), ("8:30 PM", "10:00 PM", "other")],  # Tuesday
    [("1:30 PM", "3:00 PM", "academic"), ("6:00 PM", "8:00 PM", "other")],  # Wednesday
    [("12:30 PM", "5:00 PM", "academic"), ("7:30 PM", "9:00 PM", "other")],  # Thursday
    [("10:30 AM", "11:30 AM", "academic")],  # Friday
    [("2:00 PM", "4:00 PM", "other")],  # Saturday
    [("2:00 PM", "5:00 PM", "other")],  # Sunday
]
Sean.schedule.add_conflicts(Sean_conflicts)

Ben = Actor("Ben", 10)

Ben_conflicts = [
    [("10:30 AM", "5:00 PM", "academic"), ("6:30 PM", "9:30 PM", "other")],  # Monday
    [("8:30 PM", "10:00 PM", "other")],  # Tuesday
    [("10:30 AM", "3:00 PM", "academic")],  # Wednesday
    [("3:00 PM", "4:00 PM", "academic"), ("7:30 PM", "9:00 PM", "other")],  # Thursday
    [("12:00 PM", "3:00 PM", "academic"), ("3:00 PM", "5:30 PM", "other")],  # Friday
    [("2:00 PM", "4:00 PM", "other")],  # Saturday
    [("2:00 PM", "4:00 PM", "other")],  # Sunday
]
Ben.schedule.add_conflicts(Ben_conflicts)

Texaco = Actor("Texaco", 10)

Texaco_conflicts = [
    [("1:00 PM", "4:30 PM", "other")],  # Monday
    [("9:00 AM", "12:00 PM", "academic"), ("2:00 PM", "5:00 PM", "other")],  # Tuesday
    [("9:00 AM", "10:30 AM", "other"), ("12:00 PM", "3:00 PM", "academic")],  # Wednesday
    [("9:00 AM", "1:00 PM", "academic"), ("2:00 PM", "4:30 PM", "other"), ("6:00 PM", "8:00 PM", "academic")],  # Thursday
    [("10:00 AM", "4:30 PM", "academic"), ("6:00 PM", "7:00 PM", "other")],  # Friday
    [("5:00 PM", "6:00 PM", "other")],  # Saturday
    [],  # Sunday
]
Texaco.schedule.add_conflicts(Texaco_conflicts)

Anna = Actor("Anna", 10)

Anna_conflicts = [
    [("10:30 AM", "3:00 PM", "academic")],  # Monday
    [("12:00 PM", "1:30 PM", "academic"), ("3:30 PM", "6:00 PM", "academic")],  # Tuesday
    [("10:30 AM", "12:00 PM", "academic"), ("3:00 PM", "6:00 PM", "academic"), ("6:00 PM", "7:00 PM", "other")],  # Wednesday
    [("12:00 PM", "3:00 PM", "academic")],  # Thursday
    [("10:30 AM", "12:00 PM", "academic")],  # Friday
    [],  # Saturday
    [("2:00 PM", "3:00 PM", "other")],  # Sunday
]
Anna.schedule.add_conflicts(Anna_conflicts)

Lindsay = Actor("Lindsay", 10)

Lindsay_conflicts = [
    [("6:00 PM", "7:00 PM", "academic"), ("7:30 PM", "8:30 PM", "other")],  # Monday
    [("10:30 AM", "2:00 PM", "academic"), ("3:00 PM", "4:30 PM", "academic"), ("8:00 PM", "9:30 PM", "other")],  # Tuesday
    [("9:00 AM", "10:00 AM", "academic"), ("6:30 PM", "7:30 PM", "other")],  # Wednesday
    [("10:30 AM", "12:00 PM", "academic"), ("3:00 PM", "4:30 PM", "academic")],  # Thursday
    [("9:00 AM", "10:00 AM", "academic"), ("2:30 PM", "5:00 PM", "other")],  # Friday
    [("9:00 PM", "10:00 PM", "other")],  # Saturday
    [],  # Sunday
]
Lindsay.schedule.add_conflicts(Lindsay_conflicts)

Daniela = Actor("Daniela", 10)

Daniela_conflicts = [
    [("10:30 AM", "2:00 PM", "academic"), ("3:00 PM", "5:00 PM", "academic")],  # Monday
    [("2:00 PM", "5:00 PM", "other")],  # Tuesday
    [("10:30 AM", "2:00 PM", "academic"), ("5:30 PM", "9:00 PM", "other")],  # Wednesday
    [("3:00 PM", "6:00 PM", "academic")],  # Thursday
    [("10:30 AM", "12:00 PM", "academic"), ("2:30 PM", "3:30 PM", "academic")],  # Friday
    [],  # Saturday
    [],  # Sunday
]
Daniela.schedule.add_conflicts(Daniela_conflicts)

Rob = Actor("Rob", 10)

Rob_conflicts = [
    [("12:00 PM", "1:30 PM", "academic"), ("8:00 PM", "10:00 PM", "other")],  # Monday
    [("10:30 AM", "1:30 PM", "academic")],  # Tuesday
    [("9:30 AM", "1:30 PM", "academic"), ("6:30 PM", "8:30 PM", "other")],  # Wednesday
    [("9:00 AM", "1:30 PM", "academic")],  # Thursday
    [("12:00 PM", "1:00 PM", "academic")],  # Friday
    [],  # Saturday
    [("1:00 PM", "3:00 PM", "other")],  # Sunday
]
Rob.schedule.add_conflicts(Rob_conflicts)

Alvin = Actor("Alvin", 10)

Alvin_conflicts = [
    [("10:30 AM", "12:00 PM", "academic"), ("3:00 PM", "4:30 PM", "academic")],  # Monday
    [("9:30 AM", "2:00 PM", "academic")],  # Tuesday
    [("1:00 PM", "2:30 PM", "other"), ("3:00 PM", "4:30 PM", "academic"), ("7:00 PM", "10:00 PM", "other")],  # Wednesday
    [("9:30 AM", "2:00 PM", "academic"), ("8:00 PM", "10:00 PM", "other")],  # Thursday
    [("2:00 PM", "5:00 PM", "academic")],  # Friday
    [],  # Saturday
    [("12:00 PM", "2:00 PM", "other"), ("3:00 PM", "5:00 PM", "other")],  # Sunday
]
Alvin.schedule.add_conflicts(Alvin_conflicts)

Saswato = Actor("Saswato", 10)

Saswato_conflicts = [
    [("9:00 AM", "10:30 AM", "academic"), ("1:30 PM", "3:00 PM", "academic"), ("4:30 PM", "9:00 PM", "other")],  # Monday
    [("1:00 PM", "1:30 PM", "other"), ("1:30 PM", "6:00 PM", "academic"), ("9:30 PM", "10:30 PM", "other")],  # Tuesday
    [("9:00 AM", "10:30 AM", "academic"), ("1:30 PM", "6:00 PM", "academic"), ("6:00 PM", "7:30 PM", "other")],  # Wednesday
    [("9:30 AM", "12:00 PM", "academic"), ("3:00 PM", "6:00 PM", "academic")],  # Thursday
    [("9:00 AM", "10:30 AM", "academic"), ("12:00 PM", "1:30 PM", "academic")],  # Friday
    [],  # Saturday
    [("9:30 PM", "10:30 PM", "other")],  # Sunday
]
Saswato.schedule.add_conflicts(Saswato_conflicts)

Mattheus = Actor("Mattheus", 10)

Mattheus_conflicts = [
    [("1:30 PM", "3:00 PM", "academic"), ("3:00 PM", "5:00 PM", "other")],  # Monday
    [("12:00 PM", "3:00 PM", "academic")],  # Tuesday
    [("1:30 PM", "4:30 PM", "academic")],  # Wednesday
    [("12:00 PM", "6:00 PM", "academic"), ("7:30 PM", "9:15 PM", "other")],  # Thursday
    [("3:00 PM", "5:00 PM", "other")],  # Friday
    [],  # Saturday
    [],  # Sunday
]
Mattheus.schedule.add_conflicts(Mattheus_conflicts)

upper_voices = ["Shannon", "Hannah", "Andreea", "Kiesse", "Riley", "Ria", "Anna", "Daniela", "Lindsay", "Texaco"]
lower_voices = ["Jonah", "Nikhil", "Andrew", "Jared", "Sean", "Ben", "Rob", "Alvin", "Saswato", "Mattheus"]
ALL = upper_voices + lower_voices

# input all the necessary rehearsals for the full rehearsal period (estimate as 4 weeks)
    # this can be a class so that each rehearsal name has a type (blocking, music, choreo), how long it'll take
    # and which people are needed for the rehearsal

class Rehearsal:
    def __init__(self, name, rehearsal_type, duration, required_people):
        self.name = name
        self.type = rehearsal_type
        self.duration = duration # in hours
        self.required_people = required_people

# assign rehearsal times based on minimum 80% actor availability for group rehearsals, 100% availability for
# small group or solo rehearsals 
    # raise an error that says that an actor has been called for too many hours if necessary

# Convert decimal hours to 12-hour format with AM/PM
def format_time(decimal_time):
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

def assign_rehearsal_times(rehearsals, actors, staff_members):
    rehearsal_blocks_weekdays = [i * 0.25 for i in range(72, int(23.75 / 0.25))]  # From 6 PM to 11:30 PM
    rehearsal_blocks_weekends = [i * 0.25 for i in range(40, int(23.75 / 0.25))] # From 10 AM to 11:30 PM
    required_roles = {"blocking": "director", "music": "music_director", "choreo": "choreographer"}

    for rehearsal in rehearsals:
        print(f"Checking availability for {rehearsal.name}:")
        required_people = rehearsal.required_people + [staff.name for staff in staff_members
                                                       if required_roles[rehearsal.type] == staff.role]
        
        print(f"{required_people} must all be present") # just so I can check that it's working

        # # Gather all conflicts from required participants
        all_conflicts = {day: [] for day in range(1, 8)}

        for person in actors + staff_members:
            if person.name in required_people:
                for day in range(1, 8):
                    all_conflicts[day].extend(person.schedule.schedule[day])

        for day in range(1, 8):
            print(f"\nDay: {day_names[day-1]}")
            day_conflicts = sorted((start, end) for start, end, _ in all_conflicts[day])
            rehearsal_blocks = rehearsal_blocks_weekdays if day <= 5 else rehearsal_blocks_weekends
            available_blocks = check_availability(rehearsal_blocks, day_conflicts, rehearsal.duration)

            if available_blocks:
                display_missing_actors(rehearsal, required_people, day, available_blocks, day_conflicts)
            else:
                print(f"No available blocks for {rehearsal.name} on this day.")

# Define participants, their schedules, and rehearsals, then call assign_rehearsal_times

# Week 1 Rehearsals
blue_wind_music = Rehearsal("[Vocal] Blue Wind", "music", 1, ["Hannah"])
touch_me_music_georg = Rehearsal("[Vocal] Touch Me - Georg", "music", .5, ["Sean"])
act_1_scene_1 = Rehearsal("[Blocking] Act 1, Scene 1", "blocking", 1, ["Texaco", "Shannon"])
act_1_scene_2_adults = Rehearsal("[Blocking] Act 1, Scene 2", "blocking", .5, ["Daniela", "Rob"])
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
my_junk_music_girls = Rehearsal("[Vocal] My Junk", "music", .5, ["Shannon", "Kiesse", "Ria", "Riley", "Andreea", "Hannah"])
mama_who_bore_me_blocking = Rehearsal("[Blocking] Mama Who Bore Me", "blocking", .5, ["Shannon", "Kiesse", "Ria", "Riley", "Andreea", "Hannah"])
mama_who_bore_me_reprise_choreo = Rehearsal("[Choreo] Mama Who Bore Me Reprise", "choreo", 1.5, ["Shannon", "Kiesse", "Ria", "Riley", "Andreea", "Hannah"])
act_1_scene_2_boys = Rehearsal("[Blocking] Act 1, Scene 2", "blocking", 1, ["Jonah", "Nikhil"])
my_junk_music_all = Rehearsal("[Vocal] My Junk", "music", 1, ALL)
touch_me_music_all = Rehearsal("[Vocal] Touch Me", "music", 1, ALL)
the_word_of_your_body_blocking = Rehearsal("[Blocking] The Word of Your Body", "blocking", .75, ["Shannon", "Jonah"])

rehearsals_week_1 = [blue_wind_music, touch_me_music_georg, touch_me_music_all, act_1_scene_1, act_1_scene_2_adults,
                     all_thats_known_blocking, jonah_vocal_review, touch_me_music_mm, touch_me_music_ernst, all_thats_known_music_boys,
                     all_thats_known_music_all, bitch_of_living_music, touch_me_music_otto, all_thats_known_choreo, mama_who_bore_me_reprise_music,
                     my_junk_music_girls, mama_who_bore_me_blocking, mama_who_bore_me_reprise_choreo, act_1_scene_2_boys, 
                     my_junk_music_all, the_word_of_your_body_blocking]
actors = [Jonah, Shannon, Nikhil, Hannah, Andreea, Andrew, Jared, Sean, Ben, Kiesse, Riley,
          Ria, Daniela, Texaco, Anna, Lindsay, Rob, Alvin, Saswato, Mattheus]
staff_members = [Fahim, Joe, Henry, Grace, Caron, Adrienne]
assign_rehearsal_times(rehearsals_week_1, actors, staff_members)