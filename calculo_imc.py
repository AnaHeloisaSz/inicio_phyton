nome=str(input("Qual é o seu nome?"))
peso=float(input("Quanto você pesa?"))
altura=float(input("Qual a sua altura?"))

imc = peso/(altura*altura)

print(f"Seu IMC é de {imc}")

if imc<=18.5:
    print("Você esta abaixo do peso")
    
if imc>=18.5 and imc<=24.9:
    print("Seu peso é normal")
    
if imc>=25 and imc<=29.9:
    print("Esta com sobrepeso")
     
if imc>=30:
    print("Esta na obesidade")
