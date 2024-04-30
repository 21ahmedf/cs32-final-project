from datetime import datetime
from staff_schedules import *
from cast_schedules import *
day_names = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

# Function to convert time from 12-hour format to decimal hour military time
def convert_to_military(time_str):
    # Parse the time string into a datetime object
    time_obj = datetime.strptime(time_str, "%I:%M %p")
    # Convert to military time in decimal hours
    return time_obj.hour + time_obj.minute / 60

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
    
Fahim_onetime = [[],[],[],[("7:00 PM", "9:30 PM", "other")],[],[],[]]
# Thursday one-time conflict for BachSoc Orchestra

Fahim.schedule.add_conflicts(Fahim_onetime)

Oasis_onetime = [[],[],[],[],[],[],[("9:45 PM", "11:45 PM", "other")]
# Sunday one-time conflict for Oasis, pertains to both choreographers

Adrienne.schedule.add_conflicts(Oasis_onetime)
Caron.schedule.add_conflicts(Oasis_onetime)
