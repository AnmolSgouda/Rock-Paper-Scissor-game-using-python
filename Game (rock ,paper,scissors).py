from pickle import FALSE


def game(comp,your):
    
    print(f"Your choise was {your}")
    print(f"Computer's choise was {comp}")
    if comp==your:

        return a
    elif comp == 'Scissors':
        if your=='rock':
            return True
        else:
            return FALSE
    elif comp == 'Rock':
        if your=='paper':
            return True
        else:
            return False
    elif comp == 'paper':
        if your=='Scissors':
            return True
        else:
            return FALSE


import random
a=random.randint(1,3)
if a==1 :
    comp= 'Rock'
elif a==2 :
    comp='Paper'
elif a==3 :
    comp= 'Scissors'
print("Computer has taken it's choice ")
b=input("Enter your input of rock(r) paper(p) scissors(s)  :")

if b=='r' :
    your= 'Rock'
elif b=='p':
    your= 'Paper'
elif b=='s':
    your= 'Scissors'

c=game(comp,your)

if (c==a):
    print("The game is draw")
elif c:
    print('So your win')
else :
    print('So you loose')
