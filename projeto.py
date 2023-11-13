import os
total = 0
cont = 0
reg = 0
bomOtimo = 0
while(True):
    opniao = input('Nota[3] Otimo\nNota[2] Bom\nNota[1] Regular\nDigite uma das opções: ')
    idade = int(input('Digite sua idade: '))
    total = total + idade
    cont = cont + 1
    if opniao == '1':
        if idade >= 25 and idade <= 30:
            reg = reg + 1

    elif opniao == '2' or opniao == '3':
        bomOtimo = bomOtimo + 1
    else:
        print('digite uma opçao correta')

    resp = input('Digite 0 para encerrar ou 1 para continuar: ')
    if resp =='0':
        break
    os.system('cls')
media = total/cont
percentual = (bomOtimo/cont) * 100
print(f'a media é : {media:.2f}')
print(f'pessoas entre 25 e 30 anos que responderam regular: {reg:.1f}')
print(f'o percentual de pessoas que votaram em bom ou otimo: {percentual:.1f}')
