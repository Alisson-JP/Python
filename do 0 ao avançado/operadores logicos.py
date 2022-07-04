# operadores lógicos

# vamos simular uma situação de análise de crédito bancário
# se o usuário tem renda mínima a 5k, e se o nome estiver limpo = crédito aprovado
# do contrário = reprovado

renda_min_5k = True
nome_limpo = True

# usar o operador and
# o operador [ and ] é como uma soma, onde ambos precisam ser verdadeiros
if renda_min_5k and nome_limpo:
    print('Financiamento Aprovado!')
else:
    print('Financimento Negado!')


# teste com um False
renda_min_5k = True
nome_limpo = False

if renda_min_5k and nome_limpo:
    print('Financiamento Aprovado!')
else:
    print('Financimento Negado!')



# usar o operador or
# o operador [ or ] é como uma soma, onde apenas um item precisa ser verdadeiro

# teste com um False
renda_min_5k = True
nome_limpo = False

if renda_min_5k or nome_limpo:
    print('Financiamento Aprovado!')
else:
    print('Financimento Negado!')


# teste com dois False
renda_min_5k = False
nome_limpo = False

if renda_min_5k or nome_limpo:
    print('Financiamento Aprovado!')
else:
    print('Financimento Negado!')


