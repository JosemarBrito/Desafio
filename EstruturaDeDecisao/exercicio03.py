#Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

"""print (5<6)
print (5>6)
print(5==6)"""

sexo = input('Digite seu sexo. (M) Masculino, (F) Feminino, (I) Indefinido :').upper()
if sexo == 'M':
    print ('Masculino')
elif sexo == 'F':
    print ('Feminino')
elif sexo == 'I':
    print('Indefinido')
else:
    print ('Sexo Inválido')

print ('Finalizou o Programa')
