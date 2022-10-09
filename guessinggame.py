# secreat_word = "zanzibar"
# guess=""


# while guess != secreat_word:
#     guess=input("enter a guess: ")

# print("you are the winner of this game")


# another example with have multiple condition

secreat_word = "Suza"
guess=""
guess_count=0
guess_limit=3
out_of_guesses=False


while guess != secreat_word and not(out_of_guesses):
    if guess_count < guess_limit:
       guess=input("enter a guess: ")
       guess_count +=1
    else:
        out_of_guesses=True
if out_of_guesses:
    print("you are out of guesses, sorry you lose!")
else:
    print("you are the winner of this game")