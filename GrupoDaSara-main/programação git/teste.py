import time
#Mostra a frase abaixo


""" 
Mostra 
a 
frase
abaixo 
"""


print("Bem-Vindo")
name = input("qual seu nome?")
print("Bem-Vindo,", name + "!")

print("Em que posso te ajudar?")
print("1-Queijo")
print("2-Água")
print("3-Leite")
print("4-Pão")

opcao = int(input("Digite a opção desejada")) 

if opcao == 1:
    print ("R$ 40,00/KG ")
elif opcao == 2:
    print ("R$ 3,50")
elif opcao == 3:
    print ("R$ 5,99")
elif opcao == 4:
    print ("R$ 0,70 uni/francês")


