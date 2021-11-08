# refaça o desafio 051, lendo o primeiro termo e a razao de uma PA, mostrando os 10 primeiros termos da progressao
# usando a estrutura while
t1 = float(input('Insira o primeiro termo da razao: '))
r = float(input('Insira a razao da p.a: '))
cont = 0
print('Os dez primeiros termos da progressao sao')
print(t1)
while cont <= 8:
    cont = cont + 1
    print(t1 + r * cont)
