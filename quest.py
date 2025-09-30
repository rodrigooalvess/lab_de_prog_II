from functions import *

def questao_1():
    frase = input('Digite uma frase: ').lower()
    palavra = input('Digite uma palavra pra buscar: ').lower()

    busca_palavra = frase.split()

    contador = 0
    
    for i in busca_palavra:
        if i == palavra:
            contador += 1
    
    print(contador)

def questao_2():
    print('Conversor de Temperaturas')
    print('1 - Celsius p/ Fahrenheit')
    print('2 - Fahrenheit p/ Celsius')

    opc = int(input('Digite a opção que deseja: '))

    if opc == 1:
        celsius = float(input('Digite a temperatura que deseja converter: '))
        print(f'Temperatura convertida: {celsius_fahrenheit(celsius):.1f}F')
    elif opc == 2:
        fahrenheit = float(input('Digite a temperatura que deseja converter: '))
        print(f'Temperatura convertida: {fahrenheit_celsius(fahrenheit):.1f}C')
        
    else:
        print('Opção Inválida')

def questao_3():
    usuarios = {
        'admin': '1234',
        'maria': 'abc@2025',
        'joao': 'senha123'
    }

    login = input('Digite o Usuário: ')
    senha = input('Digite a senha: ')

    if usuarios.get(login) == senha:
        print(f'Usuário Logado com Sucesso, Seja Bem-Vindo {login}')
    else:
        print('Usuário ou Senha Incorretos')

def questao_4():
    numero = int(input('Digite um número pra verificar se ele é par ou ímpar: '))
    print(verificar_par_impar(numero))