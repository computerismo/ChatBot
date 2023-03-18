############################## Menu 2
from resposta_final import fc1,fc2, fc3, fc4, fc5, fc6, fc7, fc8, fc9, fc10, fc11, fc12

def funcao1():
    while True:
        n = int(input('Menu 2 escolha a opção : \n 1 -  \n 2 - \n 3 - \n' ))
        if 0 < n <= 3:
            break
        print('Opção inválida.')
    match n:
        case 1:
            fc1()
        case 2:
            fc2()
        case 3:
            fc3()

        case _:
            print('Valor inválido.')


def funcao2():
    while True:
        n = int(input('Menu 2 escolha a opção : \n 1 -  \n 2 - \n 3 - \n'))
        if 0 < n <= 3:
            break
        print('Opção inválida.')

    match n:
        case 1:
            fc4()
        case 2:
            fc5()
        case 3:
            fc6()
        case _:
            print('Valor inválido.')

def funcao3():
    while True:
        n = int(input('Menu 2 escolha a opção : \n 1 -  \n 2 - \n 3 - \n'))
        if 0 < n <= 3:
            break
        print('Opção inválida.')

    match n:
        case 1:
            fc7()
        case 2:
            fc8()
        case 3:
            fc9()
        case _:
            print('Valor inválido.')

def funcao4():
    while True:
        n = int(input('Menu 2 escolha a opção : \n 1 -  \n 2 - \n 3 - \n'))
        if 0 < n <= 3:
            break
        print('Opção inválida.')

    match n:
        case 1:
            fc10()
        case 2:
            fc11()
        case 3:
            fc12()
        case _:
            print('Valor inválido.')


######################################## Menu 1

print( 'Ola, seja bem vindo! ')
while True:
    n = int(input('Como posso ajudá-lo ? \n 1 -  \n 2 -  \n 3 -  \n 4 - \n'))
    if 0< n <= 4:
     break
    print('Opção inválida.')
match n:
    case 1:
        funcao1()
    case 2:
        funcao2()
    case 3:
        funcao3()
    case 4 :
        funcao4()
    case _:
        print('Valor inválido.')




