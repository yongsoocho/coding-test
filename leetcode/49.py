str_ = input().strip().split(",")

table = {}

for s in str_:
    if "".join(sorted(list(s))) in table:
        table["".join(sorted(list(s)))].append(s)
    else:
        table["".join(sorted(list(s)))] = [s]
        
print(table.values())