from sys import stdin

inp = []

while True:
    L, P, V = map(int, stdin.readline().strip().split())

    if not L and not P and not V:
        break

    inp.append((L, P, V))


for i in range(len(inp)):
    L, P, V = inp[i]

    print(f'Case {i + 1}: {(V // P) * L + min(V % P, L)}')