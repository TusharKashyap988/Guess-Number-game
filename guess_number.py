import random
"A guess the number game"

n = random.randint(1, 100)
a = -1
guesses = 0
while(a != n):
    guesses += 1
    a = int(input("Guess the number: "))
    if(a > n):
        print("Guess the lower number")
    else:
        print("Guess the higher number")
print(f"You guess the same number in {guesses} guesses")