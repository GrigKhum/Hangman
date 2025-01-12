import random

from hangman_words import word_list
from hangman_art import logo
from hangman_art import stages
print(logo)

chosen_word = random.choice(word_list)
word_lenght = len(chosen_word)
lives = 6

end_of_game = False

# while not end_of_game:
#     x = input("greq tary ")
#     if x in chosen_word:
#         print(f"{x}-y ka yntrvac bari mej")
#     else:
#         lives-=1
#         print(stages[lives])



display = []
for _ in range(word_lenght):
    display += "_"


while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print(f"You've already guessed {guess}")

    for position in range(word_lenght):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a live")

        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")
    
    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You win")

    print(stages[lives])
    

