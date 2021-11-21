# simon says Jvdb
import os
import time
import collections

simon_list = []
user_list = []
score = 0
highScore = 0
play = True
z = True


def high_score(score, highScore):
    while True:
        if score > highScore:
            score = highScore
            return highScore
        else:
            break


def correction(a, b):
    if a == b:
        z = True
        return z
    else:
        z = False
        return z


def random():
    import random
    randomL = chr(random.randint(ord('a'), ord('d')))
    return randomL


def ask():
    print('Press space between every character, press enter when you are done.')
    answer = [str(answer) for answer in (input(
        "Give the right combination: \n")).split()]
    return answer


def restart():
    while True:
        question = str(input('[y,n]  \n'))
        if question in ['y', 'Y']:
            z = True
            clear()
            return z
            False
        elif question in ['n', 'N']:
            z = False
            return z
            False
        else:
            print("\n I didn't understand that \n")


def clear():
    user_list.clear()
    simon_list.clear()
    score == 0


def main():
    while True:
        # voegt een random letter toe aan simon_list
        simon_list.append(random())
        print('Remember wisley after 2 seconds it wil disappear.')
        print("Simon says: \n")
        print(simon_list)
        time.sleep(2)
        os.system('cls')
        user_list = ask().copy()        # kopiëert de ingegeven list van de user
        if correction(simon_list, user_list) == True:   # als correctie juist is
            score = + 1
            print('score= ', score)
            continue  # terug aan het begin van de loop
        if correction(simon_list, user_list) == False:  # als de corretie fout is
            print('You lost')
            print('\tSimon said:', simon_list)
            print('\tYou said: ', user_list)
            break  # stopt de loop
        break


def run():
    while True:
        main()
        print("do you want to play again? ")
        if restart() in [True]:
            print('Have fun')
            main()
        else:
            break


run()
exit()
