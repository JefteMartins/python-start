#   vai ai um codigo pra ver se 2 dos 3 numeros
#   somados da igual ao 3° que restou
#   bem facin é tóis
def verificaNumero():
    num1 = input("Digite o primeiro numero: ")
    num2 = input("Digite o segundo numero: ")
    num3 = input("Digite o terceiro numero: ")
    num1 = int(num1) #atribuindo o valor de 1 a um inteiro pq pegava como string
    num2 = int(num2) #mesma coisa aqui
    num3 = int(num3) #aqui tbm viu?
    if num1 + num2 == num3 or num1 == num2 - num3 or num1 * num2 == num3:
        print("Passou")
        return
    print("Não passou")
    return
print("teste teste")
print(verificaNumero())