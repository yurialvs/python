with open('pagina.html', 'w') as pagina:
    pagina.write('<body> <h1> Teste para página WEB </h1> \n')
    pagina.write('<br> <h2> Abaixo seguem alguns nomes importantes para o projeto: </h2> \n')
    pagina.write('<h3>')
    nome = ''
    while nome != 'SAIR':
        nome = input('Digite um nome ou SAIR: ').upper()
        if nome != 'SAIR':
            pagina.write('<br>' + nome)
    pagina.write('</h3> </body>')