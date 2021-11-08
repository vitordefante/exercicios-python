# ler uma frase e mostrar quantas letra 'a' ela possui, quais as posiçoes da primeira e ultima vez que a letra aparece
frase = input('Insira uma frase a seguir: ').upper().strip()
aquantos = frase.count('A')
aprimeiro = frase.find('A')+1
aultimo = frase.rfind('A')+1
print('A frase que você inseriu possui {} letras "a", a primeira encontra-se no caractere {} da frase e a última no'
      ' caractere {}' .format(aquantos, aprimeiro, aultimo))
# mostrar a frase inserida no último print sem .upper ou .lower e mostrar a quantia total da 'a' minusculo e maiusculo
