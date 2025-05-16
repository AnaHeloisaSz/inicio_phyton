print("==Tabela de Preços==")
print("Valor do carro por dia: R$90.00")
print("Preço por KM: R$0.20")
print("--------------------")

precoAlugado = int(input("Quantos dias você ficou com o carro?"))
precoKm = int(input("Quantos Km foram percorridos?"))

total=(precoAlugado*90)+(precoKm*0.2)

print("=====RECIBO=====")
print("Valor do aluguel do carro:", (precoAlugado*90), " R$")
print("Valor dos quilometros rodados:",(precoKm*0.20), "R$")
print("Preço á pagar:", total, "R$")