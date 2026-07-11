import math
import random

# 1. math.floor = gives closest number below value
print(math.floor(1.9))
print(math.trunc(-3.9))

# 2. math.trunc = gives closest number towards zero
print(math.trunc(4.9))
print(math.trunc(-5.9))

# 3. complex number = 2+3j, 4+5j, 7+9i

# 4. octal = numbers with base 8 => 0o20 = 16
print(oct(16))

# 5. Hexa = numbers with base 16 => 0xff = 255
print(hex(255))

# 6. Binary literals = numbers with base 2 => 0b1000 = 8
print(bin(8))

# 7. random() = gives random numbers 
print(random.random())

# 8. random.randint() = gives any random integer
print(random.randint(1,10)) 

# 9. random.choice() = gives random choices from given data
chai_types = ['lemon', 'masala', 'ginger', 'mint', 'oolong']
print(random.choice(chai_types))

# 10. random.shuffle() = shuffles the values
print(random.shuffle(chai_types))

# 11. Sets
a = {1,2,3,4,5}
b = {2,3,4}
print(a&b) # intersection
print(a|b) # union