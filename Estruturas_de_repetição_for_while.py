'''
for numero in range(5):
    print("Executando...")
'''
'''print(list(range(5)))'''
'''
for numero in range(5):
    print(numero)
'''
'''
for numero in range(1,6):
    print(numero)
'''
'''
for numero in range(0,10,2):
    print(numero)
'''
'''
contador = 0
while contador <5:
    print(contador)
    contador += 1
'''
'''
contador=0
while contador < 10:
    print(contador)

    if contador == 5:
        break

    contador+=1
'''
'''
for numero in range(10):
    if numero == 3:
        break
    print(numero)
'''
'''
for numero in range(6):
    if numero == 3:
        continue
    print(numero)
'''

status_codes = [200,200,500,200]
for status in status_codes:
    if status == 500:
        print(f"status {status}, Erro encontrado!")
        break
    else:
        print(f'status {status}')


'''
status_codes = [200,200,500,200]
for status in status_codes:
    if status==200:
        continue
print("Status diferente de 200:",status)
'''