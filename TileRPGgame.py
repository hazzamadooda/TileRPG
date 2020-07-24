import random
import os
import time
words = ['hi','bye','hahahah','catch','romantic','roof','wander','brainstorm','wage']
words_with_muti_player = ['']

death_1 = '\n\n\n\n\n__________'
death_2 = '     |\n     |\n     |\n     |\n____________'
death_3 = '   __________    \n     |\n     |\n     |\n     |\n____________'
death_4 = '   __________    \n     | /\n     |/\n     |\n     |\n____________'
death_5 = '   __________    \n     | /   |\n     |/    |\n     |\n     |\n____________'
death_6 = '   __________    \n     | /   |\n     |/    O\n     |    \n     |     \n____________'
death_7 = '   __________    \n     | /   |\n     |/    O\n     |    \/ \n     |     \n____________'
death_8 = '   __________    \n     | /   |\n     |/    O \n     |    \/ \n     |    /\ \n____________'




def Hangman_start():
    os.system('clear')
    word = random.choice(words)
    correct_guesses = ''
    incorrect_guesses = ''
    turns = 10



    while turns > 0:
        failed = 0
        for char in word:
            if char in correct_guesses:
                print(char)

            else:
                print("-")
                failed += 1

        if failed == 0:
            print("You Win")
            print("The word is: ", word)
            break





        guess = input("guess a character:")
        words_in_guess = len(guess)
        correct_guesses += guess

        if guess not in "abcdefghijklmnopqrstuvwxyz":
            print("not in the alphabet, try again: ")
        elif guess in incorrect_guesses:
            os.system('clear')
            print(incorrect_guesses)
            print("You have allready guessed that, try again: ")
        elif words_in_guess >= 2:
            os.system('clear')
            print("Please only enter one letter at a time: ")
        else:

            if guess not in word:
                turns -= 1
                incorrect_guesses += guess + ","
                os.system('clear')
                print("Wrong, here are your incorrect guesses: " + incorrect_guesses)

                print("You have", + turns, 'more guesses')
                if turns == 1:
                    print(death_8)
                elif turns == 2:
                    print(death_7)
                elif turns == 3:
                    print(death_6)
                elif turns == 4:
                    print(death_5)
                elif turns == 5:
                    print(death_4)
                elif turns == 6:
                    print(death_3)
                elif turns == 7:
                    print(death_2)
                elif turns == 8:
                    print(death_1)
                elif turns == 0:
                    print("You lost")



Hangman_start()
