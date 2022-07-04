# verificar métodos de string

mensagem = 'eu amo tocar BATERIA!!!'
#index      0123456789~
print(mensagem)


# colocando tudo em letra minúscula e imprimindo - lower
print(mensagem.lower())

# colocando tudo em letra maiúscula e imprimindo - upper
print(mensagem.upper())

# aplicando letra maiuscula na primeira letra - capitalize
print(mensagem.capitalize())

# procurar letra específica - find
print(mensagem.find('B'))

# onde inicia uma palavra - find
print(mensagem.find('tocar'))

# substiuir uma palavra por outra - replace
print(mensagem.replace('BATERIA', "VIOLÃO"))

# remover espaço (ou espaços) antes do primeiro caractere
print(mensagem.strip())


