from random import randint

random_number = randint(1, 100)
try_counter = 0

def check_how_close(played_number):
    if played_number > random_number:
        return f"The number is less than {played_number}"
    elif played_number < random_number:
        return f"The number is greater than {played_number}"

print("""
Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.""")
dificulty = int(input("""
1. Easy (10 chances)
2. Medium (5 chances)
3. Hard (3 chances)
Enter your choice: 
>"""))
while dificulty != 1 or dificulty != 2 or dificulty != 3:
    if dificulty == 1:
        play_counter = 10
        print("Great! You have selected the Easy difficulty level.")
        break
    elif dificulty == 2:
        play_counter = 5
        print("Great! You have selected the Medium difficulty level.")
        break
    elif dificulty == 3:
        play_counter= 3
        print("Great! You have selected the Hard difficulty level.")
        break
    else:
        print("Invalid Option")
        dificulty = int(input(">"))
while True:
    if play_counter > 0:
        played_number = int(input(f"Enter your guess: \n>"))
        play_counter -= 1
        try_counter += 1
        if played_number == random_number:
            print(f"Congratulation! You guessed the correct number in {try_counter} attempts")
            break
        else:
            print(f"Incorrect! {check_how_close(played_number)}")
    elif play_counter <= 0:
        print("You Lose! Better luck next time")
        break
