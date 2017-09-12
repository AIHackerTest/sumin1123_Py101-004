#! python3

def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print("you have %d cheeses!" % cheese_count)
    print("you have %d boxes of crackers!" % boxes_of_crackers)
    print("man that's enough for a party!")
    print("get a blanket.\n")


print("we can just give the function numbers directly:")
cheese_and_crackers(20, 30)


print("or, we can use variables from our script:")
amout_of_cheese = 10
amout_of_crackers = 50

cheese_and_crackers(amout_of_cheese, amout_of_crackers)


print("we can even do math inside too:")
cheese_and_crackers(10 + 20, 5 + 6)


print("and we can combine the two, variables and math:")
cheese_and_crackers(amout_of_cheese + 100, amout_of_crackers + 1000)
