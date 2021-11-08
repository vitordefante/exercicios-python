# leia a velocidade de um carro, se ultrapassar 80km/h haverá multa proporcional ao tamanho da infraçao
vel = float(input('Insira a velocidade maxima atingida pelo seu veículo na rodovia em km/h: '))
multa = (vel-80)*7
if vel > 80:
    print('\nVocê excedeu o limite de velocidade proposto nessa rodovia e será multado em R${:.2f}.'.format(multa))
else:
    print('\nVocê nao excedeu o limite de velocidade proposto e nao levou nenhuma multa.')
# segunda-feira assistir correçao novamente do exercicio acompanhando atenciosamente