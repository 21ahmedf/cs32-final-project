from datetime import datetime, timedelta
import calendar

# input all the necessary rehearsals for the full rehearsal period (estimate as 4 weeks)
    # this can be a class so that each rehearsal name has a type (staging, music, choreo), how long it'll take
    # and which people are needed for the rehearsal

class Rehearsal:
    def __init__(self, name, rehearsal_type, duration, required_people):
        self.name = name
        self.type = rehearsal_type
        self.duration = duration # in hours
        self.required_people = required_people

blue_wind_music = Rehearsal("Blue Wind Music", "music", 1, ["Hannah"])
word_of_your_body_staging = Rehearsal("Word of Your Body Staging", "staging", 1, ["Shannon", "Jonah"])
mama_who_bore_me_reprise_choreo = Rehearsal("Mama Who Bore Me Reprise Choreo", "choreo", 1, ["Shannon", "Kiesse", "Ria", "Riley", "Andreea", "Hannah"])

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
        for day, conflicts in zip(range(1, 8), conflicts_per_day):
            self.schedule[day].extend(conflicts)

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

actors = [Hannah]

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

print(Hannah)

# print(Hannah_schedule.schedule)

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
    [("10:30 PM", "12:00 PM", "academic"), ("12:30 PM", "2:00 PM", "academic"), ("3:00 PM", "4:00 PM", "other")],  # Monday
    [("9:00 AM", "12:00 PM", "academic"), ("12:00 PM", "1:00 PM", "other"), ("1:30 PM", "3:00 PM", "academic"), ("5:00 PM", "6:30 PM", "other"), ("7:30 PM", "9:30 PM", "other")],  # Tuesday
    [("9:00 AM", "12:00 PM", "academic"), ("12:30 PM", "2:00 PM", "academic"), ("3:00 PM", "6:00 PM", "academic")],  # Wednesday
    [("9:00 AM", "12:00 PM", "academic"), ("1:30 PM", "3:00 PM", "academic"), ("5:00 PM", "6:30 PM", "other")],  # Thursday
    [("10:30 PM", "12:00 PM", "academic"), ("12:30 PM", "2:00 PM", "academic")],  # Friday (no conflicts)
    [],  # Saturday (no conflicts)
    [("9:30 AM", "12:30 PM", "other"), ("4:00 PM", "6:00 PM", "other")],  # Sunday
]
Fahim.schedule.add_conflicts(Fahim_conflicts)

staff_members = [Fahim]

print(Fahim)

# set limit for how many hours an actor can be called per week
    # most likely 10 hours

# assign rehearsal times based on minimum 80% actor availability for group rehearsals, 100% availability for
# small group or solo rehearsals 
    # raise an error that says that an actor has been called for too many hours if necessary

def assign_rehearsal_times(rehearsals, actors, staff_members):
    for rehearsal in rehearsals:
        required_people = rehearsal.required_people
        if rehearsal.type == "staging":
            required_people.append("director")
        elif rehearsal.type == "music":
            required_people.append("music_director")
        elif rehearsal.type == "choreo":
            required_people.append("choreographer")

        for participant in actors + staff_members:
            participant_schedule = participant.schedule.schedule
            available_time_slots = []
            for day, conflicts in participant_schedule.items():
                day_name = calendar.day_name[day - 1]  # Translate day number to day name
                if not conflicts:
                    available_time_slots.append((day_name, "6:00 PM", "11:30 PM"))
                else:
                    for conflict in conflicts:
                        start_time, end_time = conflict[0], conflict[1]
                        # need to add conflicts into set of unavailable time slots
                    # then see what values in between 6:00 PM and 11:30 PM don't overlap with the
                    # unavailable time slots and add those open times to available time slots instead

            for day, start_time, end_time in available_time_slots:
                duration = rehearsal.duration
                rehearsal_end_time = (datetime.strptime(start_time, "%I:%M %p") + timedelta(hours=duration)).strftime("%I:%M %p")

                # Check if all required participants are available
                all_available = True
                for required_person in required_people:
                    if required_person not in participant.name:
                        all_available = False
                        break

                if all_available and end_time <= "11:30 PM":
                    print(f"All required participants are available for {rehearsal.name} on {day} from {start_time} to {rehearsal_end_time}")

rehearsals = [blue_wind_music]
assign_rehearsal_times(rehearsals, actors, staff_members)
