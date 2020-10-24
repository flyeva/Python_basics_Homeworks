
num = int(input("Select a number between 1 and 100. "))

for num in range(1, num+1):
    if num % 3 == 0 and num % 5 ==0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)
