#! python3

print("how old are you?", end = ' ')
age = input()
print("how tall are you?", end = ' ')
height = input()
print("how much do you weigh?", end = ' ')
weight = input()

print("so, you're %r old, %r tall and %r heavy." % (
    age, height, weight))
