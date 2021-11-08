# aplicativo que lê um numero e o transforma termos da sequencia de fibonacci
cont = int(input('Insira quantos termos da sequencia de Fibonacci deseja ver: '))
if cont == 1:
    print('0')
elif cont == 2:
    print('0\n1')
elif cont == 3:
    print('0\n1\n1')
elif cont > 3:
    print('0\n1\n1')
    cont0 = 1
    ultimo = 1
    penultimo = 1
    while cont0 <= cont - 3:
        cont0 = cont0 + 1
        termo = ultimo + penultimo
        penultimo = ultimo
        ultimo = termo
        print(termo)
# a logica de funcionamento desse programa baseia-se na substituiçao de dados durante um loop

#  cont0 = 1       < contagem até chegar no cont inicial do input
#     ultimo = 1  < ultimo numero dos dois primeiros algarismos da sequencia fib
#     penultimo = 1 < penultimo numero dos dois primeiros algarismos da sequencia fib
#     while cont0 <= cont - 3:  < -3 pois a sequencia se aplica ao terceiro numero da sequencia em diante
#         cont0 = cont0 + 1  < somando o contador
#         termo = ultimo + penultimo  < o termo final da sequencia (penultimo + ultimo numero da sequencia)
#         penultimo = ultimo  < o penultimo número precisa tornar-se o novo ultimo
#         ultimo = termo   < o ultimo número torna-se o resultado da soma entre o penultimo e ultimo
#         print(termo)
