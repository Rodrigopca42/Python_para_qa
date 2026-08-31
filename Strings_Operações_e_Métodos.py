
'''
email = 'QA@EMAIL.COM'

email_normalizado = email.lower()
print(email)
print(email_normalizado)
'''
'''
protocolo = 'http://1.1'
print(protocolo[6])
print(protocolo[:10])
print(protocolo[10:])
print(protocolo[1])
'''
'''
token = "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9"
tipo_auth = token[7:] # "Bearer"

print(tipo_auth)
'''

#Metodo de busca e verificação
'''
linha_log = 'ERROR: falha de autenticação do usuário'

print(linha_log.startswith('ERROR'))
print(linha_log.startswith('WARNING'))
print(linha_log.endswith('usuário'))
'''

#Metodods de transformação

email = " usuario@teste.com "
print(email.strip()) # 'usuario@teste.com'
print(email.lstrip()) # 'usuario@teste.com '
print(email.rstrip()) # ' usuario@teste.com'
