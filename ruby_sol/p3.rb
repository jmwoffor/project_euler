#!/usr/bin/ruby
# Project Euler #3
# Find the greatest prime factor of 600851475143

# Don't actually need to determine if number is prime
# def is_prime(n)
#   if n <= 1
#     return false
#   elsif n <= 3
#     return true
#   elsif n%2 == 0 || n%3 == 0
#     return false
#   end
#   i = 5
#   while i*i <= n
#     if n%i == 0 || n%(i+2) == 0
#       return false
#     end
#     i += 6
#   end
#   return true
# end

N = 600851475143
d = 2

# loop is basically a factor tree to find greatest prime factor
# keeps going until the greatest factor is prime
while N > 1
  while N % d == 0
    factor = d
    N /= d
  end
  d += 1
end

puts factor
