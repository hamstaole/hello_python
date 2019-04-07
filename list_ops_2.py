friends = [1, 2, 3, 4, 5, 6]
friends.append([8,9,10,"mi"])
friends.append([10,8,9])
print("  Updated list : " + str(friends))
alpha = ["a", "b", "c", "d", "e"]
gr_alpha = ["alpha", "beta", "gamma", "delta", "epsilon"]
alpha.extend(gr_alpha)
print(" Extended List : " + str(alpha))

name = ["L", "e", "T", "a", "o", "M", "a", "i"]
print("My new list ist:" + str(name))
name.extend(["letaomai"])
print("Extended List 2: " + str(name))
name.count("a")
print("Count for a    : " + str(name.count("a")))
#print("Count for a : " + str(name)) is equal to print(name)
print("Count for i    : " + str(name.count("i")))
alphabet = ["N", "g", "u", "y", "e", "n", "H", "o", "a", "n", "g", "D", "u", "o", "n", "g"]
print("  Another list : " + str(alphabet))
print("Count for n    : " + str(alphabet.count("n")))
#just practice
print("Count for g    : " + str(alphabet.count("g")))
print(len(alphabet))
alphabet.insert(16, "kasino")
print("Inserted list  : " + str(alphabet))
#can I insert a list ?
alphabet.insert(16, [31, "kasino"])
print("Inserted List 2: " + str(alphabet))
#yes
alphabet.insert(0, "abc")
print("Last inserted list : " + str(alphabet))
#python wil put all the command above into the final list
print("List with pop() method : " + str(alphabet.pop()))
print("List with pop(15) method : " + str(alphabet.pop(15)))




