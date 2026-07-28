numero1 = float(input('Digite o primeiro número: '))
operacao = input("digite a operação (+, -, *, /): ")
numero2 = float(input("Digite o segundo número: "))
if operacao == "+":
    resultado = numero1 + numero2
elif operacao == "-":
    resultado = numero1 - numero2
elif operacao == "*":
    resultado = numero1 * numero2
elif operacao == "/":
    resultado = numero1 / numero2
else: 
    resultado = "Operação inválida"

print(f"Resultado: {resultado}")
