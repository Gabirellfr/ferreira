import os
os.system('cls | clear')

# def classificar_pedido(valor, dias):
#   if (valor < 100) or (dias>7):
#     print('A entrega é NORMAL')
#   elif ((valor >= 100) and (valor <= 500)) or ((dias >= 4) and (dias <= 7)):
#     print('A entrega é PRIORITÁRIA')   
#   else:
#     print('A entrega de URGENTE')  

# classificar_pedido(15, 1800)    

def classificar_pedido(valor_pedido, dias_para_entrega):
  if (valor_pedido < 100) or (dias_para_entrega > 7):
    return ("pedido normal")
  elif (valor_pedido >= 100 and valor_pedido<=500) or (dias_para_entrega >=4 and dias_para_entrega <=7):
    return ("pedido prioritário")
  else:
    return('pedido urgente')

#print(classificar_pedido(250, 3))
pedido1 = classificar_pedido(250, 3)
print(pedido1)
  










  