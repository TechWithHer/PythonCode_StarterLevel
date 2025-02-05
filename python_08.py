#On what date a particular day happens?

import datetime
m = int(input("Enter the month: "))
d = int(input("Enter the day: "))
y = int(input("Enter the year: "))

day = datetime.date(y, m, d)

print(day.strftime("%A"))

''' 
%A	Wednesday (Full weekday name)
%a	Wed (Abbreviated weekday name)
%B	February (Full month name)
%b	Feb (Abbreviated month name)
%d	05 (Day of the month)
%m	02 (Month number)
%Y	2025 (Full year)
%y	25 (Last two digits of year) '''