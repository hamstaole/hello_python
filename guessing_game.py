# unlimited try
# secret_word = "giraffe"
# guess = input("Enter a guess: ")
# while guess != secret_word:
#     guess = input("Enter a guess: ")
# print("You win. ")

#  limited try , 3 tries
secret_word = "Mai"
guess = ""
guess_count = 0
out_of_guess = False
guess_limit = 3

while guess != secret_word and not(out_of_guess):
    if guess_count < guess_limit:
        guess = input("Enter your guess: ")
        guess_count += 1
    else:
        out_of_guess = True
if out_of_guess:
    print("You lose")
else:
    print("You win")




