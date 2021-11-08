# programa que ê nome, idade e sexo de 4 pessoas e mostra: media de idade, nome do homem mais velho, quantas muie etc

#  text colors #
format = '\033[1;m'
blue = '\033[1;34m'
purple = '\033[1;35m'
lightblue = '\033[1;36m'
#  lista com todos inputs de nome, idade, genero etc #
count = 0  # mulheres com idade acima de 20
generos = []
mulhernomes = []
mulheridades = []
homemnomes = []
homemidades = []
grupoidade = mulheridades + homemidades

print('A seguir adicione as informaçoes das 4 pessoas')

for i in range(0, 4):   # loop para inserir as informaçoes dentro das listas acima
    genero = int(input('Digite {}1{} para {}homem{} e {}2{} para {}mulher{}: '
                       .format(blue, format, blue, format, purple, format, purple, format)))
    if genero == 1:
        nome = input('{}Insira aqui seu nome: '.format(format))
        idade = int(input('Insira aqui sua idade: '))
        homemidades.append(idade)  # insere as infomaçoes de genero, idade e nome no grupo dos homens e no grupo geral
        generos.append(genero)      # .append para inserir input em uma determinada lista
        homemnomes.append(nome)
        grupoidade.append(idade)
    elif genero == 2:
        nome = input('{}Insira aqui seu nome: '.format(format))
        idade = int(input('Insira aqui sua idade: '))
        if idade < 20:
            count = count + 1  # <inserir mulheres com a baixo de 20 anos no count para depois printar
        mulheridades.append(idade)  # insere a informaçoes de idade, nome e genero no grupo das mulheres e grupo geral
        generos.append(genero)  # .append para inserir um input em uma determinada lista
        mulhernomes.append(nome)
        grupoidade.append(idade)

grupoidade1 = sum(grupoidade)
homemvelho = homemidades.index(max(homemidades))
# prints para mostrar as informaçoes requeridas pelo exercício
print('\n{}A média de idade do grupo é de {} anos.'.format(lightblue, grupoidade1 / 4))
print('{}O homem mais velho do grupo é {} e tem {} anos.'.format(blue, homemnomes[homemvelho], homemidades[homemvelho]))
print('{}No grupo, o número de mulheres com idade abaixo de 20 anos é {}.'.format(purple, count))
