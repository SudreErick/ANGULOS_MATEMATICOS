import math

co = float(input('comprimento do cateto oposto: '))
ca = float(input('comprimento do cateto adjacente: '))
hipo = (co ** 2 + ca ** 2) ** (1/2)
print('a hipotenusa vai medir {}'.format(hipo))
seno = float(co/hipo)
cosseno = float(ca/hipo)
tan = float(co/ca)
print('''ESCOLHA UMA DAS FORMULAS: 
[ 1 ] converter para SENO
[ 2 ] converter para COSSENO
[ 3 ] converter para TANGENTE''')
opção = int(input('sua opção: '))
if opção == 1:
    print('O SENO VALE: ', seno)
elif opção == 2:
    print('O COSSENO VALE: ', cosseno)
elif opção == 3:
    print('A TANGENTE VALE', tan)
else:
    print('funçao invalida. TENTE NOVAMENTE')
