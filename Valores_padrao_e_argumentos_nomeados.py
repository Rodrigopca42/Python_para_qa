'''
def gerar_url_teste(endpoint, ambiente="dev"):
    bases = {
    "dev": "https://dev.api.com",
    "hml": "https://hml.api.com",
    "prod": "https://api.com"
    }
    base = bases.get(ambiente, "https://dev.api.com")
    return f"{base}/{endpoint}"

# Sem passar ambiente: usa "dev"
print(gerar_url_teste("users")) # https://dev.api.com/users

# Passando ambiente: sobrescreve o padrão
print(gerar_url_teste("users", "hml")) # https://hml.api.com/users

print(gerar_url_teste("users", "prod")) # https://api.com/users
'''

def validar_resposta_api(
 status_code,
 corpo,
 status_esperado=200,
 campos_obrigatorios=None,
 tempo_resposta=None,
 max_tempo=5.0
):
    if campos_obrigatorios is None:
        campos_obrigatorios = []
    erros = []
    if status_code != status_esperado:
        erros.append(f"Status: esperado {status_esperado},recebeu {status_code}")
    for campo in campos_obrigatorios:
        if campo not in corpo:
            erros.append(f"Campo ausente: '{campo}'")
    if tempo_resposta is not None and tempo_resposta > max_tempo:
        erros.append(f"Tempo: {tempo_resposta}s excede limite de {max_tempo}s")
    print({"valido": len(erros) == 0, "erros": erros})

# Validação mínima (só status)
validar_resposta_api(200, {"id": 1})
# Com campos obrigatórios
validar_resposta_api(200, {"id": 1}, campos_obrigatorios=
["id", "nome"])
# Validação completa
validar_resposta_api(
 status_code=201,
 corpo={"id": 1},
 status_esperado=200,
 campos_obrigatorios=["id", "nome"],tempo_resposta=6.2
 )

# Endpoint de criação (status 201)
print(validar_resposta_api(201, {"id": 99}, status_esperado=201))





