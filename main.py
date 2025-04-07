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
    while True:
        generation = random.sample(range(0, 9), 4)
        if generation[0] > 0:
            return ''.join(str(x) for x in generation)
        else:
            continue

def evaluation_bulls(PC: str, user: str) -> int:
    '''
    Vyhodnoceni, jestli uživatel uhodl jak číslo tak i pozici
    uhodnutého čísla
    :param PC: nahodné číslo od PC
    :param uzivatel: hadané číslo uživatele
    :param sum_bulls = když je shodné číslo a pozice
    pc [1,2,3,4] user [1,2,9,6] = "1","2"
    '''
    conversion_PC = list(map(int, str(PC)))
    conversion_user = list(map(int, str(user)))
    sum_bulls = 0 #součet stejných čísel
    # vyhledani stejných čísel na stejné pozici
    for i in range(len(conversion_PC)):
        if conversion_PC[int(i)] == conversion_user[int(i)]:
            sum_bulls += 1
    return sum_bulls

def evaluation_cows(PC: str, user: str, bull: int) -> int:
    '''
    vyhledaní stejnéjo čísel
    :param PC: nahodné číslo od PC
    :param user: hadané číslo uživatele
    pc [1,2,3,4] user [6,9,1,7] = "1"
    '''
    # vyhledaní stejného čísla
    difference_number = set(PC) & set(user)
    cows = Counter(difference_number)
    #odečtení bull. aby se vyřadilo číslo na stejne pozici
    #pc[1,2,3,4] user [1,4,9,9] = "1","4" - "1"
    sum_cows = sum(cows.values()) - bull
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
    :return: True, jestli je číslo duplicitní
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

def historie(pokus: str, cislo: str):
    '''
    shromažďuje data pro overview_of_numbers
    pokus = počet pokusu hadani
    cislo = tipvane cisla
    '''
    overview_of_numbers[pokus] = [cislo]

symbol = "-" * 47 # oddělovací čárka
welcome_user() # uvitání hráče
pc_tip = random_number() # náhodné číslo od PC
number_of_attempts = 0 # počet pokusů
start_time = time() # začátek času
overview_of_numbers = {} #pamět tipovanych cisel

if __name__ == '__main__':
    guessed = True
    while guessed:
        # připočitá bod při každém špatném pokusu
        number_of_attempts += 1
        try:
            user_tip = input(">>> ")
            #data pro historii
            historie(cislo=user_tip, pokus=number_of_attempts)
            #data pro bull
            bull_data = evaluation_bulls(PC=pc_tip, user=user_tip)
            #data pro cow
            cow_data = evaluation_cows(PC=pc_tip, user=user_tip,
                        bull=evaluation_bulls(PC=pc_tip, user=user_tip))
            #oznámí, jestli uživatel zadal duplicitní čísla
            if user_duplicita(user=user_tip):
                print("duplicity number!")
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
                #historie tipovanych cisel
                print(f"Historie: {overview_of_numbers}")
                guessed = False # ukončení opakování, když user uhodne
            else:
                #vypíše počet bull
                if int(bull_data) == 1:
                    bull = "s"
                else:
                    bull = ""
                # vypíše počet cows
                if int(cow_data) == 1:
                    cow = "s"
                else:
                    cow = ""
                print(f"{bull_data} bull{bull}, {cow_data} cow{cow}")
                print(symbol)
        except ValueError:
            #oznámí uživateli, že nezadal číslo
            print("Only numbers!")