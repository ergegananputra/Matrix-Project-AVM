from matrix import Matrix, Operasi_Baris_Elementer

matrix : Matrix = Operasi_Baris_Elementer()
matrix.createMatrix(3, 3, type=int)
matrix.findDeterminanMatrix()
matrix.displayBeforeAfter()
print(f"determinan matrix adalah {matrix.findDeterminanMatrix()}")