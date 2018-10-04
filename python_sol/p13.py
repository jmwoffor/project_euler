# Project Euler #13
# What are the first ten digits of the sum of the following one hundred 50 digit numbers

sum = 0

data = open("p13_data.txt", "r")

for line in data:
    num = line.rstrip()
    sum += int(num)

long_ass_string = str(sum)
print(long_ass_string[0:10])
