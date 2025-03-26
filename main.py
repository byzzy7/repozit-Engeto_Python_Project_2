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
    return print(f"Hi there!\n{symbol}\nI've generated a random 4 digit number for you.\n"
    f"Let's play a bulls and cows game.\n{symbol}\nEnter a number:\n{symbol}")

def random_number():
    ''' vygenerování náhodného čtyřmístného čísla
    a nesmí začínat 0
    '''
    return random.randint(1000, 9999)

def evaluation_bulls(PC, user):
    '''
    Vyhodnoceni, jestli uživatel uhodl jak číslo tak i pozici
    uhodnutého čísla
    :param PC: nahodné číslo od PC
    :param uzivatel: hadané číslo uživatele
    '''
    conversion_PC = list(map(int, str(PC)))
    conversion_user = list(map(int, str(user)))
    sum_bulls = 0
    for i in range(len(conversion_PC)):
        if conversion_PC[int(i)] == conversion_user[int(i)]:
            sum_bulls += 1
    if sum_bulls == 1:
        return print(f"{sum_bulls} bull, ")
    else:
        return print(f"{sum_bulls} bulls, ")

def evaluation_cows(PC, user):
    '''
    Vyhodnocení uhodnutého čísla, ale nezáleží
    na jaké je pozici
    :param PC: nahodné číslo od PC
    :param user: hadané číslo uživatele
    '''
    difference_number = set(PC) & set(user)
    objekt = Counter(difference_number)
    sum_objekt = sum(objekt.values())
    if sum_objekt == 1:
        return print(f"{sum_objekt} cow")
    else:
        return print(f"{sum_objekt} cows")

symbol = "-" * 47
welcome_user()
pc_tip = random_number()
number_of_attempts = 0
stopwatch = 0

guessed = True
while (guessed):
    start = time()
    number_of_attempts += 1
    print(f"TEST: {pc_tip}")
    user_tip = input(">>> ")
    if int(user_tip[0]) == 0:
        print(f"Number must not begin 0!\n{symbol}")
    elif len(user_tip) != 4:
        print(f"Only four-digit numbers!\n{symbol}")
    elif int(user_tip) == pc_tip:
        print(f"{symbol}\n>>> {guessed}\nCorrect, you've guessed the right number\n"
              f"in {pc_tip} guesses!\n{symbol}\nThat´s amazing!\nTime: {stopwatch}")
        guessed = False
    else:
        evaluation_bulls(PC=pc_tip, user=user_tip)
        print(symbol)
    end = time()
    stopwatch += round(end - start, 2)




