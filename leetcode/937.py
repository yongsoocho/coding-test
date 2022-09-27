logs = input().strip().split(",")

letters, digits = [], []

for l in logs:
    if l.split()[1].isalpha():
        letters.append(l)
    else:
        digits.append(l)

return sorted(letters, key=lambda x: (x.split()[1:], x.split()[0])) + digits