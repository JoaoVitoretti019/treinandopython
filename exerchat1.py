nome = input("Digite seu nome: ")
nota1 = (float(input("Digite sua primeira nota: ")))
nota2 = (float(input("Digite sua segunda nota: ")))
nota3 = (float(input("Digite sua terceira nota: ")))

soma = nota1 + nota2 + nota3  
resultado = soma / 3

if resultado < 6 :
 print(nome, "você foi reprovado com nota", resultado)

else:
    print(nome, "você foi aprovado! Sua nota foi", resultado)

