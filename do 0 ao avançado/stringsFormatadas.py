# atuando com strings formatadas

# montagem de texto modo padrão
nome = 'Alisson'
sobrenome = 'Joabe'
profissao = 'Programador'

texto = 'O ' + nome + ' ' + sobrenome + ' é um excelente ' + '[' + profissao + '].'

print(texto)


# montagem de texto com [ f ]

texto2 = f'O {nome} {sobrenome} é um excelente [{profissao}].'
print(texto2)

