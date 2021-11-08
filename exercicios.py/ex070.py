# programa que lê nome e preço de varios produtos, e mostra preço total, quantos >1000 e mais barato

produtos = []  # < nome dos produtos
precos = []  # < preco dos produtos
mil = 0
soma = 0

while True:
    produto = str(input('\n\033[1mInsira o nome do produto: ')).strip()
    produtos.append(produto)
    preco = float(input('Insira o preço do produto \033[1;32mR$\033[m '))
    precos.append(preco)
    soma += preco
    if preco >= 1000:
        mil += 1
    continuar = str(input('\n\033[1mDeseja continuar? Informe usando [S/N]: ')).strip().upper()
    while continuar != 'S' and continuar != 'N':
        continuar = str(input('\033[1mInput inválido. Informe apenas usando S/N: ')).strip().upper()
    if continuar == 'N':
        break
barato = min(precos)  # pega o menor número da lista de precos (produto com menor valor)
barato1 = precos.index(min(precos))  # pega o endereço da lista onde fica o menor valor, que também será o endereço
#                                                                                               do nome do produto
print('\nA soma total dos produtos é de \033[1;32mR${:.2f}\033[m\033[1m'.format(soma))
print('{} produtos custam mais de \033[1;32mR$1000\033[m\033[1m'.format(mil))
print('O nome do produto mais barato é {} e custa \033[1;32mR${:.2f}'
      .format(produtos[barato1], barato))
