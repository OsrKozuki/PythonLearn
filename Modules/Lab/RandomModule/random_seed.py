# Add necessary imports here
from random import seed, random

# Write the function random_seed
def random_seed(s):
    seed(s)
    result  = random()
    return result



s = float(input("Enter a value: "))
print(random_seed(s))