import os 
os.system('cls || clear')
# senha = str(input('Crie uma senha\n'))
# senhaCorreta = (len(senha)>=8) and (senha.isalpha() == False) and (senha.isdigit() == False)
# while (senhaCorreta == False):
#   print('A senha não atende os critérios de pelo menos 8 caracteres ou não tem números e letras')
#   senha = str(input('Tente criar outra senha\n'))
#   senhaCorreta = (len(senha)>=8) and (senha.isalpha() == False) and (senha.isdigit() == False)
# print('A senha foi criada com sucesso!') 

senha = str(input('Crie uma senha\n'))

if(len(senha) >= 8):
  if (senha.isalpha() == False and senha.isdigit() == False):
    print('Senha foi criada com sucesso')
  else:
    print('A senha deve ter números e letras')
else:
  print('A senha não tem 8 caracteres ou mais')