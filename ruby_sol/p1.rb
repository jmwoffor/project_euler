#!/usr/bin/ruby
# Find the sum of all the multiples of 3 or 5 below 1000

i = 1
sum = 0

while i < 1000
  if i % 15 == 0
    sum += i
  elsif i % 5 == 0
    sum += i
  elsif i % 3 == 0
    sum += i
  end
  i += 1
end

puts sum
