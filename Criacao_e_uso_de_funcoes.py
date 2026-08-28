'''
def exibir_separador():
    print("-" * 40)
# Chamando a função
exibir_separador()
print("Relatório de Testes")
exibir_separador()
'''
'''
def exibir_status_teste(nome_teste, status):
    print(f"Teste: {nome_teste} | Status: {status}")

exibir_status_teste(nome_teste = "Login com credenciais válidas", status = "PASSOU")

exibir_status_teste("Login com senha incorreta", "PASSOU")

exibir_status_teste("Login sem preencher email", "FALHOU")
'''
'''
def classificar_status_code(codigo):
    if 200 <= codigo < 300:
        print(f"Status {codigo}: Sucesso")
    elif 400 <= codigo < 500:
        print(f"Status {codigo}: Erro do cliente")
    elif 500 <= codigo < 600:
        print(f"Status {codigo}: Erro do servidor")

classificar_status_code(201)
'''

#Chamando Funções dentro de Funções
def formatar_resultado(nome, status):
    icone = "✅" if status == "PASSOU" else "❌"
    return f"{icone} {nome}: {status}"

def calcular_taxa_sucesso(total, aprovados):
    if total == 0:
        return 0
    return (aprovados / total) * 100


def gerar_relatorio_suite(nome_suite, resultados):
    print(f"Suite: {nome_suite}")
    print("=" * 40)
    for teste, status in resultados:
        linha = formatar_resultado(teste, status) # Chamaoutra função
        print(f" {linha}")

    total = len(resultados)
    aprovados = sum(1 for _, s in resultados if s == "PASSOU")
    taxa = calcular_taxa_sucesso(total, aprovados) # Reutiliza
    print(f" Taxa de sucesso: {taxa}%")

# Chamando com dados reais de teste
testes_login = [
 ("Login válido", "PASSOU"),
 ("Login inválido", "PASSOU"),
 ("Login sem senha", "FALHOU"),
 ("Login bloqueado", "PASSOU"),
]
testes_cadastro = [
 ("Cadastro completo", "PASSOU"),
 ("Cadastro sem email", "PASSOU"),
 ("Cadastro duplicado", "FALHOU"),
]
gerar_relatorio_suite("Login", testes_login)
gerar_relatorio_suite("Cadastro", testes_cadastro)