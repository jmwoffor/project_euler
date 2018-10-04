# Project Euler #6
# Find the difference between the sum of the square of the first 100 natural
# numbers and the square of the sum of the first 100 natural numbers

hundo = [i for i in range(1,101)]


x = [];
for i in hundo:
    x.append(i**2)

print(sum(hundo)**2 - sum(x))
