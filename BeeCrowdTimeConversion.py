'''
Read an integer value, which is the duration in seconds of a certain
event in a factory, and inform it expressed in hours:minutes:seconds.

Input
The input file contains an integer N.

Output
Print the read time in the input file (seconds) converted in
hours:minutes:seconds like the following example.
'''

N = int(input())

hour = N // 3600 # Ao usar "//" a divisão retorna somente a divisão perfeita, sem sobras. Ignorando o resto.
rest = N % 3600 # O cálculo do resto é importante para definir os minutos e segundos.

minute = rest // 60 # O resto é dividindo considerando apenas a divisão perfeita.
second = rest % 60 # O resto do resto dividido por 60

print(f"{hour}:{minute}:{second}")

