# function that adds two given numbers
def add(term1, term2):
    return term2 + term1


print(add(3, 4))


# say hello to the given name
def greeting(person):
    print("Say hello ")
    print("Say hello " + person + "!")


person = "Duong Kasino"
greeting(person)


# practice
def say_hi(name, age):
    print("Hello" + name + ", you are " + age)


say_hi("Mai", "20")


# can only concatenate str (not "int") to str

def say_hi(name, age):
    print("Hello" + name + ", you are " + str(age))


say_hi("Mai", 20)


def return_func(num):
    return num + 3


print(return_func(3))


def print_func(num):
    print(num + 3)


print_func(3)

# x_r = return_func(3)
#
# x_p = print_func(3)

# print(x_r, x_p)
print(return_func(3) * 2)
print(print_func(3) * 3)
# print() vs. return
# print() doesn't return anything.
# return doesn't print anything.
