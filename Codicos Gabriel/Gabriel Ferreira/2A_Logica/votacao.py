import os
os.system('clear || cls')
print('Vote 1 para o Partido A:\nCandidato à Presidência: Eneas Carneiro\nCandidato à Vice-Presidência: Getúlio Vargas\n\nVote 2 para o Partido B:\nCandidato à Presidência: Lula\nCandidato à Vice-Presidência: Bolsonario\n\n')
voto = int(input('Digite o número do Partido\n'))
if (voto == 1):
  print('Partido A venceu')
elif(voto == 2):
  print('Partido B venceu')
else:
  print('Você votou nulo')
