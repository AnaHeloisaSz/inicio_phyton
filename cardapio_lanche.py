opcao = 0
while opcao != 5:
    print  ("Cardápio")
    print ("1. Hambúrguer 🍔")
    print ("2. Pizza 🍕")
    print ("3. Salada 🥗")
    print ("4. Refrigerante 🥤")
    print ("5. Sair")
    
    opcao = int(input("Escolha uma opção: "))
    
    if opcao == 1:
        print("Você selecionou hambúrguer.")
    elif opcao == 2:
        print("Você selecionou Pizza.")
    elif opcao == 3:
        print("Você selecionou salada.")
    elif opcao == 4:
        print("Você selecionou Refrigerante.")
    elif opcao == 5:
        print("Você esta saindo do cardápio...")
        break