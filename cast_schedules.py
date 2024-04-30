from staff_schedules import Schedule

# input each actor's schedules manually, this part of the code will vary each week, but recurring conflicts will stay
    # schedules for each person can be split by day
    # conflict type should either be "academic" or "other"

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


actors = [Jonah, Shannon, Nikhil, Hannah, Andreea, Andrew, Jared, Sean, Ben, Kiesse, Riley,
          Ria, Daniela, Texaco, Anna, Lindsay, Rob, Alvin, Saswato, Mattheus]
upper_voices = ["Shannon", "Hannah", "Andreea", "Kiesse", "Riley", "Ria", "Anna", "Daniela", "Lindsay", "Texaco"]
lower_voices = ["Jonah", "Nikhil", "Andrew", "Jared", "Sean", "Ben", "Rob", "Alvin", "Saswato", "Mattheus"]
ALL = upper_voices + lower_voices