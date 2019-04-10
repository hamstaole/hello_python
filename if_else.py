# ask user to enter a number. print out if the number is odd or even
# generate a random number between 1 and 10. ask the user to guess the number and reply if the answer is true or wrong

num: int = int(input("Enter a number : "))
if num % 2 == 0:
    print(str(num) + " is even. ")
else:
    print(str(num) + " is odd. ")

from random import randint


def rand_num():
    return randint(1, 10)


randNum = rand_num()
print(randNum)
num = int(input("Enter a number: "))
if randNum == num:
    print("True")
else:
    print("False")
