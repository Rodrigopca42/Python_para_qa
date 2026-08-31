'''
status_code = 404
endpoint = "/usuarios/99"
tempo_resposta = 230

# Concatenação com + — verboso e propenso a erro
mensagem1 = "Status: " + str(status_code) + " | Endpoint: "+ endpoint + " | Tempo: " + str(tempo_resposta) + "ms"
# .format() — ainda encontrado em código legado
mensagem2 = "Status: {} | Endpoint: {} | Tempo: {}ms".format(status_code, endpoint, tempo_resposta)

print(mensagem1)
print(mensagem2)
'''

def relatar_teste (nome , passou, tempo_ms, detalhe=''):
    status_label = 'Passou' if passou else 'Falhou'
    base = f'[{status_label}] {nome} ({tempo_ms}ms)'
    if detalhe:
        base += f' - {detalhe}'
    return base

print(relatar_teste('Login com credênciais válidas', True, 145))
print(relatar_teste('Login com senha errada', False, 89, 'é esperado 401, recebido 200'))
print(relatar_teste('Exportar relatório CSV', False, 5001, 'timeout após 5000ms'))



