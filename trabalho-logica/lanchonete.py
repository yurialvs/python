print('._____________________________________________.')

print('''
|             Lanchonete do Yuri              |
|_________________CARDÁPIO____________________|
| Código |       Descrição       | Valor (R$) |
|  100   |    Cachorro-Quente    |    9.00    |
|  101   | Cachorro-Quente Duplo |   11.00    |
|  102   |        X-Egg          |   12.00    |
|  103   |        X-Salada       |   12.00    |
|  104   |        X-Bacon        |   14.00    |
|  105   |        X-Tudo         |   17.00    |
|  106   |   Refrigerante Lata   |    5.00    |
|  107   |      Chá Gelado       |    4.00    |
''')

print('¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨')

acumulador=0 #acumulador de pedidos
while True:

  codigo = int(input('Digite o código do produto desejado: '))

  if codigo < 100 and codigo > 107:

    print('Opção inválida. Por gentileza digite um código existente!')
    continue #verifica se o código digitado é existente, se não repete o processo

  if codigo == 100:
    print('Você escolheu um Cachorro-Quente no valor de R$9.00')
    acumulador=acumulador+9

  elif codigo == 101:
    print('Você escolheu um Cachorro-Quente Duplo no valor de R$11.00')
    acumulador=acumulador+11

  elif codigo == 102:
    print('Você escolheu um X-Egg no valor de R$12.00')
    acumulador=acumulador+12

  elif codigo == 103:
    print('Você escolheu um X-Salada no valor de R$12.00')
    acumulador=acumulador+12

  elif codigo == 104:
    print('Você escolheu um X-Bacon no valor de R$14.00')
    acumulador=acumulador+14

  elif codigo == 105:
    print('Você escolheu um X-Tudo no valor de R$17.00')
    acumulador=acumulador+17

  elif codigo == 106:
    print('Você escolheu um Refrigerante Lata no valor de R$5.00')
    acumulador=acumulador+5

  elif codigo == 107:
    print('Você escolheu um Chá Gelado no valor de R$4.00')
    acumulador=acumulador+4

  pedir_mais = input('Deseja pedir mais alguma coisa? (sim/não) ')
  if pedir_mais == 'sim':
    print('Faça mais um pedido!')
    continue #para fazer mais pedidos o cliente digita 'sim' e para finalizar digita 'não'

  else: #programa finaliza com o valor total dos pedidos feito pelo cliente
    print('Valor total a ser pago: R${:.2f}'.format(acumulador))
    print('PEDIDO FINALIZADO, volte sempre!')
    break
