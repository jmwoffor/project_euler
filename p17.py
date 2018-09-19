# Project Euler 17
# If all the numbers from 1 to 1000 (inclusive) were written out in words, how
# many letters would be used?

letters = 0
# need a dictionary of unique words
num2word = {1:"one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six",
    7: "seven", 8: "eight", 9: "nine", 10: "ten", 11: "eleven", 12: "twelve",
    13: "thirteen", 14: "fourteen", 15: "fifteen", 16: "sixteen", 17: "seventeen",
    18: "eighteen", 19: "nineteen", 20: "twenty", 30: "thirty", 40: "forty",
    50: "fifty", 60: "sixty", 70: "seventy", 80: "eighty", 90: "ninety"}
hundred = 7 # length of word hundred
nd = 3 # length of word "and"

for i in range(1,1001):
    if 1 <= i <= 19:
        letters += len(num2word[i])
        #print(i)
    elif 20 <= i <= 99:
        tens, ones = divmod(i,10)
        if ones != 0:
            letters += len(num2word[tens*10]) + len(num2word[ones])
            #print(i)
        else:
            letters += len(num2word[tens*10])
            #print(i)
    elif 100 <= i <= 999:
        hundreds, tens1 = divmod(i,100)
        tens2, ones = divmod(tens1,10)
        if tens2 != 0: # not 100,101
            if ones != 0 and tens1 > 19: # for 121, 333, etc.
                letters += len(num2word[hundreds]) + hundred + nd + len(num2word[tens2*10]) + len(num2word[ones])
                #print(len(num2word[hundreds])+hundred+nd+len(num2word[tens2*10])+len(num2word[ones]))
                #print(i)
            elif 11 <= tens1 <= 19: # for 111, 119, 211, etc.
                letters += len(num2word[hundreds]) + hundred + nd +len(num2word[tens1])
                #print(i)
            else: # for 110, 130, 250, etc.
                letters += len(num2word[hundreds]) + hundred + nd + len(num2word[tens2*10])
                #print(i)
        elif tens2 == 0 and ones != 0: # for 101, 303, etc.
            letters += len(num2word[hundreds]) + hundred + nd + len(num2word[ones])
            #print(i)
        else: # for 100, 200
            letters += len(num2word[hundreds]) + hundred
            #print(i)
    else: # for 1000
        letters += 11 # number of letters in "one thousand"
        #print(i)
print(letters)
