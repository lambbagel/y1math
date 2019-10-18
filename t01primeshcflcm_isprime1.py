# Is num a prime number? 
# A prime number is an integer n with exactly 2 factors, 1 and n, where n =/= 1.

num = 61
num_factors = 0
for i in range(1,num+1):
  if num % i == 0:
    num_factors += 1
if num_factors == 2:
  print(num, "is prime")
else:
  print(num, "is not prime")
  
