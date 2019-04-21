# 1a. generate a list of high school classes, each class is a list of strings,
# each string is a student name. Student names are of your choice.

# 1b. iterate through the list of classes and print out all the classes and
# their student following this format:

# class 1: John, Marry, Jim, Jame, Hoang
# class 2: Duong, Mai, Nam, Ton, Hoang, Thai

# 1c. ask the user for a student name and print out the list of all classes
# that student attends. Example:

# input: Duong => output: class 2
# input: Hoang => output: class 1, class 2


# 1a
list_of_class = [
    ["Mai", "Ton", "Duong"],
    ["Le", "Tao", "Mi"]

]
# 1b
for row in range(len(list_of_class)):
    print("class " + str(row + 1) + ": " + ", ".join(list_of_class[row]))
    # for col in row:
    #      print(col)

# class_1 = ["John", "Jim", "Marry", "Jame", "Hoang"]
# class_2 = ["Duong", "Mai", "Nam", "Ton", "Hoang", "Thai"]
# print("class 1 :" + ", ".join(class_1))
# print("class 2 :" + ", ".join(class_2))
# for x in range(class_1):
#     int(input("Enter a name : "))
