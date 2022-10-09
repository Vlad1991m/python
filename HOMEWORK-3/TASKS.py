# TASK-1
# list = []
# count = 5
# for i in range(count):
#     from random import randint
#     list.append(randint(0,9))
# print(list)

# sum = 0
# for i in range(count):
#     if i % 2 != 0:
#         sum += list[i]

# print(sum)

# TASK-2
# list = [2, 4, -5, -8, 6]
# result = []

# for i in range(len(list) // 2):
#     result.append(list[i] * list[len(list) - i - 1])

# if len(list) % 2 != 0:
#     result.append(list[len(list) // 2] ** 2)

# print(result)

# elements = [1.1, 1.2, 3.1, 10.01]

# TASK-3
# elements = [1.5, 8.2, 5.1, 9.03]
# drob = []
# for i in range(len(elements)):
#     drob.append(elements[i] - int(elements[i]))

# min_element = min(drob)
# max_element = max(drob)

# result = round(max_element - min_element, 2)
# print(result)

# TASK-4
# num = int(input('Введите число: '))
# result = str()
# while num != 0:
#     result = str(num % 2) + result
#     num //= 2
# print(result)

# TASK-5
# def fibonacci(n):
#     if n in [1, 2]:
#         return 1
#     elif n < 1:
#         return fibonacci(n + 2) - fibonacci(n + 1)
#     else:
#         return fibonacci(n - 1) + fibonacci(n - 2)

# num = int(input('Введите число: '))
# result = []
# for i in range(-num, num + 1):
#     result.append(fibonacci(i))
# print(result)