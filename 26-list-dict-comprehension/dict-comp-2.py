week_temps_f = {
'Monday': 53.6,
'Tuesday': 57.2,
'Wednesday': 59.0,
'Thursday': 57.2,
'Friday': 69.8,
'Saturday': 71.6,
'Sunday': 75.2
}

week_temps_c = {day: {'fahrenheit': temp, 'celsius': round(((temp - 32) * 5/9), 2)} for (day, temp) in week_temps_f.items()}

print(week_temps_c)

week_temps_c = {day: round((temp - 32) * 5/9) for (day, temp) in week_temps_f.items()}
print(week_temps_c)