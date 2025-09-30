from functions import *

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