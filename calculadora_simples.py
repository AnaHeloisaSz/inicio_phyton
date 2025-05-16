print(" Calculadora Simples 💯")
print("[1] Somar")
print("[2] Subtrair")
print("[3] Multiplicar")
print("[4] Dividir")
print('[0] Sair')

opcao = int(input(" Escolha uma opção "))

if opcao == 1:
    print(" Você escolheu somar. ")
    numero1 = int(input("escolha um número: "))
    numero2 = int(input("escolha um numero: "))
    resultado_soma = numero1 + numero2
    print (f"O resultado da soma é: {resultado_soma}")
    
if opcao == 2:
    print(" Você escolheu subtrair. ")
    numero1 = int(input("escolha o número: "))
    numero2 = int(input("escolha o numero: "))
    resultado_subtração = numero1 - numero2
    print (f"O resultado da subtração é: {resultado_subtração}")
    
if opcao == 3:
    print(" Você escolheu multiplicar. ")
    numero1 = int(input("escolha o número: "))
    numero2 = int(input("escolha o numero: "))
    resultado_multiplicacao = numero1 * numero2
    print (f"O resultado da multiplicação é: {resultado_multiplicacao}")
    
if opcao == 4:
    print(" Você escolheu dividir")
    numero1 = int(input("escolha o número: "))
    numero2 = int(input("escolha o numero: "))
    resultado_divisao = numero1 / numero2
    print (f"O resultado da divisão é: {resultado_divisao}")
    
if opcao == 5:
    print("Você escolheu sair...")
    