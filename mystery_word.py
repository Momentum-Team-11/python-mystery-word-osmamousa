from importlib.resources import path
from random import random


def play_game():
    pass

import random

print("Here are the rules of the game!!")
print("You have 8 attempts at guessing the word ")
print("You as the player will input one letter at a time")
print("watch as your word comes to life with each guess!!")
print("but remember the number of guesses cannot exceede 8!")

with open("words.txt","r") as file:
    allText = file.read()
    words = list(map(str, allText.split()))

#print(random.choice(words))

print ("Guess the characters")



guesses = ""
attempts = 8

while attempts > 0:
    lost = 0
    for char in words:
        if char in guesses:
            print(char)
        else:
            print("Try again!")
            lost += 1
        return
    if lost == 0:
        print("You got it!")
        print("The mystery word is:", words)
        break


    guess = input("Guess a letter!:")
    guesses += guess
    if guess not in words:
        attempts -= 1
        print("Dang try again!")
        print("Dont worry you have:", attempts, "more attempts")
    if attempts == 0:
        print("Game Over!!")
        print("Better luck next time!")

if __name__ == "__main__":
    play_game()
