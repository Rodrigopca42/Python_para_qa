'''
Sintaxe básica

Objetivo da Aula
Ao final desta aula, o aluno deverá ser capaz de:
Entender como o Python organiza o código
Compreender a importância da indentação
Reconhecer instruções básicas da linguagem
Escrever e executar comandos simples em Python
Evitar erros comuns de sintaxe

====================================================
O que é sintaxe?
Sintaxe é o conjunto de regras que define como o código deve ser escrito
para que o Python consiga entender.
Assim como na língua portuguesa, onde uma frase mal escrita perde o sentido,
em Python:

Código fora da sintaxe correta não executa
Pequenos erros geram falhas imediatas
Primeira regra: indentação é obrigatória
Diferente de muitas linguagens, Python usa indentação para definir blocos de
código.

Indentação é o espaçamento no início da linha.
Exemplo correto:
if True:
 print("Essa linha está dentro do if")
Exemplo incorreto:
if True:
Sintaxe básica 1
print("Erro de indentação")
Resultado:
IndentationError: expected an indented block
Padrão de indentação
Use 4 espaços
Não misture espaços com TAB
O PyCharm cuida disso automaticamente
Fim de linha e separação de comandos
Em Python:
Cada linha representa uma instrução
Não é necessário usar ; no final da linha
Exemplo:
print("Linha 1")
print("Linha 2")
Uso de maiúsculas e minúsculas (case sensitive)
Python diferencia letras maiúsculas de minúsculas.
Exemplo:
print("Ok")# correto
Print("Erro")# erro
Erro gerado:
NameError:name'Print'isnot defined
Sintaxe básica 2
Comentários no código
Comentários servem para documentar o código e não são executados.
Comentário de uma linha:
# Este é um comentário
print("Código executado")
Comentários em boas práticas:
Explique o porquê, não o óbvio
Use comentários para regras de negócio
Evite comentários desnecessários
Strings: textos em Python
Strings são textos e podem ser declaradas com:
"texto"
'texto'
Exemplo:
print("Python para QAs")
print('Curso básico')
Erros comuns de sintaxe
1. Esquecer dois pontos ( : )
if True
print("Erro")
Erro:
SyntaxError: expected ':'
Sintaxe básica 3
2. Aspas não fechadas
print("Erro)
Erro:
SyntaxError: unterminated string literal (detected at line 1)
3. Indentação incorreta
Misturar TAB e espaços gera erro.
Boas práticas iniciais de sintaxe
Código limpo é mais importante que código curto
Quebre linhas longas
Confie nas mensagens de erro do Python
Na próxima aula, entraremos em comentários e boas práticas iniciais,
aprofundando ainda mais a organização do código.
Sintaxe básica 4'''