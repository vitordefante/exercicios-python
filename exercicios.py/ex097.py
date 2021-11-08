# programa que tenha uma funçao escreva() e mostra as linhas externas adaptadas ao tamanho da string
def escreva(txt):
    print('\033[1m-' * (len(txt) + 4))
    print(f' {txt}')
    print('-' * (len(txt) + 4))


cont = 0
palavras = []
for x in range(0, 3):
    palavra = input('Digite algo: ').strip().title()
    palavras.append(palavra)
while cont < len(palavras):
    escreva(palavras[cont])
    cont += 1

# O programa tem uma funçao escreva, que o parâmetro é um texto, e printa o texto com umas linhas em cima em embaixo,
#   do tamanho do texto. Há uma lista que irá armezenar 3 inputs de texto, e depois será printado os 3 textos com a
#    funçao.

