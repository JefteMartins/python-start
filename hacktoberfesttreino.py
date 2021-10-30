def verificaNumero():
    num1 = input("Digite o primeiro numero: ")
    num2 = input("Digite o segundo numero: ")
    num3 = input("Digite o terceiro numero: ")
    num1 = int(num1)
    num2 = int(num2)
    num3 = int(num3)
    if num1 + num2 == num3 or num1 == num2 - num3 or num1 * num2 == num3:
        print("Passou")
        return
    print("Não passou")
    return
print(verificaNumero())