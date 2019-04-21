# With the break statement
# we can stop the loop even if the while condition is true:
num = 0
while num <= 10:
    print(num)
    if num == 6:
        break
    num += 1

# print("Done with loop")

num = 0
while num <= 10:
    print(num)
    num += 1

print("Loop Stop")
# With the continue statement we can stop the current iteration,
# and continue with the next
run = 0
while run < 10:
    print(run)
    if run == 3:
        continue
    run += 1

print("end")