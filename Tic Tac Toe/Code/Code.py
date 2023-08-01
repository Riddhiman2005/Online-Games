import random

tictac = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Function to print the box
def ticte(tictac=[]):
    print('______')
    for i in range(0, 9, 3):
        print(f'|{tictac[i]}{tictac[i+1]}{tictac[i+2]}|')
    print('______')


# Function to determine if someone won
def winner(tictac=[]):
    win_patterns = [
        [0, 1, 2], [0, 3, 6], [0, 4, 8],
        [3, 4, 5], [6, 7, 8], [1, 4, 7],
        [2, 5, 8], [2, 4, 6]
    ]
    for pattern in win_patterns:
        if tictac[pattern[0]] == tictac[pattern[1]] == tictac[pattern[2]] == 'X':
            return 2
        elif tictac[pattern[0]] == tictac[pattern[1]] == tictac[pattern[2]] == 'O':
            return 1
    return 0


# Multiplayer
def play(tictac=[]):
    while True:
        ticte(tictac)
        print('Player 1s turn')
        a = input()
        a = int(a)
        tictac[a - 1] = 'X'
        ticte(tictac)
        if winner(tictac) == 2:
            print('Player 1 wins \n')
            break
        if all([x != i for i, x in enumerate(tictac, 1)]):
            print('draw')
            break
        print('Player 2s turn')
        a = input()
        a = int(a)
        tictac[a - 1] = 'O'
        if winner(tictac) == 1:
            print('Player 2 wins \n')
            break
        if all([x != i for i, x in enumerate(tictac, 1)]):
            print('draw')
            break


# Single player easy mode
def play2(tictac=[]):
    tictac2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    while True:
        ticte(tictac)
        print('Player 1s turn')
        a = input()
        a = int(a)
        tictac[a - 1] = 'X'
        ticte(tictac)
        tictac2.remove(a)
        if winner(tictac) == 2:
            print('Player 1 wins \n')
            break
        if all([x != i for i, x in enumerate(tictac, 1)]):
            print('draw')
            break
        x = random.randint(0, len(tictac2) - 1)
        tictac[tictac2[x] - 1] = 'O'
        tictac2[x] = 'O'
        tictac2.remove('O')
        print("Computer playing")
        if winner(tictac) == 1:
            ticte(tictac)
            print('Computer wins \n')
            break
        if all([x != i for i, x in enumerate(tictac, 1)]):
            print('draw')
            break


# Single player medium mode
def play3(tictac=[]):
    tictac2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    while True:
        ticte(tictac)
        print('Player 1s turn')
        a = input()
        a = int(a)
        tictac[a - 1] = 'X'
        ticte(tictac)
        tictac2.remove(a)
        if winner(tictac) == 2:
            print('Player 1 wins \n')
            break
        if all([x != i for i, x in enumerate(tictac, 1)]):
            print('draw')
            break
        for y in range(0, len(tictac2) - 1):
            z = 0
            m = tictac[tictac2[y] - 1]
            tictac[tictac2[y] - 1] = 'O'
            if winner(tictac) == 1:
                x = y
                tictac[tictac2[y] - 1] = m
                z = 1
                break
            tictac[tictac2[y] - 1] = 'X'
            if winner(tictac) == 2:
                x = y
                tictac[tictac2[y] - 1] = m
                z = 1
                break
            tictac[tictac2[y] - 1] = m

        if z == 0:
            x = random.randint(0, len(tictac2) - 1)

        tictac[tictac2[x] - 1] = 'O'
        tictac2[x] = 'O'
        tictac2.remove('O')
        print("Computer playing")
        if winner(tictac) == 1:
            ticte(tictac)
            print('Computer wins \n')
            break
        if all([x != i for i, x in enumerate(tictac, 1)]):
            print('draw')
            break


# Single player hard mode
def play4(tictac=[]):
    x = 0
    tictac[6] = 'O'
    print("Computer playing first")
    while True:
        ticte(tictac)
        print('Player 1s turn')
        a = input()
        a = int(a)
        tictac[a - 1] = 'X'
        ticte(tictac)

        if a == 2 or a == 4 or a == 6:
            tictac[8] = 'O'
            print("Computer playing")
            ticte(tictac)
            print('Player 1s turn')
            a = input()
            a = int(a)
            tictac[a - 1] = 'X'
            ticte(tictac)
            if a != 8:
                tictac[7] = 'O'
                print("Computer playing")
                ticte(tictac)
                print("Computer wins")
                break
            if a == 8:
                tictac[4] = 'O'
                print("Computer playing")
                ticte(tictac)
                print('Player 1s turn')
                a = input()
                a = int(a)
                tictac[a - 1] = 'X'
                ticte(tictac)
                if a == 1:
                    tictac[2] = 'O'
                    print("Computer playing")
                    ticte(tictac)
                    print("Computer wins")
                    break
                if a != 1:
                    tictac[0] = 'O'
                    print("Computer playing")
                    ticte(tictac)
                    print("Computer wins")
                    break

        elif a == 1 or a == 3:
            tictac[8] = 'O'
            b = a
            print("Computer playing")
            ticte(tictac)
            print('Player 1s turn')
            a = input()
            a = int(a)
            tictac[a - 1] = 'X'
            ticte(tictac)
            if a != 8:
                tictac[7] = 'O'
                print("Computer playing")
                ticte(tictac)
                print("Computer wins")
                break
            if a == 8:
                tictac[3 - b] = 'O'
                print("Computer playing")
                ticte(tictac)
                print('Player 1s turn')
                a = input()
                a = int(a)
                tictac[a - 1] = 'X'
                ticte(tictac)
                if a != 5:
                    tictac[4] = 'O'
                    print("Computer playing")
                    ticte(tictac)
                    print("Computer wins")
                    break
                if a == 5:
                    tictac[6 - b] = 'O'
                    print("Computer playing")
                    ticte(tictac)
                    print("Computer wins")
                    break

        elif a == 8:
            tictac[0] = 'O'
            print("Computer playing")
            ticte(tictac)
            print('Player 1s turn')
            a = input()
            a = int(a)
            tictac[a - 1] = 'X'
            ticte(tictac)
            if a != 4:
                tictac[3] = 'O'
                print("Computer playing")
                ticte(tictac)
                print("Computer wins")
                break
            if a == 4:
                tictac[2] = 'O'
                print("Computer playing")
                ticte(tictac)
                print('Player 1s turn')
                a = input()
                a = int(a)
                tictac[a - 1] = 'X'
                ticte(tictac)
                if a == 2:
                    tictac[4] = 'O'
                    print("Computer playing")
                    ticte(tictac)
                    print("Computer wins")
                    break
                if a != 2:
                    tictac[1] = 'O'
                    print("Computer playing")
                    ticte(tictac)
                    print("Computer wins")
                    break

        elif a == 9:
            tictac[0] = 'O'
            print("Computer playing")
            ticte(tictac)
            print('Player 1s turn')
            a = input()
            a = int(a)
            tictac[a - 1] = 'X'
            ticte(tictac)
            if a != 4:
                tictac[3] = 'O'
                print("Computer playing")
                ticte(tictac)
                print("Computer wins")
                break
            if a == 4:
                tictac[2] = 'O'
                print("Computer playing")
                ticte(tictac)
                print('Player 1s turn')
                a = input()
                a = int(a)
                tictac[a - 1] = 'X'
                ticte(tictac)
                if a != 5:
                    tictac[4] = 'O'
                    print("Computer playing")
                    ticte(tictac)
                    print("Computer wins")
                    break
                if a == 5:
                    tictac[1] = 'O'
                    print("Computer playing")
                    ticte(tictac)
                    print("Computer wins")
                    break

        else:
            tictac[2] = 'O'
            print("Computer playing")
            ticte(tictac)
            print('Player 1s turn')
            a = input()
            a = int(a)
            tictac[a - 1] = 'X'
            ticte(tictac)
            if a == 2 or a == 4 or a == 6 or a == 8:
                tictac[9 - a] = 'O'
                print("Computer playing")
                ticte(tictac)
                print('Player 1s turn')
                a = input()
                a = int(a)
                tictac[a - 1] = 'X'
                ticte(tictac)
                if True:
                    tictac[9 - a] = 'O'
                    print("Computer playing")
                    ticte(tictac)
                    if winner(tictac) == 1:
                        print('Computer wins')
                        break
                    if all([x != i for i, x in enumerate(tictac, 1)]):
                        print('draw')
                        break
                    print('Player 1s turn')
                    a = input()
                    a = int(a)
                    tictac[a - 1] = 'X'
                    ticte(tictac)
                    if True:
                        tictac[9 - a] = 'O'
                        print("Computer playing")
                        ticte(tictac)
                        if winner(tictac) == 1:
                            print('Computer wins')
                            break
                        if all([x != i for i, x in enumerate(tictac, 1)]):
                            print('draw')
                            break
            if a == 1 or a == 9:
                b = a
                tictac[9 - a] = 'O'
                print("Computer playing")
                ticte(tictac)
                print('Player 1s turn')
                a = input()
                a = int(a)
                tictac[a - 1] = 'X'
                ticte(tictac)
                if b == 9 and a != 2:
                    tictac[1] = 'O'
                    print("Computer playing")
                    ticte(tictac)
                    print("Computer wins")
                    break
                if b == 9 and a == 2:
                    tictac[3] = 'O'
                    print("Computer playing")
                    ticte(tictac)
                    print("Computer wins")
                    break
                if b == 1 and a != 8:
                    tictac[6] = 'O'
                    print("Computer playing")
                    ticte(tictac)
                    print("Computer wins")
                    break
                if b == 1 and a == 8:
                    tictac[5] = 'O'
                    print("Computer playing")
                    ticte(tictac)
                    print("Computer wins")
                    break


def playit():
    while True:
        print('''\nTIC-TAC-TOE
If you want to play multiplayer, press 1
If you want to play single player:
    a) Easy mode, press 2,
    b) Medium mode, press 3,
    c) Hard mode, press 4,
and anything else to exit:''')
        g = input()

        if g == '1':
            play(tictac)
        elif g == '2':
            play2(tictac)
        elif g == '3':
            play3(tictac)
        elif g == '4':
            play4(tictac)
        else:
            break


if __name__ == "__main__":
    playit()
