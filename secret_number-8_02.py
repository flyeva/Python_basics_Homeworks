secret = 55

guess = input("Guess the srcret number! ")

if guess == "55":
    print("Congratulations, you guessed the secret number!")
elif "0" <= guess <= "50":
    print("Try higher. ")
elif guess > "50":
    print("Try lower. ")
else:
    print("The number is positive.")