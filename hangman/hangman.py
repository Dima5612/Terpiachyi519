import random

print("HANGMAN")
print("The game will be available soon.")
WORLDS = ["python", "java", "php", "C++"]
word = random.choice(WORLDS)
a = input("Guess the word :\n"">")
while True:
    if a == word:
        print("You survived")
        break
    else:
        print("You lost")
        break
# 2-nd stage completed
