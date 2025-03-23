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
    print(f'''Hi there!\n{znak}\nI've generated a random 4 digit number for you.\nLet's play a bulls and cows game.\n{znak}\nEnter a number:\n{znak}'''
    )

def random_number():
    ''' vygenerování náhodného čtyřmístného čísla
    a nesmí začínat 0
    '''
    return random.randint(1000, 9999)

def numbers_from_pc(cisla_od_PC):
    '''
    převední čísla do seznamu
    od PC
    vstup = 1234
    výstup = 1,2,3,4
    '''
    prevod = list(map(int, str(cisla_od_PC)))
    return prevod

def numbers_from_user(cisla_od_uzivatele):
    '''
    převední čísla do seznamu
    od uzivatele
    vstup = 1234
    výstup = 1,2,3,4
    '''
    prevod = list(map(int, str(cisla_od_uzivatele)))
    return prevod

def statistics(hadane_cislo, pocet_hadani, cas):
    '''
    Shromaždění údajů pro Statistiky
    Počet hádaní, Hádané číslo, Čas
    '''
    return {
        "Hadane cislo": hadane_cislo,
        "Počet hadani": pocet_hadani,
        "Čas": cas
    }

def bulls(PC_nahodne, uzivatel):
    '''
    pokud uživatel uhodne jak číslo, tak jeho umístění
    vstup - PC [1,2,0,0] uzivatel [1,0,8,9]
    vystup - stejné číslo na prvni pozici
    '''
    soucet = 0
    posun = 0
    prevod_od_PC = str(PC_nahodne)
    prevod_od_uzivatele = str(uzivatel)
    for i in range(len(prevod_od_PC)):
        if prevod_od_PC[int(i)] == prevod_od_uzivatele[int(i)]:
            posun += 1
    if soucet == 1:
        return print(f"{soucet} bull")
    else:
        return print(f"{soucet} bulls")

def cows(PC_nahodne, uzivatel):
    '''
    pokud uživatel uhodne pouze číslo, ale ne jeho umístění
    vstup - PC [1,2,0,0] uzivatel [8,9,0,6]
    vystup - soucet 1
    '''
    rozdil = set(PC_nahodne) & set(uzivatel)
    objekt = Counter(rozdil)
    soucet = sum(objekt.values())
    if soucet == 1:
        return print(f"{soucet} cow")
    else:
        return print(f"{soucet} cows")

def program_body(PC_nahodne, uzivatel):
    '''
    :param PC_nahodne: vygenerovane nahodne cisla
    :param uzivatel: vlozene nahodne cisla od uzivatele
    :param gg: odelovaci znak radku
    '''
    guesses = 0
    while PC_nahodne != uzivatel:
        print(nahodne)
        guesses += 1
        try:
            uzivatel = int(input(">>> "))
            if uzivatel != 4:
                print("Jeno čtyřmístné číslo čísla")
            print(f"{cows}, {bulls}\n{znak}")
        except ValueError:
            print("Jenom čiselné zanky")
    print(f"Correct, you've guessed the right number\nin {guesses} guesses!\n{znak}\nThat´s amazing!\nTime:")

start = time() # stopky - zacatek
nahodne = random_number()
znak = "-" * 47
welcome_user()
program_body(PC_nahodne=nahodne, uzivatel=numbers_from_user)
end = time() # stopky - konec
stopky = round(end - start,2) #výsledek jak dlouho hádal uživatel