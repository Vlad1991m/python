# TASK 1
# str_num = input('Введите вещественное число: ')
# num = float(str_num)
# int_digits = str(int(num))

# digits_after_comma = len(str_num) - len(int_digits) - 1
# new_num = int(round(num, digits_after_comma) * 10 ** digits_after_comma)

# sum = 0
# while new_num > 0:
#      sum += new_num % 10
#      new_num //= 10

# print(sum)

# TASK 2
# num = int(input('Введите число N: '))
# result = []
# mult = 1
# for i in range(num):
#     result.append(mult * (i + 1))
#     mult *= (i + 1)

# print(result)

# TASK 3
# num = int(input('Введите число k: '))
# elements = []
# for i in range(num):
#     elements.append((1 + 1/(i + 1)) ** (i + 1))

# print(elements)
# sum = 0
# for i in range(num):
#     sum += elements[i]

# print(sum)

# TASK 4
# nums = [1, -5, 8, 5]
# print(nums)

# for i in range(len(nums)):
#     temp = nums[i]
#     from random import randint
#     new_index = randint(0, len(nums)-1)
#     nums[i] = nums[new_index]
#     nums[new_index] = temp

# print(nums)