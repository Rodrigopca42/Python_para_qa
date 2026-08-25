'''
N = int(input('Quantos números vc vai digitar? '))

vet:[float] = [0 for x in range(N)]

for i in range(0, N):
    vet[i] = float(input('Digite um número: '))

print()
print('NÚMEROS DIGITADOS:')

for i in range(0,N):
    print(f'{vet[i]: .1f}')
'''
'''
ambientes = ["desenvolvimento", "homologação", "produção"]

print(ambientes[0]) # desenvolvimento
print(ambientes[1]) # homologação
print(ambientes[2]) # produção
'''

'''
ambientes = ["desenvolvimento", "homologação", "produção"]

print(ambientes[-1]) # produção ← último
print(ambientes[-2]) # homologação ← penúltimo
print(ambientes[-3]) # desenvolvimento ← antepenúltimo
'''


execucoes = ["PASSOU", "PASSOU", "FALHOU", "PASSOU"]
ultimo_resultado = execucoes[-1]
print(f"Resultado mais recente: {ultimo_resultado}")


