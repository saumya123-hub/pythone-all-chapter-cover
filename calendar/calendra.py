# program to print the calendar of any given year
import calendar
y = int(input("enter the year:"))
# m = 1
print("\n***************CALENDAR********************")
cal = calendar.TextCalendar(calendar.SUNDAY)
i = 1
while(i<=12):
    cal.prmonth(y,i)
    i= i+1
