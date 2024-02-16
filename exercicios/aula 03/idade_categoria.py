idade = int(input('Digite sua idade: '))

if idade <= 4:
    print(f'Idade não corresponde.')
elif idade <= 7:
    print(f'Categoria infantil A ')
elif idade <= 11:
    print(f'Categoria Infantil B ')
elif idade <= 13:
    print(f'Categoria Juvenil A ')
elif idade <= 17:
    print(f'Categoria Juvenil B ')
elif idade >= 18:
    print(f'Categoria Adultos ')
else:
    print('Idade não corresponde.')