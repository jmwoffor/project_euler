# Project Euler 19
# How many Sundays fell on the first of the month during the twentieth century (1/1/1901 - 12/31/2000)
# Still not working right :*(
def is_leap_year(year):
    if year % 100 == 0:
        if year % 400 == 0:
            return True
        else:
            return False
    elif year % 4 == 0:
        return True
    else:
        return False

def get_firsts(year):
    firsts = [1,32] # starts with [1/1, 2/1]
    if is_leap_year(year) == False: # handles Feb. leap years
        firsts.append(firsts[1]+28)
    else:
        firsts.append(firsts[1]+29)
    for i in range(2,11):
        if i == 3 or i == 5 or i == 8 or i == 10: # for April, June, Sept. and November with 30 days
            firsts.append(firsts[i]+30)
        else:
            firsts.append(firsts[i]+31)
    return firsts

i = 7
sundays1990 = []
# gets sundays for 1990
while i <= 365:
    sundays1990.append(i)
    i += 7

#print(sundays1990)

def get_sundays(prev_sunday, year):
    if prev_sunday[-1] != 365:
        sundays = [prev_sunday[-1]-358]
    elif prev_sunday[-1] == 366:
        sundays = [prev_sunday[-1]-359]
    else:
        sundays = [7]

    i = sundays[0]
    sundays.pop(0)
    if is_leap_year(year) == False:
        dayz = 365
    else:
        dayz = 366
    while i <= dayz:
        sundays.append(i)
        i += 7
    return sundays

year = 1901

sunday1 = 0
prev_sunday = sundays1990

while year < 2001:
    #print(sundays)
    #print(firsts)
    sundays = get_sundays(prev_sunday,year)
    firsts = get_firsts(year)

    for j in firsts:
        if j in sundays:
            sunday1 += 1

    year += 1
print(sunday1)
