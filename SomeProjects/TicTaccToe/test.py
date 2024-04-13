boar = [i for i in range(9)]
print(boar)
square = 7
col_idx = square % 3
column = [boar[col_idx + i * 3] for i in range(3)]

print(column)