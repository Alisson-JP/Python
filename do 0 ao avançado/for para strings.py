# como trabalhar com for, para strings

# como printar uma palavra, letra a letra, verticalmente
for letra in 'Google':
    print(letra)


# automatizando o processo, com uma variável para a palavra que será digitada
palavra = str(input('Qual a palavra desejada? '))
for letra in palavra:
    print(letra)


# mencionando a palavra
palavra = str(input('Qual a palavra desejada? '))
for letra in palavra:
    print(letra + ' está dentro da palavra ' + palavra)


# formatando a sentença para evitar problemas
palavra = str(input('Qual a palavra desejada? '))
for letra in palavra:
    print(f'{letra} está dentro da palavra {palavra}')
