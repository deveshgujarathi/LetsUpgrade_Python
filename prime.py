num1 = 00
num2 = 200
for n in range(num1, num2 + 1):
    if n > 1:
        for i in range(2, n):
            if (n % i) == 0:
                break
        else:
            print(n)