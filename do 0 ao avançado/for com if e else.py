# atuando com for, utilizando if e else

# vamos supor uma situação onde enviaremos um e-mail com os detalhes
# da compra online, com no máximo 3 tentativas, para as compras confirmadas

compra_confirmada = False
dados_compra = 'Compra no valor de R$ 12.50, e entrega confirmada.'

if compra_confirmada:
    print(dados_compra)
    print('Detalhes enviados para o seu e-mail.')


# agora colocando tudo isso dentro de um for
for enviar in range (3):
    if compra_confirmada:
        print(dados_compra)
        print('Detalhes enviados para o seu e-mail.')
        break       # o break é que fará com que o python saia do loop for, se a sentença for verdadeira
else:
    print('Falha na compra!')



