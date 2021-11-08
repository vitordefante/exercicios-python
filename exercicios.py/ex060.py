# aplicativo que lê um número e mostra seu fatorial..
numero = float(input('Insira um número para receber seu fatorial: '))
contador = numero
fatorial = numero
print(numero, end='')
while contador >= 2:
    contador = contador - 1
    fatorial = fatorial * contador
    print(' x', contador, end='')
print(' =', '\033[1;34m{:.2f}'.format(fatorial))
