print('e aí pessoal')


# Como integrar strings e integer.

nome = 'Alisson'
idade = 38
cidade = 'Campinas'

print('O ' + nome + ' tem ' + str(idade) + ' anos de idade e mora em ' + cidade + '.')

# ou, pode-se mudar 

nome = 'Alisson'
idade = 38
idade = str(idade)
cidade = 'Campinas'

print('O ' + nome + ' tem ' + idade + ' anos de idade e mora em ' + cidade + '.')

# adicionando o input - o usuário irá adicionar a informação via teclado

nome = input('Qual é o seu nome? ')
idade = input('Qual é a sua idade? ')
idade = str(idade)
cidade = input('Em qual cidade você mora? ')

print('O ' + nome + ' tem ' + idade + ' anos de idade e mora em ' + cidade + '.')

