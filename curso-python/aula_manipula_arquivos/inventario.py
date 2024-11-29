inventario = {}
opcao = int(input('<1> Registrar ativo \n'
                  '<2> Persistir em arquivo \n'
                  '<3> Exibir ativos armazenados \n'
                  'Digite: '))

while opcao > 0 and opcao < 4:
    if opcao == 1:
        resp = 'S'
        while resp == 'S':
            inventario[input('Digite o número patrimonial: ')] = [
                input('Digite a data da última atulização: '),
                input('Digite a descrição: '),
                input('Digite o departamento: ')]
            resp = input('Digite <S> para continuar: ').upper()
    
    elif opcao == 2:
        with open('./curso-python/aula_manipula_arquivos/inventario.csv', 'a') as inv:
            for chave, valor in inventario.items():
                inv.write(chave + ';' + valor[0] + ';' + valor[1] + ';' + valor[2] + ';')
                print('Persistindo com sucesso!')
    
    elif opcao == 3:
        with open('./curso-python/aula_manipula_arquivos/inventario.csv', 'r') as inv:
            print(inv.readlines())
    
    opcao = int(input('<1> Registrar ativo \n'
                  '<2> Persistir em arquivo \n'
                  '<3> Exibir ativos armazenados \n'
                  'Digite: '))