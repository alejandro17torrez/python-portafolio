month = int(input("Add the month: "))
hours_per_day = float(input("Add the hours per day: "))
days_per_week = int(input("Add the days per week: "))

WEEKS = 4
RANGES = {
    "months": range(1, 13),
    "days": range(1, 8),
    "hours": range(1, 17),
}

if month not in RANGES["months"]:
    raise ValueError("Invalid month, it has to be between 1 and 12")

if days_per_week not in RANGES["days"]:
    raise ValueError("Invalid days per week, it has to be between 1 to 7")

if hours_per_day not in RANGES["hours"]:
    raise ValueError("Invalid hours per day, it has to be between 1 to 16")
