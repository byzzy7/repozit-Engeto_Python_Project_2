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
    a nesmí začínat 0.
    :return - vraci vygenerované číslo bez duplicitních čísel
    '''
    generation = random.sample(range(1, 9),4)
    return ''.join(str(x) for x in generation)

def evaluation_bulls(PC, user):
    '''
    Vyhodnoceni, jestli uživatel uhodl jak číslo tak i pozici
    uhodnutého čísla
    :param PC: nahodné číslo od PC
    :param uzivatel: hadané číslo uživatele
    :param numbers_without_bulls: vymění číslo za X, když je shodné číslo a pozice
    '''
    conversion_PC = list(map(int, str(PC)))
    conversion_user = list(map(int, str(user)))
    sum_bulls = 0
    for i in range(len(conversion_PC)):
        if conversion_PC[int(i)] == conversion_user[int(i)]:
            sum_bulls += 1
            numbers_without_bulls.append("X")
        else:
            numbers_without_bulls.append(conversion_user[int(i)])
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
    difference_number = set(str(PC)) & set(str(user))
    objekt = Counter(difference_number)
    sum_objekt = sum(objekt.values())
    if sum_objekt == 1:
        return print(f"{sum_objekt} cow")
    else:
        return print(f"{sum_objekt} cows")

def stopwatch(end, start):
    '''
    :param end: konec času
    :param start: začátek času
    :return: čas za jak dlouho uhodl/a číslo
    '''
    return round(end - start, 2)

def user_duplicita(user):
    '''
    vyhodnoceni, jestli uživatel nezadává stejné čísla
    v jednom tipovaní
    :param user: tipované číslo uživatele
    :return: vypíše čísla, která jsou duplicitní
    '''
    table = set()
    duplicate_number = list()
    for number in str(user):
        if number in table:
            duplicate_number.append(number)
            return print(f"You used a duplicate number {duplicate_number}")
        else:
            table.add(number)
    
symbol = "-" * 47 # oddělovací čárka
welcome_user() # uvitání hráče
pc_tip = random_number() # náhodné číslo od PC
number_of_attempts = 0 # počet pokusů
numbers_without_bulls = [] # čísla bez bulls
start = time() # začátek času
end = 0 # konec času

guessed = True
while guessed:
    number_of_attempts += 1
    print(f"TEST: {pc_tip}")
    try:
        user_tip = input(">>> ")
        user_duplicita(user=user_tip)
        if int(user_tip[0]) == 0:
            print(f"Number cannot begin with 0!\n{symbol}")
        elif len(user_tip) != 4:
            print(f"Only four-digit numbers!\n{symbol}")
        elif int(user_tip) == pc_tip:
            print(f"Correct, you've guessed the right number\n"
                 f"in {number_of_attempts} guesses!\n{symbol}\nThat´s amazing!")
            end += time()
            print(f"Time: {stopwatch(start=start, end=end)}")
            guessed = False
        else:
            evaluation_bulls(PC=pc_tip, user=user_tip), evaluation_cows(PC=pc_tip, user=numbers_without_bulls)
            print(symbol)
    except ValueError:
        print("Only numbers!")