valor_saque = int(input("Digite o valor do saque: R$"))
notas = [50, 20, 10, 5]  # Lista com os valores das notas
quantidade_50 = 0
quantidade_20 = 0
quantidade_10 = 0
quantidade_5 = 0
while valor_saque > 0:
    for nota in notas:
        while valor_saque >= nota:
            if nota == 50:
                quantidade_50 += 1
            elif nota == 20:
                quantidade_20 += 1
            elif nota == 10:
                quantidade_10 += 1
            elif nota == 5:
                quantidade_5 += 1
            valor_saque -= nota
print(f"Notas de R$50: {quantidade_50}")
print(f"Notas de R$20: {quantidade_20}")
print(f"Notas de R$10: {quantidade_10}")
print(f"Notas de R$5: {quantidade_5}")
