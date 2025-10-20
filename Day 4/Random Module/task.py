import random


random_integer = random.randint(1, 10)
print(random_integer)

random_0_to_1 = random.random() * 10
print(random_0_to_1)

random_float = random.uniform(1, 10)
print(random_float)


random_heads_or_tails = random.randint(a=0,b=1)

if random_heads_or_tails == 0:
    print("Heads")
else:
    print("Tails")