import random

frutas = ['banana', 'jabuticaba', 'pitanga', 'mirtilo', 'morango', 'abacaxi', 'cereja']

random.shuffle(frutas)

palavra = frutas[0]

acerto = []
digitadas = []

while True:

    palavra_usuario = ''

    for letra in palavra:
        if letra in acerto:
            palavra_usuario += letra
        else:
            palavra_usuario += '.'

    print(palavra_usuario)

    if palavra_usuario == palavra:
        print('ACERTOU, MEU QUERIDO')
        break

    tentativa = input('Informe uma letra: ').lower().strip()

    if tentativa in digitadas:
        print('Opa, você já digitou essa letra antes')
    else:
        digitadas += tentativa
        if tentativa in palavra:
            acerto += tentativa
        else:
            print('Opa, não foi dessa vez')