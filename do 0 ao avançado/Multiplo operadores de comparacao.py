# Múltiplos Operadores de Comparação

# Podemos utilizar vários comparadores de forma mixada

# vamos simular um ambiente de entrada de novos produtos
# onde o preço dos novos produtos tem que estar entre 20 e 40

# modo padrão de escrever
valor = int(input('Qual o valor do produto? '))

if valor >= 20 and valor < 40:
    print('Produto foi Aceito.')
else:
    print('Produto não aceito.')


# modo mais matemático
if 20 <= valor < 40:
    print('Produto foi Aceito.')
else:
    print('Produto não aceito.')

