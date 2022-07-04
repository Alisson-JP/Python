# operadores ternários

#Como economizar linhas de código ao utilizar if, elif, else statements

# vamos simular um controle de idade, para saber se usuário tem idade mínima ou não para votar (16 anos)

# modo padrão de montar if, else
idade_atual = int(input('Qual a sua idade  atual? '))

if idade_atual >= 16:
    print('Voto Permitido!')
else:
    print('Voto não Permitido!')


# modo ternário
resultado = 'Voto Permitido!' if idade_atual >= 16 else 'Voto não Permitido!'
print(resultado)

