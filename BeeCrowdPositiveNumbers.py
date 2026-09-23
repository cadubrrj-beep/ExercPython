#BeecrowdAverage1

'''
Write a program that reads 6 numbers. These numbers will only be positive or negative (disregard null values).
Print the total number of positive numbers.

Input
Six numbers, positive and/or negative.
7, -5, 6, -3.4, 4.6, 12
(4 valores positivos)
'''
positiveCounter = 0

number1 = float(input())
if number1 > 0:
#    slot1 = number1
    positiveCounter += 1

number2 = float(input())
if number2 > 0:
    positiveCounter += 1

number3 = float(input())
if number3 > 0:
    positiveCounter += 1

number4 = float(input())
if number4 > 0:
    positiveCounter += 1

number5 = float(input())
if number5 > 0:
    positiveCounter += 1

number6 = float(input())
if number6 > 0:
    positiveCounter += 1

print(f"{positiveCounter} valores positivos")