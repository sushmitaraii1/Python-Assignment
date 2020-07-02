# 2. Write an if statement to determine whether a variable holding a year
# is a leap year.
import datetime
current_year = datetime.datetime.now().year

if (current_year % 4) == 0:
    if (current_year % 100) == 0:
        if (current_year % 400) == 0:
            print("{} is  a leap year.".format(current_year))
        else:
            print("{} is not a leap year.".format(current_year))
    else:
        print("{} is a leap year.".format(current_year))
else:
    print("{} is not leap year.".format(current_year))


