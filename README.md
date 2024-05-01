# CS 32 Final Project
CS32 Final Project - Fahim, Lucas, Kiesse

Rehearsal Scheduler: Replace every stage manager ever. Schedule daily rehearsals for a show based on the schedules of each actor and rehearsal staff member and the different rehearsals that we need to get done and how long those rehearsals will take.

Instructions:

staff_schedules.py contains the schedules of all staff members. In staff_schedules.py, for each staff member, initialize an object of class Staff with three parameters: staff member name (string), staff member role (music_director, director, or choreographer), and maximum hours that the individual can be called per week for rehearsal (int). Example:
		Fahim = Staff(“Fahim”, “music_director”, 20)

For each staff member, create a list of length 7 to enter the individual’s recurring weekly conflicts by day, where each item in the list is also a list. The first entry in the list corresponds to Monday and continues chronologically until the last item in the list, which corresponds to Sunday. For each day, each conflict should be parenthesized and contain the start time, end time, and type of conflict (all three separated by commas and entered as strings). Times must be in 12-hour AM/PM format with a space in between the numerical time and the AM/PM demarcation, i.e., “10:30 AM”. Example:
		Fahim_conflicts = [
		[(“10:30 AM”, “12:00 PM”, “academic”), (“6:00 PM”, “9:00 PM”, “other”)],
		…and onwards for the rest of the days of the week. 

Add these conflicts to the staff member’s schedule using the schedule.add_conflicts function. Example:
		Fahim.schedule.add_conflicts(Fahim_conflicts)

At the end of staff_schedules.py, create a list staff_members containing all the objects of class Staff.

In cast_schedules.py, follow the same steps as staff_members.py, but this time with objects of class Actor, and call the final list of all the objects of class Actor “actors”.

In rehearsal_timefinder.py, enter the rehearsals you’d like to schedule, initializing each as objects of class Rehearsal, with four parameters: name of rehearsal (string), type of rehearsal (music, blocking, or choreo) (string), time needed for the rehearsal in hours (float), actors needed for the rehearsal (list of strings).

Add all of the objects of class Rehearsal into a list (like rehearsals_week_1).

To find available rehearsal times for all rehearsals in the list, call the function find_rehearsal_times at the bottom of rehearsal_timefinder.py with three parameters (rehearsal list, actors, staff_members). Run rehearsal_timefinder.py in the terminal.

If no time is found for a rehearsal in the entire week, you will be prompted to input “yes” or “no” if you would like to search for rehearsal times with 90% actor availability. If no times are found again, this will decrease to 80% and onwards down to 50%.

To assign rehearsals in order of first-available times instead of searching for all possible times, call the function assign_rehearsals at the bottom of rehearsal_assigner.py with the same three parameters as find_rehearsal_times.

