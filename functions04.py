#!/usr/bin/python3
# -*- coding: utf-8 -*-

from time import sleep

def maior(*num):
    print('-='*30)
    print('Analisando os valores informados...')
    for el in num:
        print(el, end=' ', flush=True)
        sleep(0.5)
    print(f'Foram informados {len(num)} valores ao todo.')
    print(f'O maior valor informado foi {max(num)}.')


maior(3, 8, 22, 15, 18, 96)
maior(4, 16)
maior(8, 20, 41, 66, 78, 2, 4, 6)


