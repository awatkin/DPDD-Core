#number guessing game
import random

def main():
    exits = False

    while exited == False:
        go = input("Do you want to play a game? Yes or No: ")
        if go == "no":
            nums = random.randint(1, 100)
            guess = int(input("Guess a number between 1 and 100: "))
            while guess != nums:
                outy =""
                if guess > nums:
                    outy="Wrong, You are too low"
                elif guess < nums:
                    outy="Wrong, You are too high"
                print(outy)
            print("Well done, you got the right number")
        else:
            exits=True

if __name__ == '__main__':
    main()