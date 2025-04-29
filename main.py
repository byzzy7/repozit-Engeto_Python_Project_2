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
        generation = random.sample(range(9), 4)
        if generation[0] != 0:
            return ''.join(str(x) for x in generation)

def evaluation_bulls(PC: str, user: str) -> int:
    '''
    Vyhodnoceni, jestli uživatel uhodl jak číslo tak i pozici
    uhodnutého čísla
    pc [1,2,3,4] user [1,2,9,6] = [1,2]
    '''
    conversion_PC = list(map(int, str(PC)))
    conversion_user = list(map(int, str(user)))
    sum_bulls = 0 #součet stejných čísel
    # vyhledani stejných čísel na stejné pozici
    if len(conversion_PC) == len(conversion_user):
        for i in range(len(conversion_PC)):
            if conversion_PC[int(i)] == conversion_user[int(i)]:
                sum_bulls += 1
    return sum_bulls

def evaluation_cows(PC: str, user: str, bull: int) -> int:
    '''
    vyhledaní stejnéjo čísel
    pc [1,2,3,4] user [6,9,1,7] = [1]
    '''
    # vyhledaní stejného čísla
    difference_number = set(str(PC)) & set(list(user))
    sum_cows = sum(Counter(difference_number).values())
    result = int(sum_cows) - int(bull)
    return result

def stopwatch(end: float, start: float) -> float:
    '''
    Výpočet času za jak dlouho uhodl/a číslo v sekundách
    '''
    return round(end - start)

def user_duplicita(user: str) -> True:
    '''
    kontrola duplicitních čísel
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

def history(attempt: str, number: str):
    '''
    shromažďuje data pro overview_of_numbers
    attempt = počet pokusu
    number = tipvaná čísla
    '''
    overview_of_numbers[attempt] = [number]

def singular_or_plural(bull_data: int, cow_data: int):
    # řeší množné číslo pro bull
    if bull_data == 1:
        bull = "s"
    else:
        bull = ""
    # řeší množné číslo pro cow
    if cow_data == 1:
        cow = "s"
    else:
        cow = ""
    return f"{bull_data} bull{bull}, {cow_data} cow{cow}"

def check_zero(user_tip: str):
    #kontrola - číslo nezačíná nulou
    if int(user_tip[0]) == 0:
        return True

def only_four_digits(user_tip: str):
    # kontrola - čtyřmístné číslo
    if len(user_tip) != 4:
        return True

def number_is_missing(user_tip: str):
    #prazdné pole
    if user_tip == "":
        return True

def list_of_guessed_numbers(user_tip: str, pc_tip: str):
    # kontrola - uživatel nezadal tipované číslo
    if int(user_tip) == int(pc_tip):
        print(f"Correct, you've guessed the right number\n"
              f"in {number_of_attempts} guesses!\n"
              f"{symbol}\nThat´s amazing!")
        end_time = time()  # konec času
        # Čas za jak dlouho se uhadlo číslo
        print(f"Time: {stopwatch(start=start_time,
                                 end=end_time)} s")
        # Historie tipovaných čísel
        print(f"History: {overview_of_numbers}")
        exit()

def main(number_of_attempts: int, pc_tip: str):
    while True:
        # připočitá bod při každém špatném pokusu
        number_of_attempts += 1
        try:
            # Tip od uživatele
            user_tip = input(">>> ")
            if number_is_missing(user_tip=user_tip):
                print(f"Number cannot be empty!")
            elif check_zero(user_tip=user_tip):
                print(f"Number cannot begin with 0!")
            elif only_four_digits(user_tip=user_tip):
                print(f"Only four-digit numbers!")
            elif user_duplicita(user=user_tip):
                print(f"Duplicity number!")
            else:
                list_of_guessed_numbers(user_tip=user_tip, pc_tip=pc_tip)
            # byhodnocení tipu
            bull_data = evaluation_bulls(PC=pc_tip, user=user_tip)
            cow_dala = evaluation_cows(PC=pc_tip, user=user_tip,
                                       bull=bull_data)
            # historie tipovaných čísel
            history(attempt=number_of_attempts, number=user_tip)
            print(f"{singular_or_plural(bull_data, cow_dala)}\n{symbol}")
        except ValueError:
            print(f"Only numbers!\n{symbol}")


symbol = "-" * 47 # oddělovací čárka
pc_tip = random_number() # náhodné číslo od PC
number_of_attempts = 0 # počet pokusů
start_time = time() # začátek času
overview_of_numbers = {} #pamět tipovanych cisel

if __name__ == '__main__':
    welcome_user() # uvitání hráče
    main(number_of_attempts, pc_tip) # spuštění hry

