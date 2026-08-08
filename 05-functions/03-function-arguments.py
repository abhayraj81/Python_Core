# Arguments in Function

# 1. required argument (single/double/multiple)

def greetings(name):            # name is parameter
    print("Hello",name,"!")

greetings("Abhay")              # Abhay is argument


# 2. default argument

def greetings(name="Abhay"):   # default value
    print("Hello",name , "Bye!")

greetings()                    # no argument passed


# 3. keyword(named) argument
def divide(a,b):
    return a/b

result1 = divide(b=20,a=100)
print(result1)

result2 = divide(20,100)  # positional argument
print(result2)


# 4 Arbitrary Positional Argument 
# Arbitrary Positional Arguments (*args)
# note : stores arguments in form of tuple.
def add2number(*args):
    return sum(args)

op = add2number(1,2,3,4,5)
print(op)


def greeting2(*names):
    for name in names:
        print(f"Hello ! , {name}!")

greeting2("Abhay", "Anshika", "Shobhit","Sharad")

# Arbitrary Keyword Arguments (**kwargs)
# note : stores arguments in form of dictionaries
def print_details(**kwargs):
    print(type(kwargs))
    for key , value in kwargs.items():
        print(f"{key}:{value}")

print_details(name= "Abhay Raj", age=23, city="kanpur")

