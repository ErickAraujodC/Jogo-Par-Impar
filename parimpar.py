from random import randint
vitcom = vitusu = 0
print('=-'*19)
print('Vamos jogar par ou ímpar melhor de 5?')
print('=-'*19)

while True:
    num_usu = int(input('Escolha úm número: '))
    num_com = randint(0,10)
    esc_usu = ' '
    while esc_usu not in 'PI':
        esc_usu = input('Você quer par ou ímpar [P/I]: ').upper().strip()[0]
        soma = num_com + num_usu

    if esc_usu in 'P' and soma % 2 == 0:
        vitusu += 1
        print(f'Eu escolhi {num_com} e {num_usu} + {num_com} é {soma}, deu par você ganhou.')
    elif esc_usu in 'P' and soma % 2 != 0:
        vitcom += 1
        print(f'Eu escolhi {num_com} e {num_usu} + {num_com} é {soma}, deu ímpar eu ganhei.')
    elif esc_usu in 'I' and soma % 2 != 0:
        vitusu += 1
        print(f'Eu escolhi {num_com} e {num_usu} + {num_com} é {soma}, deu ímpar você ganhou.')
    elif esc_usu in 'I' and soma % 2 == 0:
        vitcom += 1
        print(f'Eu escolhi {num_com} e {num_usu} + {num_com} é {soma}, deu par eu ganhei.')
    if vitcom > 2 or vitusu > 2:
        break


if vitcom > 2:
    print(f'Resultado final {vitcom} a {vitusu} eu ganhei, mais sorte da próxima.')
else:
    print(f'Resultado final {vitusu} a {vitcom}, parabéns, você ganhou de mim.')