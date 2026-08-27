'''
ambientes = ("desenvolvimento", "homologação", "produção")
print(ambientes[0]) # desenvolvimento
print(ambientes[1]) # homologação
print(ambientes[2]) # produção
print(ambientes[-1]) # produção (índice negativo)
'''
'''
ambientes = ("desenvolvimento", "homologação", "produção")
ambientes[1] = "staging" # tentativa de alteração
'''
'''
# Usando lista — risco de alteração acidental
urls = ["https://dev.api.com", "https://hml.api.com", "https://pi.com"]
urls[2] = "http://api.com" # alteração silenciosa, sem erro
print(urls)

print()
# Usando tupla — protegido contra alteração
urls = ("https://dev.api.com", "https://hml.api.com", "https://pi.com")
urls[2] = "http://api.com" # TypeError imediato
print(urls)
'''