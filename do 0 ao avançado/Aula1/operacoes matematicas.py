# desenvolver operações matemáticas em python

calculo = 2 + 3
print(calculo)


# e se colocarmos uma multiplicação antes da soma
calc2 = 2 + 3 * 4
print(calc2)
# 1º é executado a multiplicação, para depois a soma

# multiplicação e divisão tem precedência quanto a adição e subtração


calc3 = 2 + 3 * 4 / 3
print(calc3)
# no caso acima, ficaria
# 2 + (( 3 * 4 ) / 3)
# ou seja, primeiro a multiplicação, depois a divisão, e por último a soma
# da esquerda para a direita, respeitando a preferência de multiplicação e divisão ante a soma e subtração

# para forçar a soma, deve-se utilizar o parêntese
calc4 = (2 + 3) * 4
print(calc4)


# potências / valores exponenciais
calc5 = 2 ** 3
print(calc5)

