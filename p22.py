# Sort names.txt into alphabetical order. Working out the alphabetical value
# for each name, multiply this value by its alphabetical position in the list
# to obtain a name score. What is the total of all the name scores in the file?

names = []

with open('p022_names.txt') as f:
    names_raw = f.read()

for name in names_raw:
    names.append(names_raw.split(','))

print(names)
