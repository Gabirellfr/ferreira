# 1. Simulação de dados de bugs reportados:
bugs = [
    {"titulo": "App crash ao fazer login", "gravidade": "Crítico"},
    {"titulo": "Erro no pagamento", "gravidade": "Alto"},
    {"titulo": "Carrinho calcula errado", "gravidade": "Alto"},
    {"titulo": "Tela lenta no painel", "gravidade": "Médio"},
    {"titulo": "Erro no pagamento", "gravidade": "Alto"},
    {"titulo": "Erro no pagamento", "gravidade": "Alto"},
    {"titulo": "App crash ao fazer login", "gravidade": "Crítico"},
    {"titulo": "App crash ao fazer login", "gravidade": "Crítico"},
    {"titulo": "Carrinho calcula errado", "gravidade": "Alto"},
    {"titulo": "Carrinho calcula errado", "gravidade": "Alto"},
    {"titulo": "Carrinho calcula errado", "gravidade": "Alto"},
    {"titulo": "Tela lenta no painel", "gravidade": "Médio"},
    {"titulo": "Tela lenta no painel", "gravidade": "Médio"},
    {"titulo": "Tela lenta no painel", "gravidade": "Médio"},
    {"titulo": "Tela lenta no painel", "gravidade": "Médio"},
]

# 2. Classificar bugs por gravidade e contar frequência
contagem = {}

for bug in bugs:
    titulo = bug["titulo"]
    gravidade = bug["gravidade"]

    if titulo not in contagem:
        contagem[titulo] = {"gravidade": gravidade, "quantidade": 0}

    contagem[titulo]["quantidade"] += 1

# 3. Identificar bugs com mais de 5 reportagens
prioritarios = []

for titulo, info in contagem.items():
    if info["quantidade"] > 5:
        prioritarios.append(titulo)

# 4. Gerar relatório resumido
print("=== RELATÓRIO SEMANAL DE BUGS ===\n")

# Resumo por gravidade
gravidades = {}
for titulo, info in contagem.items():
    g = info["gravidade"]
    gravidades[g] = gravidades.get(g, 0) + info["quantidade"]

print("Resumo por gravidade:")
for g, total in gravidades.items():
    print(f"- {g}: {total} ocorrências")

# Lista de todos os bugs
print("\nBugs reportados:")
for titulo, info in contagem.items():
    print(f"- {titulo} ({info['gravidade']}) -> {info['quantidade']} reportes")

# Bugs prioritários
print("\nBugs prioritários (mais de 5 reportes):")
if prioritarios:
    for titulo in prioritarios:
        print(f"* {titulo}")
else:
    print("Nenhum bug ultrapassou 5 reportes nesta semana.")

print("\nRelatório gerado automaticamente (simulação).")