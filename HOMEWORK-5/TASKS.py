from random import randint, random

# TASK 1
# my_text = 'Напишите напиабв програбвмму программу, удаляющую из этого абв текста все вабвс слова, содерабващие содержащие "абв"'
# def del_some_words(my_text):
#     my_text = list(filter(lambda x: 'абв' not in x, my_text.split()))
#     return " ".join(my_text)
# my_text = del_some_words(my_text)
# print(my_text)


# TASK 2
# Игра против бота
# def Users_steps():
#     global count
#     step = int(input('Сколько конфет Вы забираете? '))
#     count -= step
#     if count <= 0:
#         print("Вы выиграли!")
#     else:
#         print('Осталось {} конфет'.format(count))
        

# def Bots_steps():
#     global count, max_step
#     if count % (max_step + 1) !=0:
#         step = count % (max_step + 1)
#     else:
#         step = randint(1, 28)
#     print('Бот забрал {} конфет'.format(step))
#     count -= step
#     if count <= 0:
#         print('Вы проиграли!')
#     else:
#         print('Осталось {} конфет'.format(count))

# count = 150
# max_step = 28

# input('Чтобы бросить жребий, нажмите Enter: ')
# lot = randint(0,1)

# if lot:
#     print('Первым ходите Вы.')
# else:
#     print('Первым ходит бот.')

# while count > 0:
#     if lot:
#         Users_steps()
#         if count > 0:
#             Bots_steps()
#     else:
#         Bots_steps()
#         if count > 0:
#             Users_steps()

# Игра против человека

# def Users_steps(user):
#     global count
#     print('Ходит {}: '.format(user))
#     step = int(input('Сколько конфет Вы забираете? '))
#     count -= step
#     if count <= 0:
#         print("Выиграл {}!".format(user))
#     else:
#         print('Осталось {} конфет'.format(count))

# count = 100
# max_step = 28
# user1 = 'первый игрок'
# user2 = 'второй игрок'

# while count > 0:
#     Users_steps(user1)
#     if count > 0:
#         Users_steps(user2)


# TASK 3
# def Show_Matrix(m):
#     print()
#     for i in range(len(m)):
#         for j in range(len(m[i])):
#             print(m[i][j], end=' ')
#         print()
#     print()

# def Steps(sign, player):
#     global matrix
#     print('Ход игрока за {}.'.format(sign))
#     step_row = int(input('Введите номер строки: '))
#     step_column = int(input('Введите номер столбца: '))
#     while matrix[step_row][step_column] != '*':
#         print('Ошибка! Эта позиция уже занята.')
#         step_row = int(input('Введите номер строки: '))
#         step_column = int(input('Введите номер столбца: '))
        
#     matrix[step_row][step_column] = sign

#     if step_row == 0:
#         player.add(str(step_column))
#     elif step_row == 1:
#         player.add(str(step_column + len(matrix)))
#     else:
#         player.add(str(step_column + 2*len(matrix)))
    
#     Show_Matrix(matrix)

# def Checking(player):
#     global winning_combinations
#     for i in winning_combinations:
#         if i.issubset(player):
#             return True
#     return False

# matrix = [['*', '*', '*'], ['*', '*', '*'], ['*', '*', '*']]
# Show_Matrix(matrix)

# winning_combinations = [{'0', '1', '2'}, {'3', '4', '5'}, {'6', '7', '8'}, {'0', '3', '6'}, {'1', '4', '7'}, {'2', '5', '8'}, {'0', '4', '8'}, {'2', '4', '6'}]

# sign_x = 'X'
# sign_0 = '0'
# player_X = set()
# player_0 = set()

# for i in range(5):
#     Steps(sign_x, player_X)
#     if Checking(player_X):
#         print('Победили крестики!')
#         break
#     else:
#         if i != 4:
#             Steps(sign_0, player_0)
#             if Checking(player_0):
#                 print('Победили нолики!')
#                 break
#         else:
#             print('Ничья!')

# TASK 4
# def coding(txt):
#     count = 1
#     res = ''
#     for i in range(len(txt)-1):
#         if txt[i] == txt[i+1]:
#             count += 1
#         else:
#             res = res + str(count) + txt[i]
#             count = 1
#     if count > 1 or (txt[len(txt)-2] != txt[-1]):
#         res = res + str(count) + txt[-1]
#     return res

# def decoding(txt):
#     number = ''
#     res = ''
#     for i in range(len(txt)):
#         if not txt[i].isalpha():
#             number += txt[i]
#         else:
#             res = res + txt[i] * int(number)
#             number = ''
#     return res


# s = input("Введите текст для кодировки: ")
# print(f"Текст после кодировки: {coding(s)}")
# print(f"Текст после дешифровки: {decoding(coding(s))}")