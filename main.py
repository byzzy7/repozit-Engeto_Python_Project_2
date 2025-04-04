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
    print(f"Hi there!\n{symbol}\n"
            f"I've generated a random 4 digit number for you.\n"
            f"Let's play a bulls and cows game.\n{symbol}\n"
            f"Enter a number:\n{symbol}")

def random_number():
    ''' vygenerování náhodného čtyřmístného čísla
    a nesmí začínat 0.
    :return - vraci vygenerované číslo bez duplicitních čísel
    '''
    #nahode čtyřmistné číslo
    generation = random.sample(range(0, 9), 4)
    #když náhodné číslo začína 0,
    # program znovu vygeneruje nové číslo
    while generation[0] == 0:
        generation = random.sample(range(0, 9), 4)
    return ''.join(str(x) for x in generation)

def evaluation_bulls(PC: str, user: str) -> int:
    '''
    Vyhodnoceni, jestli uživatel uhodl jak číslo tak i pozici
    uhodnutého čísla
    :param PC: nahodné číslo od PC
    :param uzivatel: hadané číslo uživatele
    :param sum_bulls = když je shodné číslo a pozice
    pc [1,2,3,4] user [1,2,9,6] = 1,2
    '''
    conversion_PC = list(map(int, str(PC)))
    conversion_user = list(map(int, str(user)))
    sum_bulls = 0 #součet stejných čísel
    # vyhledani stejných čísel na stejné pozici
    for i in range(len(conversion_PC)):
        if conversion_PC[int(i)] == conversion_user[int(i)]:
            sum_bulls += 1
    return sum_bulls

def evaluation_cows(PC: str, user: str) -> int:
    '''
    vyhledaní stejnéjo čísel
    :param PC: nahodné číslo od PC
    :param user: hadané číslo uživatele
    :return: když je shodné číslo, ale ne pozice
    pc [1,2,3,4] user [6,9,1,7] = 1
    '''
    # vyhledaní stejnéjo čísel
    # mezi pc_tip a user, ale nejsou na stejné pozici
    difference_number = set(str(PC)) & set(str(user))
    cows = Counter(difference_number)
    sum_cows = sum(cows.values())
    return sum_cows

def stopwatch(end: float, start: float) -> float:
    '''
    :param end: konec času
    :param start: začátek času
    :return: čas za jak dlouho uhodl/a číslo v sekundách
    '''
    return round(end - start)

def user_duplicita(user: str) -> True:
    '''
    vyhodnoceni, jestli uživatel nezadává stejné čísla
    v jednom tipovaní
    :param user: tipované číslo uživatele
    :return: vypíše čísla, která jsou duplicitní
    '''
    #vyřezené čísel
    table = set()
    #duplikatní čísla
    duplicate_number = []
    for number in str(user):
        if number in table:
            duplicate_number.append(number)
            return True
        else:
            table.add(number)

symbol = "-" * 47 # oddělovací čárka
welcome_user() # uvitání hráče
pc_tip = random_number() # náhodné číslo od PC
number_of_attempts = 0 # počet pokusů
start_time = time() # začátek času

if __name__ == '__main__':
    guessed = True
    while guessed:
        # připočitá bod při každém špatném pokusu
        number_of_attempts += 1
        print(f"TEST: {pc_tip}")
        try:
            user_tip = input(">>> ")
            #oznámí, jestli uživatel zadal duplicitní čísla
            if user_duplicita(user=user_tip):
                print("duplicity number!")
            else:
                print("")
            #jestli uživatel nezadal 0 na začátku čísla
            if int(user_tip[0]) == 0:
                print(f"Number cannot begin with 0!\n{symbol}")
            # jestli dal jenom čtyřmístné číslo
            elif len(user_tip) != 4:
                print(f"Only four-digit numbers!\n{symbol}")
            #jestli uživatel nezadal tipované číslo
            elif int(user_tip) == int(pc_tip):
                print(f"Correct, you've guessed the right number\n"
                        f"in {number_of_attempts} guesses!\n"
                        f"{symbol}\nThat´s amazing!")
                end_time = time() # konec času
                #časomíra
                print(f"Time: {stopwatch(start=start_time, end=end_time)} s")
                guessed = False # ukončení opakování, když user uhodne
            else:
                #vypíše počet bull a cow
                if int(evaluation_bulls(PC=pc_tip, user=user_tip)) == 1:
                    bull = "s"
                else:
                    bull = ""
                # odečtení cow od bull, aby nebylo zdvojené cow.
                rozdil = evaluation_cows(PC=pc_tip, user=user_tip) - evaluation_bulls(PC=pc_tip, user=user_tip)
                if rozdil == 1:
                    cow = "s"
                else:
                    cow = ""
                print(f"{evaluation_bulls(PC=pc_tip, user=user_tip)} bull{bull},"
                      f" {rozdil} cow{cow}")
                print(symbol)
        except ValueError:
            #oznámí uživateli, že nezadal číslo
            print("Only numbers!")