from quest import *

questao = int(input('Digite a Questão (1 a 6): '))

if questao == 1:
    questao_1()
if questao == 2:
    questao_2()
if questao == 3:
    questao_3()
if questao == 4:
    questao_4()
if questao == 5:
    questao_5()
if questao == 6:
    questao_6()
else:
    print('OPÇÃO INVÁLIDA')