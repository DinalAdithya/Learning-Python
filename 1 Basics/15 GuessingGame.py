secret_word = "kyoko"
chance = 2
guess_word  = input("Enter the Secret word : ")

while secret_word != guess_word and chance != 0 :
    print("worng guess", chance,"more chances left")
    chance -= 1
    guess_word = input("Enter Secret word again :")


if guess_word == secret_word:
    print("\n""YOU WIN!")
else:
    print("\n""YOU LOSE!")
