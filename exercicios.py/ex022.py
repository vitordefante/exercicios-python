nome = input('Digite seu nome aqui: ').strip()
semletras = nome.replace(' ', '')  # indicar o valor do nome sem espaços no print ou inserir codigo na linha
semletras1 = len(semletras)  # colocar o código de analisar caracteres e tirar espaços na mesma linha
primeironome = nome.split()  # separar a string e ler a quantidade de caracteres de determinado valor da string após ser separada na mesma linha
primeironome1 = len(primeironome[0])
print('O nome escrito apenas com letras maíusculas é {}.'.format(nome.upper()))
print('O nome escrito apenas com letras minúsculas é {}.'.format(nome.lower()))
print('O nome inserido contém {} letras.'.format(semletras1))
print('O primeiro nome contém {} letras.'.format(primeironome1))
