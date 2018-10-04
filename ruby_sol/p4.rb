#!/usr/bin/ruby
# Find the largest palindrome made from the product of two 3-digit numbers

num = 999
palin = []

while num > 100
  (100..num).each do |i|
      prod = num*i
      test = prod.to_s
      if test == test.reverse
        palin.push(test.to_i)
      end
  end
  num -= 1
end

puts palin.max
