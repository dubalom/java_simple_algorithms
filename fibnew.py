n = int(input("Кол-во элементов Фибоначчи:"))
num1 = 1
num2 = 1
i = 0
while i < n - 2:
    i = i + 1
    amount = num1 + num2
    num1 = num2
    num2 = amount
print(num2)
