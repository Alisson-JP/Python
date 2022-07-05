# estudar e executar alguns tipo de looping for

# para aplicação em números

# tarefa sugerida: um programa para imprimir de 1 a 5 na tela
# modo manual
print(1)
print(2)
print(3)
print(4)
print(5)

# modo usando o [ for ]
# lembrando que o python vai até o limite anterior do último número que mencionamos
# ou seja, no caso de range(5), ele vai imprimir de 0 a 4
for contagem in range(5):
    print(contagem)


# para imprimir até 5
for contagem in range(6):
    print(contagem)

# se quisermos ignorar o 0 (zero), por exemplo
for contagem in range(1, 6):
    print(contagem)

# para adicionar pulos/intervalos de contagem (step)
for contagem in range(0, 6, 2):
    print(contagem)

