from random import randint

random_number = randint(1, 100)
play_counter = 0

def check_how_close(played_number):
    if played_number > random_number:
        return f"The number is less than {played_number}"
    elif played_number < random_number:
        return f"The number is greater than {played_number}"
    


while True:
    played_number = int(input(f"Enter your guess: \n>"))
    print(f"{random_number}")
    play_counter += 1
    if played_number == random_number:
        print(f"Congratulation! You guessed the correct number in {play_counter} attempts")
        break
    else:
        print(f"Incorrect! {check_how_close(played_number)}")