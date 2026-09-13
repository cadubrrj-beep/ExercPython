'''
Using the following table, write a program that reads a
code and the amount of an item. After, print the value
to pay. This is a very simple program with the only
intention of practice of selection commands.

1 cachorro quente - 4.00
2 X-salada - 4.50
3 x-bacon - 5.00
4 torrada simples - 2.00
5 refrigerante - 1.50

Input
The input file contains two integer numbers X and Y. X is
the product code and Y is the quantity of this item
according to the above table.

Output
The output must be a message "Total: R$ " followed by the
total value to be paid, with 2 digits after the decimal
point.
'''

id, quantity = input().split()

id = int(id)
quantity = int(quantity)

if id == 1:
    price = 4.00
elif id == 2:
    price = 4.50
elif id == 3:
    price = 5.00
elif id == 4:
    price = 2.00
else:
    price = 1.50

totalPrice = (price * quantity)

print(f"Total: R$ {totalPrice:.2f}")