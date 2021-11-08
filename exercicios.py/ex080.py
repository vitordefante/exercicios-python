# ler 5 numeros e colocalos em uma lista em ordem sem usar o sort
lista = []
for x in range(0, 5):
    lista.append(int(input('Insira um valor na lista: ')))
print('Os valores digitados em ordem foram {}'.format(sorted(lista)))
