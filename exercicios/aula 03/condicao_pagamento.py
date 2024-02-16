print('')
produto = float(1200)
print('O valor do produto é R$ 1200,00')
print('')
vista = produto*0.10
print('à vista no dinheiro/cheque: 10% de desconto -')
cartao = produto*0.05
print('À vista no cartão: 5% de desconto -')
print('Em até 2x no cartão: preço formal -')
juros = produto*0.2
print('3x ou mais no cartão: 20% de juros -')
print('')
escolha = str(input('Qual a sua opção de pagamento? Digite: cheque / vista cartao  /  2x  /  3x : '))
if escolha == 'cheque':
    print('O valor a vista será: ', produto - vista)
elif escolha == 'vista cartao':
    print('O valor a vista no cartão: ', produto - cartao)
elif escolha == '2x':
    print('O Valor a ser pago em 2x é: ', produto)
elif escolha == '3x':
    print('O Valor a ser pago em 3x é: ', produto + juros)
else:
    print('Erro de digitação na opção de pagamento.')

