"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie

author: Lukáš Bystroň
email: lbystron@gmail.com
"""

from time import time
from collections import Counter
import random

def welcome_user():
    '''uvitání hráče a představení hry'''
    return print(f"Hi there!\n{znak}\nI've generated a random 4 digit number for you.\n"
    f"Let's play a bulls and cows game.\n{znak}\nEnter a number:\n{znak}")

def random_number():
    ''' vygenerování náhodného čtyřmístného čísla
    a nesmí začínat 0
    '''
    return random.randint(1000, 9999)

def vyhodnoceni_bulls(PC, uzivatel):
    '''
    Vyhodnoceni, jestli uživatel uhodl jak číslo tak i pozici
    uhodnutého čísla
    :param PC: nahodné číslo od PC
    :param uzivatel: hadané číslo uživatele
    '''
    prevod_PC = list(map(int, str(PC)))
    prevod_uzi = list(map(int, str(uzivatel)))
    soucet_bulls = 0
    for i in range(len(prevod_PC)):
        if prevod_PC[int(i)] == prevod_uzi[int(i)]:
            soucet_bulls += 1
    if soucet_bulls == 1:
        return print(f"{soucet_bulls} bull, ")
    else:
        return print(f"{soucet_bulls} bulls, ")

def vyhodnoceni_cows(PC, ff):
    '''
    Vyhodnocení uhodnutého čísla, ale nezáleží
    na jaké je pozici
    :param PC: nahodné číslo od PC
    :param ff: hadané číslo uživatele
    '''
    rozdil = set(PC) & set(ff)
    objekt = Counter(rozdil)
    soucet = sum(objekt.values())
    if soucet == 1:
        return print(f"{soucet} cow")
    else:
        return print(f"{soucet} cows")

znak = "-" * 47
welcome_user()
nahod = random_number()
pokus = 0
stopky = 0

uhadl = True
while (uhadl):
    start = time()
    pokus += 1
    print(f"TEST: {nahod}")
    xx = int(input(">>> "))
    if len(str(xx)) == 3:
        print("Číslo nesmí začínat číslem 0!")
    elif len(str(xx)) != 4:
        print("Pouze čtyřciferné čísla!")
    elif nahod == xx:
        print(f"{znak}\n>>> {nahod}\nCorrect, you've guessed the right number\n"
              f"in {pokus} guesses!\n{znak}\nThat´s amazing!\nTime: {stopky}")
        uhadl = False
    else:
        vyhodnoceni_bulls(PC=nahod, uzivatel=xx)
        print(znak)
    end = time()
    stopky += round(end - start, 2)




