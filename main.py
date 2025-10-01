from quest import *

while True:

    questao = int(input('Digite a Questão (1 a 6) ou Digite 0 p/ Sair: '))

    if questao == 0:
        print('SAINDO DO PROGRAMA...')
        break
    elif questao == 1:
        questao_1()
    elif questao == 2:
        questao_2()
    elif questao == 3:
        questao_3()
    elif questao == 4:
        questao_4()
    elif questao == 5:
        questao_5()
    elif questao == 6:
        questao_6()
    else:
        print('OPÇÃO INVÁLIDA')