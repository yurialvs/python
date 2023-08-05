while True:
    try:
        cod = int(input('SEJA BEM-VINDO A LAVANDERIA!\n'+
               'Digite o código da opção desejada:\n'+
               '1 - Tabela de valores\n'+
               '2 - Endereço da loja\n'+
               '3 - Horários de funcionamento\n'+
               '4 - Prazos de serviços\n'+
               '5 - Falar com atendente\n'+
               '6 - Finalizar atendimento\n'+
               '>> '))

        if cod == 1: # TABELA DE VALORES
            print('1 - TABELA DE VALORES\n'+
            'Camisa - R$13,00\n'+
            'Calça - R$14,00\n'+
            'Camiseta - R$11,00\n'+
            'Terno - R$32,00\n'+
            'Bermuda- R$11,00\n'+
            '\n')

        elif cod == 2: # ENDEREÇO DA LOJA
            print('2 - ENDEREÇO DA LOJA\n'+
            'Link do GoogleMaps: https://www.google.com.br/maps/place/Brasil\n'+
            '\n')

        elif cod == 3: # HORÁRIOS DE FUNCIONAMENTO
            print('3 - HORÁRIOS DE FUNCIONAMENTO\n'+
            'Segunda a Sexta:\n'+
            '08:00 às 19:00\n'+
            'Sábado:\n'+
            '08:00 às 15:00\n'+
            '\n')

        elif cod == 4: # PRAZOS DE SERVIÇOS
            print('4 - PRAZOS DE SERVIÇOS\n'+
            'Tapetes - 10 a 15 dias\n'+
            'Cortinas - 1 semana\n'+
            'Roupas - 2 dias\n'+
            'Tênis - 5 dias\n'+
            '\n')

        elif cod == 5: # FALAR COM ATENDENTE
            print('5 - FALAR COM ATENDENTE\n'+
            'Atendimento solicitado! Aguarde...\n'+
            '\n')
            break

        elif cod == 6: # FINALIZAR ATENDIMENTO
            print('6 - Finalizar atendimento\n'+
            'Atendimento Finalizado!\n'+
            '\n')
            break
            
        else: # CORREÇÃO DE ERRO DE CÓDIGO
            print('Código inválido, tente novamente.\n')

    except ValueError: # CORREÇÃO DE ERRO DE DIGITAÇÃO
        print('Código inválido, tente novamente.\n')