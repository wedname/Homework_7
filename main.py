import random

first = tuple(random.randint(0, 10) for x in range(0, 10))
second = tuple(random.randint(0, 10) for y in range(0, 10))
third = tuple(random.randint(0, 10) for z in range(0, 10))
# first = (0, 1, 12, 3, 4, 5, 6, 7, 8, 65)
# second = (0, 1, 38, 3, 4, 5, 6, 7, 8, 9)
# third = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

print(f"{first}\n{second}\n{third}\n")

"""
Задание 1
Есть три кортежа целых чисел необходимо найти
элементы, которые есть во всех кортежах.
"""
result_first_program = set(first) & set(second) & set(third)

print(f"Числа, которые есть во всех кортежах: {result_first_program}")

"""
Задание 2
Есть три кортежа целых чисел необходимо найти
элементы, которые уникальны для каждого списка.
"""
for_first_tuple = set()
for_second_tuple = set()
for_third_tuple = set()

for i in first:
    if i not in second and i not in third:
        for_first_tuple.add(i)
print(f"Уникальные для первого кортежа: {for_first_tuple}")

for j in second:
    if j not in first and j not in third:
        for_second_tuple.add(j)
print(f"Уникальные для второго кортежа: {for_second_tuple}")

for k in third:
    if k not in first and k not in second:
        for_third_tuple.add(k)
print(f"Уникальные для третьего кортежа: {for_third_tuple}")

"""
Задание 3
Есть три кортежа целых чисел необходимо найти эле-
менты, которые есть в каждом из кортежей и находятся
в каждом из кортежей на той же позиции.
"""
result_third_program = set()
for i in range(0, len(first)):
    if first[i] == second[i] and first[i] == third[i]:
        result_third_program.add(first[i])

print(f"Элементы, которые есть в каждом из кортежей и находятся в каждом из кортежей на той же позиции: "
      f"{result_third_program}")
