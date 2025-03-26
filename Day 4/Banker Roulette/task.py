import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

print(random.choice(friends))

random_index = random.randint(0, 4)
print(friends[random_index])
