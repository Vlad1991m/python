import math
from decimal import Decimal
from random import randint, random

# TASK 1
# d = float(input('Input to round: '))
# def digits(num:float):
#     count = 1
#     div = 1
#     while True:
#         if not(num*div == int(num*div)):
#             count += 1
#             div *= 10
#         else: break
#     return count
# print(round(math.pi, digits(d)))

# TASK 2
# num = int(input('Введите натуральное число N: '))

# dividers = []
# for i in range(2, num + 1):
#     while num % i == 0:
#         num //= i
#         dividers.append(i)

# print(dividers)

# TASK 3
# elements = []
# count = 9
# for i in range(count):
#     elements.append(randint(0,9))
# print(elements)   

# unique_and_first_occurence = []
# repeating_occurence = []
# for i in elements:
#     if i not in unique_and_first_occurence:
#         unique_and_first_occurence.append(i)
#     else:
#         repeating_occurence.append(i)

# result = []
# for i in elements:
#     if i not in repeating_occurence:
#         result.append(i)
# print(result)

# TASK 4 & TASK 5 (взято с семинара)

# from random import randint as rI

# def createCoef():
#     coef = {}
#     degree = int(input("Введите максимальную степень: "))
#     for i in range(degree, -1, -1):
#         coef[i] = rI(-20,20)
#     return coef


# def createEquation(coefEquation: dict):
#     equation = ''
#     first = True

#     for i in coefEquation.items():
#         if first:
#             first = False
#             if i[1] < 0:
#                 equation += ' -' + str(abs(i[1])) + 'x^' + str(i[0])
#             elif i[1] > 0:
#                 equation += str(abs(i[1])) + 'x^' + str(i[0])
#         else:
#             if i[1] < 0:
#                 equation += ' - ' + str(abs(i[1])) + 'x^' + str(i[0])
#             elif i[1] > 0:
#                 equation += ' + ' + str(abs(i[1])) + 'x^' + str(i[0])

#     return equation + ' = 0'

# def parseEquation(equation: str):
#     equation = equation.replace(' + ', ' +').replace(' - ', ' -')
#     equation = equation.split()
#     equation = equation[:-2]

#     dictEquation = {}
#     for i in range(len(equation)):
#         equation[i] = equation[i].replace('+', '').split('x^')
#         dictEquation[int(equation[i][1])] = int(equation[i][0])
#     return dictEquation

# equation1 = createEquation(createCoef())
# equation2 = createEquation(createCoef())

# parEq1 = parseEquation(equation1)
# parEq2 = parseEquation(equation2)

# resultEquation ={}
# for i in range(max(len(parEq1), len(parEq2)), -1, -1):
#     first = parEq1.get(i)
#     second = parEq2.get(i)
#     if first != None or second != None:
#         resultEquation[i] = (first if first != None else 0) + (second if second != None else 0)

# def printEquation(equation: str):
#     print(equation.replace(" 1x", "x").replace("x^1", 'x').replace("x^0", ''))

# printEquation(createEquation(parEq1))
# printEquation(createEquation(parEq2))
# printEquation(createEquation(resultEquation))