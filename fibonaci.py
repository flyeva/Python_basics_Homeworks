n = int(input("Enter a number "))

x = 0
y = 1
if n == 1:
    print(x)
elif n == 2:
    print(y)
else:
    print(x)
    print(y)

while y < (n - y):
    z = x + y
    x = y
    y = z
    print(z)



