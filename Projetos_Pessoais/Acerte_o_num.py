from random import randint
r = str
n = int(randint(1, 1000))

while r != 'N':
    n1 = float(input('Digite um número: '))
    while n1 != n:
        if n1 > n:
            print('\033[1;31mEste número é muito alto, tente denovo!')
            n1 = float(input('Tente outra vez: '))
            print('=' * 20)
        elif n1 < n:
            print('\033[1;31mEste número é muito baixo, tente denovo!')
            n1 = float(input('Tente outra vez: '))
            print('=' * 20)
        elif n1 == n:
            print('\033[1;34mPARABÉNS! VOCÊ ACERTOU!')
    r = str(input('Quer continuar?[S/N] ')).strip().upper()
