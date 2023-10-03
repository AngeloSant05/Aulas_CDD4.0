A = [2, 10, 3, 11, 4, 12, 5, 13, 6, 14]

M = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

X = float(input("Digite o valor pelo qual quer multiplicar: "))

for i in range(10):
    M[i] = A[i] * X

print(M)
