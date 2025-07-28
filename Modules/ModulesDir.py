from random import random, seed, randint, randrange, choice, sample

print("print(random())")
print(random())

print("\nfor i in range(3)")
for i in range(3):
    seed()
    print(random())


print("\nfor i in range(3): seed(10)")
for e in range(3):
    seed(10)
    print(random())

seed()
print("\n for t in range(3): print(randint(0, 9))")
for t in range(3):
    print(randint(0, 9))

seed()
print("\n for t in range(3): print(randrange(0, 12, 3))")
for b in range(3):
    print(randrange(0, 12, 3))

seed()
print("\n+ " + 'students = ["Anne", "Bob", "Max", "John", "Peter"')
students = ["Anne", "Bob", "Max", "John", "Peter"]
print("- " + 'print(sample(students, 2))')
print(sample(students, 2))

print("\n--" + 'print(sample(students, 5))')
print(sample(students, 5))
