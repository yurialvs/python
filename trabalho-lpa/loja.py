print('Bem Vindo a Loja do Yuri')
valor = float(input('Digite o valor do produto: '))
qntd = int(input('Digite a quantidade: '))

#Quantidade até 9 unidades recebe 0% de desconto
if qntd <= 9:
  desc = 0.00 #0%

#Quantidade entre 10 e 99 unidades recebe 5% de desconto
elif 10 <= qntd <= 99:
  desc = 0.05 #5%

#Quantidade entre 100 e 999 unidades recebe 10% de desconto
elif 100 <= qntd <= 999:
  desc = 0.10 #10%

#Quantidade a partir de 1000 unidades recebe 15% de desconto
else:
  qntd >= 1000
  desc = 0.15 #15%

#VALOR SEM DESCONTO
total_sem_desc = valor * qntd
print('O valor SEM desconto foi: R$ {:.2f}'.format(total_sem_desc))

#VALOR COM DESCONTO
total_com_desc = total_sem_desc - total_sem_desc * desc
print('O valor COM desconto foi: R$ {:.2f} (Desconto de {:.0f}%)'.format(total_com_desc, desc*100))