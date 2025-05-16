nome = str (input("Qual é o seu nome?"))  
salarioFixo = float (input("Qual o seu salario?")) 
vendasTotal = int (input("Quantas vendas você realizou?")) 

bonus = 0.15
salarioTotal = salarioFixo*bonus

if vendasTotal>=20:  
    print(f"Você bateu sua meta! você vai receber R${salarioTotal} de comissão e R${salarioTotal+salarioFixo} reais no seu salário")
else:
    print(f"Você não bateu a meta, vai receber R${salarioFixo}")






