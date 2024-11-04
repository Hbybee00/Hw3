#Hayden Bybee
#Lab Section 16
#11/04/24
#Sources, Help given to/received from:
#I got some help fixing my While loop from my brother after writing it as well as figuring out formatting my weekday function


# jan, march, may, july, august, oct, dec - 31
#apr, june, sep, nov - 30
#feb 28 ry 29 ly

Leapyear = False

while True:
    yearinp = input("To find the day of the week for a date, enter in MM/DD/YYYY format!")
    date = yearinp.split("/")
    if len(date) != 3 or not date[0].isdigit() or not date[1].isdigit() or not date[2].isdigit() or len(date[2]) != 4:
        print("Invalid date format!:(")
        continue
    else:
            month = int(date[0])
            day =int(date[1])
            year = int(date[2])
            if month > 12 or month < 1:
                print("Uhoh, invalid month!")
                continue
            elif month <= 12 and month >= 1:
                if month in [1,3,5,7,8,10,12]:
                    if day > 31 or day < 1:
                        print("Invalid day, this month has 31 days!")
                        continue
                    else:
                        break
                elif month in [4,6,9,11]:
                    if day > 30 or day < 1:
                        print("Invalid day, this month has 30 days!")
                        continue
                    else:
                        break
                elif month == 2:
                    if year%100 != 0 and year%4 == 0:
                        Leapyear = True
                    elif year%400 == 0:
                        Leapyear = True
                if Leapyear == True:
                    if day > 29:
                        print("Not a valid day, this is a leap year, so February has 29 days!")
                        continue
                    elif day <= 29 and day > 0:
                        break
                elif Leapyear == False:
                    if day > 28:
                        print("Not a valid day, Febraury only has 28 days that year!")
                        continue
                    elif day <= 28 and day > 0:
                        break

Weekdays = {0:"Sunday",1:"Monday",2:"Tuesday",3:"Wednesday",4:"Thursday",5:"Friday",6:"Saturday"}

def weekday(month,day,year):
    """This function finds the day of the week based on the date."""
    if month < 3:
        year = year - 1
        month += 12
    var1 = year%100
    var2 = year/100       
    output = (day + ((13*(month + 1))/5) + var1 + (var1/4) + var2 - (2*var2))%7
    return output
#I couldn't understand how to find the day of the week based off of just what january was, so I just based it off of the equation instead, sorry D:

if weekday(month,day,year) < 1:
    date = 0
elif weekday(month,day,year) < 2 and weekday(month,day,year) > 1:
    date = 1
elif weekday(month,day,year) < 3 and weekday(month,day,year) > 2:
    date = 2
elif weekday(month,day,year) < 4 and weekday(month,day,year) > 3:
    date = 3
elif weekday(month,day,year) < 5 and weekday(month,day,year) > 4:
    date = 4
elif weekday(month,day,year) < 6 and weekday(month,day,year) > 5:
    date = 5
else:
    date = 6

for keys, items in Weekdays.items():
    if keys == date:
        answerday = yearinp + " " + items

print(answerday)
