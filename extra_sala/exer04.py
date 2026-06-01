
notas = []
#ler notas
for i in range(5):
    nota = float(input("Digite uma nota"))
    notas.append(nota)   

menor = min(notas)
notas.remove(menor)

print(f"Listas com as notas {notas}")
print(f"Essa foi a menor nota {menor}")