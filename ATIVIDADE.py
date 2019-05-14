#atividade 1#
pedido = input('Digite seu pedido:')
print(pedido)
if pedido == salgado:
    print('Valor = R$4,00')
elif  pedido == cafe:
    print('Valor = R$4,00')
elif pedido == refrigerante:
    print('Valor = R$4,50')
elif pedido == bolo:
    print('Valor = R$4,50')
elif pedido == suco:
    print('Valor = R$5,00')

elif pedido == sorvete or pedido == capuccino:
    print('Valor = R$6,00')

elif pedido == dadinho:
     print('Valor = R$0,50')




#atividade2#

    nome1 = input('Digite seu nome:')
pedido1 = input('Digite seu pedido:')
print(nome1, pedido1)

nome2 = input('Digite seu nome:')
pedido2 = input('Digite seu pedido:')
print(nome2, pedido2)

nome3 = input('Digite seu nome:')
pedido3 = input('Digite seu pedido:')
print(nome3, pedido3)

nome4 = input('Digite seu nome:')
pedido4 = input('Digite seu pedido:')
print(nome4, pedido4)

nome5 = input('Digite seu nome:')
pedido5 = input('Digite seu pedido:')
print(nome5, pedido5)

nome6 = input('Digite seu nome:')
pedido6 = input('Digite seu pedido:')
print(nome6, pedido6)

nome7 = input('Digite seu nome:')
pedido7 = input('Digite seu pedido:')
print(nome7, pedido7)

lista_nomes = [nome1, nome2, nome3]
lista_pedido = [pedido1, pedido2, pedido3]
print(lista_nomes,lista_pedido)

#atividade3#

def valor(pedido):
    if pedido == salgado:
        print(pedido, 'Valor = R$4,00')
    elif pedido == cafe:
         print(pedido, 'Valor = R$4,00')
    elif pedido == refrigerante or pedido == bolo:
        print(pedido, 'Valor = R$4,50')

    elif pedido == suco:
         print(pedido, 'Valor = R$5,00')

    elif pedido == sorvete or pedido == capuccino:
        print(pedido, 'Valor = R$6,00')

    elif pedido == dadinho:
        print(pedido, 'Valor = R$0,50')
    return valor


nome = input('Digite seu nome:')
pedido = input('Digite seu pedido:')


print(nome, pedido, valor)
