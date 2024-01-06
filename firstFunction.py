# function definition
def say_hi():
    print("Hello User")

def say_hi_again(name):
    print("Hello " + name + ".")

def name_and_age(name, age):
    print("Dam " + name + "! You are " + str(age) + " already?")

# calling the function
say_hi()

# parameters
name = input("What's your name? ")
say_hi_again(name)
say_hi_again("Miguel")

age = input("What's your age? ")
name_and_age(name, str(age))
name_and_age("Steve", 70)
