import lives
import bank

def main():
    temp = ""
    ans = ["","","","",""]
    word = bank.word()
    print("Word: -----")
    while lives.life > 0:
        count = 0
        guess = input("Guess a letter: ")
        templist = list(temp)
        if guess in word:
            temp += guess
            for i in word:
                count += 1
                if i == guess or i in templist:
                    ans[count-1] = i
                    print(i, end="")
                else:
                    print("-", end="")

            print("\n")

            
            lives.life = lives.get_lives(lives.life)
            print("\nLives Remaining:", lives.life)
        else:
            lives.life = lives.lose_life(lives.life)
            print("\nLives Remaining:", lives.life)

        if ans == list(word) and lives.life > 0:
            print("You win!")
            print("The word was: " + word)
            break

    if lives.life == 0:
        print("You lose!")
        print("The word was: " + word)

    

