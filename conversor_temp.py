print("Conversor de temperaturas🌡️")
print("1 - Celsius para Fahrenheit")
print("2 - Celsiu para Kelvin")
print("3 - Fahrenheit para Celsius")
print("4 - Fahrenheit para Kelvin")
print("5 - Kelvin para Celsius")
print("6 - Kelvin para Fahrenheit")

opcao = int(input("Escolha uma conversão"))

if opcao==1:
    tempInicial=float(input("Digite a temperatura em Celsius"))
    tempConvertida=(tempInicial*9/5)
    print(f"Temperatura em fahrenheit:{tempConvertida}")
    
elif opcao==2:
    tempInicial=float(input("Digite a temperatura em Celsius"))
    tempConvertida=(tempInicial+273.15)
    print(f"Temperatura em kelvin:{tempConvertida}")
    
elif opcao==3:
    tempInicial=float(input("Digite a temperatura em Fahrenheit"))
    tempConvertida=(tempInicial-32)*5/9
    print(f"Temperatura em Celsiu:{tempConvertida}")
    
elif opcao==4:
    tempInicial=float(input("Digite a temperatura em Fahrenheit"))
    tempConvertida=((tempInicial-32)*5/9)+273.15
    print(f"Temperatura em Kelvin:{tempConvertida}")
    
elif opcao==5:
    tempInicial=float(input("Digite a temperatura em Kelvin"))
    tempConvertida=tempInicial-273.15
    print(f"Temperatura em Celsius:{tempConvertida}")
    
elif opcao==6:
    tempInicial=float(input("Digite a temperatura em Kelvin"))
    tempConvertida=(tempInicial-273.15)*9/5+32
    print(f"Temperatura em Fahrenheit:{tempConvertida}")
    

    

    

    
