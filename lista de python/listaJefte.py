#Aluno: Jefté Oliveira Martins
#Estrurua de dados lista 1


#R-1.1 Write a short Python function, is_multiple(n, m), that takes two integer values and #
#returns True if n is a multiple of m, that is, n = mi for some integer i, and False otherwise#

def multiplo(n,m):
    if m == 0: return(False)
    return (n%m==0) #vendo se o divisor é igual a 0

print(multiplo(5,3))
print(multiplo(15,5))

#R-1.3 Write a short Python function, minmax(data), that takes a sequence of one or more
#numbers, and returns the smallest and largest numbers, in the form of a tuple of length
#two. Do not use the built-in functions min or max in implementing your solution

def minmax(numeros):
    maior = numeros[0] #o maior começa com o a posição 0 e vai atualizando
    menor = numeros[0] #mesma coisa com o menor
    for i in numeros:  #percorre o vetor e atualiza menor ou maior
        if i > maior:
            maior = i
        elif i < menor:
            menor = i
    return menor, maior

vetor = [1,2,3,4,5,6,7,8,9,10]
print(minmax(vetor))

#R-1.4 Write a short Python function that takes a positive integer n and returns the sum of
#the squares of all the positive integers smaller than n.

def soma_dos_quadrados(num):
    print("soma dos quadrados abaixo de", num,":")
    num -=1 #tira um pra começar abaixo do numero escolhido
    total = 0 #variável auxiliar que retorna o total
    while num > 0:
        total += num*num #adiciona ao total
        num-=1 #tira um do numero escolhido para continuar o loop
    return total

print(soma_dos_quadrados(5))

#R-1.5 Give a single command that computes the sum from Exercise R-1.4, relying on
#Python’s comprehension syntax and the built-in sum function.

def soma_dos_quadrados(num):
    print("Soma dos quadrados abaixo de", num)
    return sum(i**2 for i in range(num)) #mesma coisa que o anterior, mas faz a soma de i ao quadrado seguido do for

print(soma_dos_quadrados(4))

#R-1.6 Write a short Python function that takes a positive integer n and returns the sum of
#the squares of all the odd positive integers smaller than n.

def soma_dos_quadrados(num):
    print("soma dos quadrados abaixo de", num,":")
    num -=1 #tira um pra começar abaixo do numero escolhido
    total = 0 #variável auxiliar que retorna o total
    while num > 0:
        if num%2 != 0:
            total += num*num #adiciona ao total
            num-=1 #tira um do numero escolhido para continuar o loop
        else: num-=1
    return total

print(soma_dos_quadrados(7))

#R-1.7 Give a single command that computes the sum from Exercise R-1.6, relying on
#Python’s comprehension syntax and the built-in sum function.

def soma_dos_quadrados(num):
    print("Soma dos quadrados abaixo de ", num)
    return sum(i**2 for i in range(num) if i%2==1) #mesma coisa do  1.5 mas com a condicional de i%2==0

print(soma_dos_quadrados(7))

#R-1.12 Python’s random module includes a function choice(data) that returns a random
#element from a non-empty sequence. The random module includes a more basic function
#randrange, with parameterization similar to the built-in range function, that return a
#random choice from the given range. Using only the randrange function, implement your
#own version of the choice function.

import random
def meuRandom(data):
    return data[random.randrange(0, len(data) - 1)]

vetor = [1,2,3,4,5,6,7,8,9,10]
print(meuRandom(vetor))

#C-1.15 Write a Python function that takes a sequence of numbers and determines if all
#the numbers are different from each other (that is, they are distinct).

def numerosIguais(data):
    c = 0
    for i in range(len(data)-1):
        a = data[i]
        for j in range(i+1,len(data)):
            b = data[j]
            if a == b :
                c = 1
                break
        if c == 1:
            print('Sim, há numeros iguais')
            return
    print("Não há números iguais")

lista = [1,2,3,4,5,6,7,8,9]
numerosIguais(lista)

#C-1.24 Write a short Python function that counts the number of vowels in a given
#character string.

def contaVogais(frase):
    contador=0
    lista=list(frase)
    for i in lista:
        if i in ['a','e','i','o','u']:
            contador+=1
    return contador
print(contaVogais("Paralelo"))

#C-1.25 Write a short Python function that takes a string s, representing a sentence, and
#returns a copy of the string with all punctuation removed. For example, if given the string
#"Let s try, Mike.", this function would return "Lets try Mike".

string = "Let's try, mike."
lista = list(string);
pontuacoes = ''''~!@#$%^*()_-{}[]|\:'";<>,./'''
saida = ''

for i in string:
    if i not in pontuacoes:
        saida += i
print(saida)

#C-1.26 Write a short program that takes as input three integers, a, b, and c, from the
#console and determines if they can be used in a correct arithmetic formula (in the given
#order), like “a+b = c,” “a = b−c,” or “a ∗ b = c.”

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


############Questão Bônus############

#P-1.34 A common punishment for school children is to write out a sentence multiple
#times. Write a Python stand-alone program that will write out the following sentence one
#hundred times: “I will never spam my friends again.” Your program should number each
#of the sentences and it should make eight different random-looking typos.

from random import randrange

def spamDeFrases(n):
    sentence = "I will never spam my friends again."
    fraseAux = list(sentence)
    fraseAux2 = list(sentence)
    for i in range (n):
        if i % 12 == 0:
            localDeErro = randrange(0,(len(fraseAux2)-1))
            fraseAux.pop(localDeErro)
            str1 = ''.join(fraseAux)
            print(i , str1)
            fraseAux = list(sentence)
        else:

            print(i , sentence)

spamDeFrases(100)