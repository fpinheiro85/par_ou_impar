nome = input('Qual seu nome? ')
print("")
print('Seja bem vindo ' + nome)
print('')
n = float(input('Digite um numero: '))
r = (n%2)
print('')
if r == 0 :
    print('O numero {:.0f} é PAR' .format(n))
else:
    print('O numero {:.0f} é IMPAR' .format(n))
