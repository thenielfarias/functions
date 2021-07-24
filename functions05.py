#!/usr/bin/python3
# -*- coding: utf-8 -*-

from random import randint
from time import sleep

def sorteia(lst):
    for el in range(0, 5):
        el = randint(0, 100)
        lst.append(el)
    print('Sorteando 5 valores', end=' ')
    for el in lst:
        print(el, end=' ', flush=True)
        sleep(0.5)
    print('PRONTO!')

def somaPar(lst):
    print(f'Somando os números pares de {lst}, temos', end=' ')
    par = 0
    for el in lst:
        if el % 2 == 0:
            par += el
    print(par)


números = []

sorteia(números)
somaPar(números)


