# asking user for input
num = int(input("Enter the integer for the player to guess.\n"))
# declaring variable to hold number of guess
count = 0
guess = int(input("Enter your guess.\n"))
# this loop will run until user enter correct number
while True:
    count = count + 1
    # checking if larger
    if guess > num:
        guess = int(input("Too high - try again:\n"))
        continue
    # checking if smaller
    elif guess < num:
        guess = int(input("Too low - try again:\n"))
        continue
    else:
        break

        # printing result
        # noinspection PyUnreachableCode
        print("You guessed it in", count, 'tries.')
