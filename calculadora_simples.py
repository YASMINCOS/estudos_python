operacao = input("Digite a operacao desejada (+,-,*,/): ")
numero1 = input("Digite o primeiro número: ")
numero2 = input("Digite o segundo número: ")

if operacao == "+":
	resultado = int(numero1) + int(numero2)
elif operacao == "-":
	resultado = int(numero1) - int(numero2)
elif operacao == "*":
	resultado = int(numero1) * int(numero2)
elif operacao == "/":
	resultado = int(numero1) / int(numero2)
else:
	resultado = "Operação não suportada"
    
print("O resultado da operação é: " + str(resultado))
