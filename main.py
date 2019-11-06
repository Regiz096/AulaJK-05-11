
#nome a se escrever para realizar o exercicio
pessoaNome = input("Nome da pessoa:")

#numero para determinar o primeiro elemento da "soma"
a = input("primeiro numero:") 
#nuemro para determinar o segundo elemento da "soma"
b = input("segundo numero:") 

#variavel para soma de 2 numeros
soma = a +b

#funçao para revelar se e verdadeiro ou falso
if(soma > a): # para ver se "soma" é maior que "a"
    print(pessoaNome + ",A soma e maior que a")
elif(soma == a):# para ver se "soma" e igual a "a"
    print(pessoaNome +",A soma e igual a a ")
else:# para ver se "soma" e menor que "a"
    print(pessoaNome + ",A soma e menor que a")
        
#mostra a primeira , segunda e ultima linha do nome descrito
print("A primeira letra do nome e " + pessoaNome[0])
print ("A segunda letra do nome e " + pessoaNome[1])
print("A ultima letra do nome e " + pessoaNome[4])
    