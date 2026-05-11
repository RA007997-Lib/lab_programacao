import random

vetor = []
contador6 = 0

for i in range(50):
    dado = random.randint(1, 6)
    vetor.append(dado)

    if dado == 6:
        contador6 += 1

percentual = (contador6 / 50) * 100

print("Lançamentos:", vetor)
print("Quantidade de faces 6:", contador6)
print(f"Percentual: {percentual:.2f}%")