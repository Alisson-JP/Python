# aprendendo a utilizar o slice
# pegar pedaços de strings ou números
# cortar parte ou blocos de informações e extrair somente o desejável

fruta = 'abacate'
#index   0123456

print(fruta)

# para puxar a letra específica da palavra abacate
# por exemplo, caso queiramos extrair a letra c
print(fruta[3])

# para pegar intervalos
# se quiser buscar as letras [ baca ], que seria de 1 até 4, 
# é necessário ir um item a mais, pq o python não pega o último item solicitado
# então, no caso, teremos que ir do  1 até 5
print(fruta[1:5])


# exercitando com valores
# por exemplo, centavos

valor = 33.459
#index  012345
valor = str(valor)
print(valor[3:6])

