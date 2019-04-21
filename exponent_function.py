


def raise_to_power(base_num, pow_num):
     result = 1
     for index in range(pow_num):
         result = result * base_num
     return result


print(raise_to_power(3, 4))

from math import exp
print(exp(3))
print(pow(3, 4))
print(pow(3, 2))
print(pow(2, 3))

number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]
print(number_grid[2][1])

# for row in number_grid:
#     print(row)
#     for col in row:
#         print(col)
