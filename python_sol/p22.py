# Sort names.txt into alphabetical order. Working out the alphabetical value
# for each name, multiply this value by its alphabetical position in the list
# to obtain a name score. What is the total of all the name scores in the file?

import csv

with open('p022_names.txt', newline = '') as f:
    raw_names = list(csv.reader(f,delimiter = ","))

names = raw_names[0] # raw_names is a weird nested list [[]] so this grabs list
names = sorted(names) # sorts names alphabetically

a = {"A":1, "B":2, "C":3, "D":4, "E":5, "F":6, "G":7, "H":8, "I":9, "J":10, "K":11,
    "L":12, "M":13, "N":14, "O":15, "P":16, "Q":17, "R":18, "S":19, "T":20, "U":21,
    "V":22, "W":23, "X":24, "Y":25, "Z":26} # set up dictionary for name scores

n = 1 # counter for position of name in list
total = 0

for i in names:
    name = list(i)
    sum = 0
    for j in name:
        sum += a[j] # calculates alphabetical value for each name
    total += sum*n
    n += 1

print(total)
