'''
for i in range(3):
    for j in range(2):
        print("i =",i,"| j =",j)

'''
'''
for linha in range(3):
    for coluna in range(3):
        print("*",end=" ")
    print()
'''

x: int
soma: int

soma = 0
x= int(input('Digite o primeiro número: '))

while x != 0:
    soma = soma + x
    x = int(input('Digite outro número: '))

print('Soma = ', soma)














