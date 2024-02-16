nome = input('Digite seu nome: ')
sobrenome = input('Digite seu sobrenome: ')
idade = input('Digite sua idade: ')
cidade = input('Digite sua cidade: ')
altura = float(input('Digite sua altura: '))
peso = float(input('Digite seu peso: '))

imc = peso/altura**2
print('Seu IMC é igual a: ', imc)