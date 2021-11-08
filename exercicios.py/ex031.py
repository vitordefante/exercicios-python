# programa que calcula o valor de uma passagem ate 200km cobrando 0,50R$,e e 0,45R$ para 200km>
distancia = float(input('Digite aqui a distância da viagem em km: '))
if distancia <= 200:
    print('\nO valor da sua viagem é de R${:.2f}'.format(distancia*0.50))
else:
    print('\nO valor da sua viagem é de R${:.2f}'.format(distancia*0.45))

# há também um else simplficado, apesar de talvez nao ser a melhor opçao, ela existe

# preço = distancia * 0.50 if distancia <= 200 else distancia * 0.45
