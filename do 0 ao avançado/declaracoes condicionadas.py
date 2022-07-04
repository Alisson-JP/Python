# testar e atribuir declarações condicionadas

# faremos um programa que "auditará" a velocidade do usuário
# se a velocidade estiver dentro do limite permitido, então
# o usuário receberá a mensagem que "está tudo ok"
# caso contrário, receberá um aviso para "baixar a velocidade"

velocidade_atual = int(input('Qual a sua velocidade atual? '))

if velocidade_atual > 100:
    print('Você está acima da velocidade máxima permitida!')
    print('Baixe a velocidade!')
elif velocidade_atual < 50:
    print('Você está abaixo da velocidade mínima requerida!')
    print('Aumente a velocidade para 60, pelo menos!')
else:
    print('Velocidade okay')


