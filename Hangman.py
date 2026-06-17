import random

words = ("apple", "banana", "grape", "orange", "strawberry",
         "watermelon", "peach", "kiwi", "pineapple", "mango")
hangman = {
    0: ("   ", "   ", "   "),
    1: (" O ", "   ", "   "),
    2: (" O ", " | ", "   "),
    3: (" O ", "/| ", "   "),
    4: (" O ", "/|\\", "   "),
    5: (" O ", "/|\\", "/  "),
    6: (" O ", "/|\\", "/ \\")
}
def display_man(wrong_guesses):
    for i in range(3):
        print(hangman[wrong_guesses][i])
def display_hint(hint):
    print(" ".join(hint))
def display_answer(answer):
    print(" ".join(answer))
def main():
    answer  = random.choice(words)
    hint  = ["_"] * len(answer)
    wrong_guesses = 0
    guessed_letters = set()
    is_running  = True

    while is_running:
        display_man(wrong_guesses)
        display_hint(hint)
        guess = input("Guess a letter: ").lower()
        if len(guess) != 1 or not guess.isalpha():
            print("please enter a valid letter.")
            continue
        if guess in guessed_letters:
            print("you have already guessed that letter.")
            continue
        guessed_letters.add(guess)
        if guess in answer:
            for i in range(len(answer)):
                if answer[i] == guess:
                    hint[i] = guess
        else:
            wrong_guesses += 1
            
        if  "_" not in hint:
            print("Congratulations! You guessed the word!")
            is_running = False
        elif wrong_guesses >= 6:
            print("Game Over! The word was:", answer)
            is_running = False
if __name__ == "__main__":    
    main()
        