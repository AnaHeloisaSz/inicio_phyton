opcao = 0
frances = integral = doceLiso = doceFarofa = paoForma = 0
valorFrances = valorIntegral = valorDoceLiso = valorDoceFarofa = valorForma = 0

while opcao != 6:
    print("\n------------ PADARIA ------------")
    print("[1] Pão Francês - R$ 1.04")
    print("[2] Pão Integral - R$ 1.04")
    print("[3] Pão Doce Liso - R$ 1.08")
    print("[4] Pão Doce com Farofa - R$ 1.11")
    print("[5] Pão de Forma - R$ 0.95")
    print("[6] Finalizar Compra")
    print("---------------------------------")
    
    
    opcao = int(input("Escolha a sua opção: "))
    

    if opcao == 1:
        qtd = int(input("Quantidade de Pão Francês: "))
        frances = qtd
        valorFrances = qtd * 1.04

    elif opcao == 2:
        qtd = int(input("Quantidade de Pão Integral: "))
        integral = qtd
        valorIntegral = qtd * 1.04

    elif opcao == 3:
        qtd = int(input("Quantidade de Pão Doce Liso: "))
        doceLiso = qtd
        valorDoceLiso = qtd * 1.08

    elif opcao == 4:
        qtd = int(input("Quantidade de Pão Doce com Farofa: "))
        doceFarofa += qtd
        valorDoceFarofa = qtd * 1.11

    elif opcao == 5:
        qtd = int(input("Quantidade de Pão de Forma: "))
        paoForma = qtd
        valorForma = qtd * 0.95

    elif opcao == 6:
        break
    else:
        print("Opção inválida. Tente novamente.")


print("\n=========== RESUMO DA COMPRA ===========")
if frances > 0:
    print(f"Pão Francês - Quantidade: {frances} | Valor: R$ {valorFrances}")
if integral > 0:
    print(f"Pão Integral - Quantidade: {integral} | Valor: R$ {valorIntegral}")
if doceLiso > 0:
    print(f"Pão Doce Liso - Quantidade: {doceLiso} | Valor: R$ {valorDoceLiso}")
if doceFarofa > 0:
    print(f"Pão Doce com Farofa - Quantidade: {doceFarofa} | Valor: R$ {valorDoceFarofa}")
if paoForma > 0:
    print(f"Pão de Forma - Quantidade: {paoForma} | Valor: R$ {valorForma}")

total = valorFrances + valorIntegral + valorDoceLiso + valorDoceFarofa + valorForma
print("-----------------------------------------")
print(f"TOTAL A PAGAR: R$ {total}")
print("Obrigado pela compra:)")
