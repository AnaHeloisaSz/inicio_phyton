import random 
numero_secreto = random.randint (1,10)
tentativas = 0 
contagem_tentativas = 0
print ("Seja bem-vindo ao Jogo do Numero Secreto 🎮 ")
print ("Tente adivinhar o número secreto.")
print ("❗ Dica: o número está entre 1 e 10")
while tentativas != numero_secreto:
    numero = int(input("Digite um número "))
    contagem_tentativas = contagem_tentativas+1
    if numero == numero_secreto:
        print ("Parabéns! você acertou o número secreto. 😄 ")
        print ("Você tentou {contagem_tentativas} vezes.")
        break
    elif numero < numero_secreto:
        print ("O número secreto é maior, tente novamente")
    else:
        print ("O número secreto é menor, tente novamente")