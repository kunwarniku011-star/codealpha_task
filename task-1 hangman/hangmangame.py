#@code alpha internship task-1 python programming hangman game
import random
print("welcome to the hangmane game ")
words=["python","java","computer","programming","developer"]
word=random.choice(words)
max_attempts=6
wrong_guesses=0
hidden_word ="_" *len(word)
print(hidden_word)
guessed_letters =" "
while wrong_guesses<max_attempts:
 guess = input("enter a letter:\n").lower()
 print("word",hidden_word)
 print("wrong guesses",wrong_guesses ,"/", max_attempts)
 if len(guess) != 1:
    print("please enter only one letter!")
    continue
 if not guess.isalpha():
    print("please enter a letter only !")
    continue
 if guess in guessed_letters:
    print("you already guessed this letter!")
    continue
 guessed_letters += guess
 if guess in word:
    print("correct guess!")
    hidden_word=" "
    for letter in word:
        if letter in guessed_letters:
            hidden_word += letter
        else:
           hidden_word += "_"
    print("hidden_word",hidden_word)
    if "_" not in hidden_word:
        print("you win!")
        break
 else:
    print("wrong guess!")
    wrong_guesses +=1  
    print("wrong_guesses are",wrong_guesses,"/",max_attempts)
if wrong_guesses == max_attempts:
   print("game over")
   print("the word was",word)            

