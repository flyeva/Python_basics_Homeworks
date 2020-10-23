user_name = input("Please enter your name: ")

print("Hello " + user_name + "! This is a unit converter. You can convert kilometers into miles. ")

while True:
    km = int(input("Please enter the number of kilometers: "))


    miles = km * 0.621371
    print(miles)
    choice = input("Enter 'yes' if you want to do another conversion. Enter 'no' if you are finished. ")

    if choice == "no":
        print("Goodbye.")
        break
