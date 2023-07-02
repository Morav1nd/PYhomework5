a = int(input())
b = int(input())

def summa(a, b):
    if a == 0:
        return b
    print(a - 1, b + 1)
    return summa(a - 1, b + 1)

print(summa(a, b))