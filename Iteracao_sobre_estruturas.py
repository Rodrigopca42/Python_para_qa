'''
status_code = [200, 404, 500, 201, 403]

for code in status_code:
    if code >= 400:
        print(f'Status {code}: Error')
    else:
        print(f'Status {code}: OK')
'''


#zip(): Combinar Estruturas em Paralelo
#Quando temos dados relacionados em listas separadas, zip() combina par a par:

testes = ["Login", "Busca", "Checkout"]
resultados = ["PASSOU", "FALHOU", "PASSOU"]
for teste, resultado in zip(testes, resultados):
    print(f"{teste}: {resultado}")






