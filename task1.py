print("enter 1 number")
a = int(input())
print("enter 2 number")
b = int(input())

def degree(a, b):
    if b == 0:
        return 1
    print(a**b)
    return a * degree(a, b - 1)

print(degree(a, b))