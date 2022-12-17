import game
import os



os.system('cls' if os.name == 'nt' else 'clear')



print("Welcome to Hangman!")
print("")

#print the rules of the game
print("The rules of the game are:")
print("You have 5 lives to guess the word.")
print("You can guess a letter or a word.")
print("If you guess a letter that is not in the word, you lose a life.")
print("If you guess a letter that is in the word, you gain a life.")
print("")
print("===========================================================================================")
print("")
print("Press enter to continue...")

input()

game.main()
