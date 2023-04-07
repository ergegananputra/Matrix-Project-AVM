'''
Cara Run program
Run in terminal, copy text dibawah ini (ctrl+c) :
& "d:/#Universitas Gadjah Mada/#Kelas/Aljabar Vector Matrix/Pertemuan 7/Matrix/.venv/Scripts/python.exe" "d:/#Universitas Gadjah Mada/#Kelas/Aljabar Vector Matrix/Pertemuan 7/Matrix/src/test_program.py"


Format input createMatrix
contoh:
matrix 2 x 2
baris ke-1 : 2 3
baris ke-2 : 3 2

'''

from matrix import Matrix, Operasi_Baris_Elementer, Cofactor_Expansion_Determinan

# myMatrix = [
#     [0,  1, 5],
#     [3, -6, 9],
#     [2,  6, 1]
# ]

myMatrix = [
    [0,  3, 2, 4],
    [1, -6, 6, 5],
    [4, 4, 4, 9],
    [5,  0, 1, 6]
]


matrix : Matrix = Operasi_Baris_Elementer()
# matrix.createMatrix(2, 2, type=int)
matrix.createInstantMatrix(myMatrix)
matrix.findDeterminanMatrix()
matrix.displayBeforeAfter()
print(f"determinan matrix adalah {matrix.findDeterminanMatrix()}")

print("\n Perhitungan dengan cara Cofactor Expansion\n")

matrix : Matrix = Cofactor_Expansion_Determinan()
matrix.createInstantMatrix(myMatrix)
matrix.display(title="Matrix solve with Cramer")    # Contoh pakai display()
matrix.findDeterminanMatrix()
print(f"determinan matrix adalah {matrix.findDeterminanMatrix()}")

