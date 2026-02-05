nome = input("Digite seu nome: ")

quantidade = (int(input("Quantas notas deseja inserir: ")))
notas = []

for i in range(quantidade): #Isso é uma lista
   item = float(input(f"Digite a nota {i+1}: "))
   notas.append(item)

media = sum(notas) / len(notas)
maior = max(notas)
menor = min(notas)

print("-" * 30 ) #linha separadora

print("Aluno: ", nome)
print("Suas notas são: ", notas)
print("Sua média é: ", round(media,2))
print("Sua maior nota é: " , maior)
print("Sua menor nota é: " , menor)

if media < 6 :
 print("Situação: Reprovado")

else:
    print("Situação: Aprovado")