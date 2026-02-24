import os
os.system ('cls')

alunos = ['aprovado','reprovado','aprovado','reprovado''aprovado','reprovado''aprovado','reprovado''aprovado','reprovado''aprovado','reprovado''aprovado','reprovado''aprovado','reprovado''aprovado','reprovado''aprovado','reprovado''aprovado','reprovado''aprovado','reprovado''aprovado','reprovado''aprovado','reprovado''aprovado','reprovado''aprovado','reprovado''aprovado','reprovado''aprovado','reprovado''aprovado','reprovado''aprovado','reprovado''aprovado','reprovado''aprovado','reprovado''aprovado','reprovado']

contador = 0
for itens in alunos:
    if itens == 'reprovado':
        contador += 1 

print(f'{contador} alunos foram reprovados')