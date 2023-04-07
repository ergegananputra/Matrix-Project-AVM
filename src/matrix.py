'''
Sebuah module Matrix
Matrix Kelompok 3 Aljavar Linear Matrix
oleh:
    - Adiel Boanerge G
    - Sena Aji Bayu M
    - Risma S
'''

from dataclasses import dataclass

@dataclass
class Matrix:
    """class yang digunakan untuk menampilkan dan membuat matrix
    ### Atributes
    - matrix, list dalam list.
    - row, banyak baris suatu matrix
    - column, banyak kolom suatu matrix
    - coefficient, koefisien suatu matrix

    ### Methods
    - createMatrix() -> void
    - createInstantMatrix() -> void
    - getRow() -> int
    - getColumn() -> int
    - getMatrix() -> list matrix
    - display() -> void
    """

    def __init__(self):
        self.__matrix = []
        self.__row    : int = 0
        self.__column : int = 0
        self.__coefficient = 1
    
    def updateCoefficient_by(self, value : int | float = 1):
        """Mengkalikan koefisien dengan suatu value. 

        #### Warning!
        Value 0 adalah untuk mereset koefisien"""
        self.__coefficient *= value
    
    def getCoefficient(self):
        return self.__coefficient
    
    def createMatrix(self, row : int = 0, column : int= 0, fill : float | int = None, type : object = float):
        '''Membuat matrix

        ### Parameters
        - #### row : int 
            Menentukan banyak baris suatu matrix
        - #### column : int
            menentukan banyak kolom suatu matrix
        - #### fill : float | int
            Mengisi matrix secara otomatis dengan nilai fill. 
            Secara default fill bernilai None yang mengharuskan mengisi secara manual melalui terminal.
        - #### type : object <- [int, float]
            Menetapkan apakah nilai dari elemen matrix berupa integer atau float. 
            Secara default type bernilai class float.

        ### Contoh :
        createMatrix(row=3, column=3, fill=0, type=int) \n
        akan terbentuk matrix 3x3 dengan isi semua elemen bernilai 0 
        '''
        if type not in [int, float]:
            type = float
        try:
            if fill == None:
                print(f"\nMembuat Matrix {row}*{column}!\n")
                self.__matrix = [ [type(x) for x in input(f"Baris ke-{row_index} : ").split()[:column]] for row_index in range(row) ]
            else:
                self.__matrix = [ [fill for _ in range(column)] for _ in range(row)]
        except ValueError as e:
            raise Exception(e)
        except:
            raise Exception
        finally:
            self.__row    = row
            self.__column = column
    
    def createInstantMatrix(self, matrix = [[]]):
        '''Membuat Matrix secara instant dengan memberikan array matrix'''
        if isinstance(matrix, list):
            self.__matrix = matrix
            self.__row = len(matrix)
            self.__column = len(matrix[0])
        
        elif isinstance(matrix, Matrix):
            self.__matrix = matrix.getMatrix()
            self.__row = matrix.getRow()
            self.__column = matrix.getColumn()

    
    def getRow(self) -> int | float:
        """ Mengembalikan nilai banyak baris suatu matrix"""
        return self.__row

    def getColumn(self) -> int | float:
        """ Mengembalikan nilai banyak kolom suatu matrix"""
        return self.__column
    
    def getMatrix(self) -> list:
        """ Mengembalikan salinan nilai list suatu matrix"""
        return self.__matrix.copy()
    
    def display(self, matrix : list = [], decoration : str = "", coefficient = 1, digitShow = 3) -> None:
        """ Menampilkan matrix ke dalam terminal dengan dekorasi dan nilai koefisien
        
        #### Parameters
        - ##### matrix : list
            Matrix yang ingin ditampilkan. Jika tidak diberikan maka akan menggunakan matrix
            yang ada di dalam kelas Matrix.
        - ##### decoration : str
            Decoration adalah dekorasi penampilan matrix. 
            Dekorasi akan ditampilkan di ujung kiri dan ujung kanan isi matrix.
            Contoh input decoration = " | "
        - #### coefficient : double | int
            Coefficient adalah koefisien matrix yang akan ditampilkan di bagian kiri matrix
            sebelum dekorasi.
            Contoh input coefficient = -4 
        - #### digitShow : int
            digitShow digunakan untuk berapa banyak n-digit yang ditampilkan. Hal ini tidak merubah
            nilai matrix
        """
        if matrix == []:
            matrix = self.getMatrix()
        
        if coefficient == 1:
            for row in matrix:
                print(decoration, end="\t")
                for div in row:
                    print(div, end="\t")
                print(decoration)
        else:
            index = 0
            center = self.__row // 2
            coefficient = str(coefficient)
            space = " " * (len(coefficient) + 1)
            for row in matrix:
                if index == center:
                    print(coefficient, end=" ")
                    print(decoration, end="\t")
                else:
                    print(space, end="")
                    print(decoration, end="\t")

                for div in row:
                    print(round(div, digitShow), end="\t")
                print(decoration)
                index += 1

    

class MyMath:
    """ Kelas Matematika untuk pembagian dan menyederhanakan nilai elemen baris matrix"""
    def division(self, x1, x2, precision : float = 0.0000000001):
        result = x1 / x2
        if precision > result % 1 > -1*precision:
            result = int(result)
            return result
        else:
            return x1 / x2
        
    def roundRow(self, Row, precision : float = 0.0000000001) -> list:
        tempRow = []
        for col in Row:
            # if precision > col % 1 > -1 * precision:
            #     tempRow.append(int(col))
            # else:
            #     tempRow.append(round(col, 3))
            tempRow.append(self.division(col, 1, precision))
        return tempRow


class Operasi_Baris_Elementer(Matrix, MyMath):
    """Kelas ini melakukan operasi baris elementer"""
    def __init__(self):
        super().__init__()
        self.matrix : list = []
        self.k = 1
    
    def zeroLeft(self, columnDiv : int) -> None:
        """Membuat elemen yang ada di kiri elemen menjadi bernilai 0.
        
        #### Raise
        - ##### ZeroDivisionError
            dapat terjadi ketika memanggil method zero_interchange_diagonal
            untuk mencari pembagi yang tidak 0 atau pembagi di method division
            sama dengan 0
        """
        headRow = self.matrix[columnDiv]
        if headRow == 0:
            self.zero_interchange_diagonal(startIndex=columnDiv)
            headRow = self.matrix[columnDiv]
        for row in range(columnDiv + 1, super().getRow()):
            toZeroConstant = super().division(self.matrix[row][columnDiv] , headRow[columnDiv])
            newRow = super().roundRow([self.matrix[row][x] - headRow[x] * toZeroConstant for x in range(super().getRow())])
            self.matrix[row] = newRow
    
    def zeroRight(self, columnDiv : int) -> None:
        """Membuat elemen yang ada di kanan elemen menjadi bernilai 0.
        
        #### Raise
        - ##### ZeroDivisionError
            dapat terjadi ketika pembagi di division sama dengan 0
        """
        columnDiv = super().getRow() - columnDiv - 1
        headRow = self.matrix[columnDiv]
        if headRow == 0:
            headRow = self.matrix[columnDiv]
        for row in range(columnDiv - 1, -1, -1):
            toZeroConstant = self.division(self.matrix[row][columnDiv] , headRow[columnDiv])
            newRow = super().roundRow([self.matrix[row][x] - headRow[x] * toZeroConstant for x in range(super().getRow())])
            self.matrix[row] = newRow
    
    def Operasi_Baris_Elementer(self) -> None:
        """Mencari Matrix elementer Triangular
        
        #### Raise
        - ##### ZeroDivisionError
            dapat terjadi ketika memanggil method zero_interchange_diagonal sebelum
            melakukan operasi OBE, dan pembagian di dalamnya
        """
        self.matrix : list = super().getMatrix()
        self.zero_interchange_diagonal()
        for row in range(super().getRow()):
            self.zeroLeft(row)
        

    def zero_interchange_diagonal(self, startIndex = 0) -> None:
        """Memindahkan elemen diagonal matrix yang memiliki nilai 0 dengan cara
        menukarkan baris yang ada dibawahnya sampai elemen tersebut tidak bernilai 0.
        Jika tidak ada nilai 0 maka akan melempar exception
        #### raise
        ##### ZeroDivisionError
        """
        for i in range(startIndex, super().getRow()):
            if self.matrix[i][i] == 0:
                temp = self.matrix[i]
                a = i + 1
                while self.matrix[i][i] == 0 and a < super().getRow():
                    if self.matrix[a][i] != 0:
                        self.matrix[i] = self.matrix[a]
                        self.matrix[a] = temp
                        temp = self.matrix[i]
                        self.k *= -1
                    a += 1
                if self.matrix[i][i] == 0:
                    print("error: currently not solvable")
                    raise ZeroDivisionError.add_note("error: currently not solvable")
    
    def display(self, matrix: list = [], Coefficient = 1, title = "") -> None:
        """ Menampilkan matrix ke dalam terminal dengan dekorasi dan nilai koefisien didahului dengan judul.
        #### Notes:
        method dislay akan mengirimkan parameter ke superclass nya dan tidak melakukan di dalam method ini.
        
        #### Parameters
        - ##### matrix : list
            Matrix yang ingin ditampilkan. Jika tidak diberikan maka akan menggunakan matrix
            yang ada di dalam kelas Matrix.
        - #### coefficient : double | int
            Coefficient adalah koefisien matrix yang akan ditampilkan di bagian kiri matrix
            sebelum dekorasi.
            Contoh input coefficient = -4 
        - ##### title : str
            Memberikan judul sebelum matrix di tampilkan.
        """
        print(title)
        return super().display(matrix, decoration="|", coefficient=Coefficient)

    def displayBeforeAfter(self):
        """Menampilkan matrix awal dan matrix elementer"""
        print()
        self.display(title="Matrix Awal")
        print()
        self.display(self.matrix, self.k, title="Matrix Elementer")

    def findDeterminanMatrix(self):
        """Mencari determinan suatu matrix
        #### Variablles:
        - k = coefficient suatu matrix
        - determinan (local) = nilai determinan

        #### Return
            mengembalikan nilai determinan
        """
        self.k = 1
        self.Operasi_Baris_Elementer()
        determinan = self.k
        for i in range(super().getRow()):
            determinan *= self.matrix[i][i]
        return super().division(determinan, 1)    # Melakukan pembulatan
        

class Cofactor_Expansion_Determinan(Operasi_Baris_Elementer):
    """Kelas untuk mencari determinan menggunakan Cofactor Expansion.
    Kelas ini merupakan child dari class Operasi_Baris_Elementer.
    Kelas ini menggunakan konsep queue untuk membuat ekspansi mencapai matrix 2x2.
    
    #### Methods:
    - enqueue()
    - dequeue()
    - inversion()
    - cofactorExpansion()
    - findDeterminanMatrix()
    """
    def __init__(self):
        super().__init__()
        self.__queue : list[Matrix] = []
        self.__determinan = 0
    
    def enqueue(self, matrix : Matrix):
        self.__queue.insert(0, matrix)
    
    def dequeue(self) -> Matrix:
        return self.__queue.pop()
    
    def inversion(self, i : int, j: int):
        """Menghitung nilai inversi"""
        return 1 if (i+j)%2 == 0 else -1

    def cofactorExpansion(self, row_cofactor : int = 0):
        """Mencari determinan menggunakan Ekspansi Kofaktor
        
        #### Parameter
        - row_cofactor = baris dimana Minors dibuat
        """
        temp_matrix : Matrix = Matrix()
        temp_matrix.createInstantMatrix(super().getMatrix())
        self.enqueue(temp_matrix)

        while self.__queue != []:
            if self.__queue != []:
                matrix_now : Matrix = self.dequeue()

                if row_cofactor >= matrix_now.getRow():
                    row_cofactor -= 1

            if matrix_now.getRow() > 2 :
                
                # Membuat Matrix Minors, Inversion dan Minor Entry
                for column_cofactor in range(matrix_now.getColumn()):
                    new_matrix : Matrix = Matrix()
                    new_matrix.updateCoefficient_by(matrix_now.getMatrix()[row_cofactor][column_cofactor])    # Minor Entry
                    new_matrix.updateCoefficient_by(self.inversion(row_cofactor, column_cofactor))    # Inversion
                    new_matrix.updateCoefficient_by(matrix_now.getCoefficient())    # Menurunkan koefisien sebelumnya

                    # Matrix Minors
                    __temp__matrix = []
                    for i in range(matrix_now.getRow()):
                        if i == row_cofactor:
                            continue
                        
                        __temp__row = []
                        for j in range(matrix_now.getColumn()):
                            if j == column_cofactor:
                                continue
                            
                            __temp__row.append(matrix_now.getMatrix()[i][j])
                        
                        __temp__matrix.append(__temp__row)
                    
                    new_matrix.createInstantMatrix(__temp__matrix)
                    self.enqueue(new_matrix)
            
            else:
                # Menghitung Determinan Matrix 2 x 2
                self.__determinan += (matrix_now.getMatrix()[0][0] * matrix_now.getMatrix()[1][1] \
                                    - matrix_now.getMatrix()[0][1] * matrix_now.getMatrix()[1][0]) \
                                    * matrix_now.getCoefficient()
       

    def findDeterminanMatrix(self, MinorsRow : int = None):
        """Mencari determinan menggunakan Cofactor Expansion.

        #### Parameters
        - MinorsRow, merupakan i dari Mij. i dimulai dari index 1
        
        #### Override method
        - from child class : Cofactor_Expansion_Determinan
        """
        self.__determinan = 0
        self.coefficient = 1

        if MinorsRow == None:
            self.cofactorExpansion()
        else:
            self.cofactorExpansion(MinorsRow-1)

        return self.__determinan

    

        

