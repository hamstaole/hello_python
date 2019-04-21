is_cute = False
is_hamster = False

if is_cute or is_hamster:
    print("Mai is a hamster or cute or both. ")
else:
    print("Mai is neither a hamster nor cute. ")

love_rabbit = False
love_cat = True

if love_cat and love_rabbit:
    print("Mai really loves cat and rabbit. ")
elif love_cat and not(love_rabbit):
    print("Mai loves cat but doesn't love rabbit. ")
elif not(love_cat) and love_rabbit:
    print("Mai loves rabbit but doesn't love cat.  ")
else:
    print("Mai hates cat and rabbit.  ")
# if statement with numbers and input
x = int(input("Enter a an integer: "))
if x < 0:
    print("Negative changed to zero")
elif x == 1:
    print("One")
else:
    print("I don't know")
# if statement and comparison
