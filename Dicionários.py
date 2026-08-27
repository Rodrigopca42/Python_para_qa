'''
usuario = {
'nome': 'Carlos',
'idade': 30,
'ativo': True
}

print(usuario)
print()
print(usuario.items())
print()
print(usuario.values())
print()
print(usuario['nome'])

print(usuario['idade'])
'''

'''
usuario = {
    'nome': 'Rodrigo',
    'idade': 47
}

usuario['cidade'] = 'Nova Iguaçu'

print(usuario)

for valor in usuario.values():
    print(valor)
'''


resposta_api = {
'statu_code': 401,
'mensagem': 'Secesso',
'tempo_resposta': 120
}

if resposta_api['statu_code'] != 200:
    print('Erro na API')

print('tempo de resposta: ', resposta_api['tempo_resposta'])

