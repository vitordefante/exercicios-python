# programa que lê nascimento do atleta e mostre sua categoria
nascimento = int(input('Insira aqui a idade do atleta: '))
if nascimento <= 9:
    print('Categoria MIRIM')
elif nascimento > 9 and nascimento <= 14:
    print('Categoria INFANTIL')
elif nascimento > 14 and nascimento <=19:
    print('Categoria JUNIOR')
elif nascimento > 19 and nascimento <= 20:
    print('Categoria SÊNIOR')
else:
    print('Categoria MASTER')
