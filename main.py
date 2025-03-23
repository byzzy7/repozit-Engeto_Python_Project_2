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
    print(f'''Hi there!\n{znak}\nI've generated a random 4 digit number for you.
    Let's play a bulls and cows game.\n{znak}\nEnter a number:\n{znak}'''
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
    xx = list(map(int, str(cisla_od_PC)))
    return xx

def numbers_from_user(cisla_od_uzivatele):
    '''
    převední čísla do seznamu
    od uzivatele
    vstup = 1234
    výstup = 1,2,3,4
    '''
    xx = list(map(int, str(cisla_od_uzivatele)))
    return xx

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

def bulls(ff, hh):
    '''
    pokud uživatel uhodne jak číslo, tak jeho umístění
    '''
    soucet = 0
    xx = str(ff)
    dd = str(hh)
    if xx[0] == dd[0]:
        soucet +=1
    elif xx[1] == dd[1]:
        soucet += 1
    elif xx[2] == dd[2]:
        soucet += 1
    elif xx[3] == dd[3]:
        soucet += 1
    return soucet

def cows(PC_nahodne, uzivatel):
    '''
    pokud uživatel uhodne pouze číslo, ale ne jeho umístění
    '''
    a = set(PC_nahodne) & set(uzivatel)
    b = Counter(a)
    c = sum(b.values())
    if c == 1:
        print(f"{c} cow")
    else:
        print(f"{c} cows")
    return

def program_body(PC_nahodne, uzivatel):
    '''
    :param PC_nahodne: vygenerovane nahodne cisla
    :param uzivatel: vlozene nahodne cisla od uzivatele
    :param gg: odelovaci znak radku
    '''
    guesses = 0
    while PC_nahodne != uzivatel:
        guesses += 1
        uzivatel = int(input(">>> "))
        print(f"{cows}, {bulls}\n{znak}")
        print(nahodne)
    print(f"Correct, you've guessed the right number\nin {guesses} guesses!\n{znak}\nThat´s amazing!")

start = time() # stopky - zacatek
nahodne = random_number()
znak = "-" * 47
welcome_user()
program_body(PC_nahodne=nahodne, uzivatel=numbers_from_user)
end = time() # stopky - konec
stopky = round(end - start,2) #výsledek jak dlouho hádal uživatel
#statistics(hadane_cislo=nahodne, pocet_hadani=guesses, cas=stopky)