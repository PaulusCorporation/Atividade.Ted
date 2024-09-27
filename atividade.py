notas = []

while True:

    nota = float(input("Digite a nota do aluno (ou digite -1 para encerrar): "))

    if nota == -1:
        break

    notas.append(nota)   

if len(notas) >0:

    media = sum(notas) / len(notas)
    print(f"A média das notas é: {media:.2f}")
else:
    print("nenhuma nota foi inserida.")               