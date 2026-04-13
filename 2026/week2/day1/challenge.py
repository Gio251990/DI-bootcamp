MATRIX_STR = '''
7ir
Tsi
h%x
i ?
sM# 
$a 
#t%'''

matrix = [list(row) for row in MATRIX_STR.splitlines() if row]

decoded = ""

rows = len(matrix)
cols = len(matrix[0])

for col in range(cols):
    for row in range(rows):
        char = matrix[row][col]
        decoded += char

filtered = ""
for c in decoded:
    if c.isalpha():
        filtered += c
    else:
        filtered += " "

final_message = " ".join(filtered.split())

print(final_message)