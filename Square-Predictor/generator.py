import random
numbers = random.randint(1000,2000)
print(numbers)
for i in range(numbers):
    sq = random.randint(1,100)
    print(sq, end=" ")
    print(sq*sq)
