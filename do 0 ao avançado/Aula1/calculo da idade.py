# esse programa irá calcular a idade do usuário, mediante a entrada do ano que o usuário digitar


ano_de_nascimento = input("Em qual ano você nasceu? ")

idade_atual = 2022 - int(ano_de_nascimento)

print('Atualmente, você possui ' + str(idade_atual) + ' anos de idade.')


# ou, podemos escrever

ano_de_nascimento = int(input("Em qual ano você nasceu? "))

idade_atual = 2022 - ano_de_nascimento

print('Atualmente, você possui ' + str(idade_atual) + ' anos de idade.')

