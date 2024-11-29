inventario = {}
opcao = int(input('Digite: ' +'<1> Registrar ativo \n'
                  '<2> Persistir em arquivo \n'
                  '<3> Exibir ativos armazenados:'))
while opcao > 0 and opcao < 4:
    if opcao == 1:
        resp = 'S'
        while resp == 'S':
            inventario[input('Digite o número patrimonial: ')] = [
                input('Digite a data da última atulização: '),
                input('Digite a descrição: '),
                input('Digite o departamento: ')]
            resp = input('Digite <S> para continuar.').upper()
