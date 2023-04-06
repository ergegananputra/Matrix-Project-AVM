'''
Sebuah module Matrix
Matrix Kelompok 3 Aljavar Linear Matrix
oleh:
    - Adiel Boanerge G
    - Sena Aji Bayu M
    - Risma S
'''

class Matrix:
    """class yang digunakan untuk menampilkan dan membuat matrix

    ### Methods
    - createMatrix() -> void
    - getRow() -> int
    - getColumn() -> int
    - getMatrix() -> list matrix
    - display() -> void
    """

    def __init__(self):
        self.__matrix = []
        self.__row    : int = 0
        self.__column : int = 0
    
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
    
    def getRow(self) -> int | float:
        """ Mengembalikan nilai banyak baris suatu matrix"""
        return self.__row

    def getColumn(self) -> int | float:
        """ Mengembalikan nilai banyak kolom suatu matrix"""
        return self.__column
    
    def getMatrix(self) -> list:
        """ Mengembalikan salinan nilai list suatu matrix"""
        return self.__matrix.copy()
    
    def display(self, matrix : list = [], decoration : str = "", coefficient = 1) -> None:
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
                    print(div, end="\t")
                print(decoration)
                index += 1


class MyMath:
    """ Kelas Matematika untuk pembagian dan menyederhanakan nilai elemen baris matrix"""
    def division(self, x1, x2, precision : float = 0.0000000001):
        try:
            result = x1 / x2
            if precision > result % 1 > -1*precision:
                result = int(result)
                return result
            else:
                return x1 / x2
        except ZeroDivisionError as e:
            raise ZeroDivisionError(f"{x1} / {x2}")
        
    def roundRow(self, Row) -> list:
        tempRow = []
        for col in Row:
            if 0.0000000001 > col % 1 > -0.0000000001:
                tempRow.append(int(col))
            else:
                tempRow.append(round(col, 3))
        return tempRow


class Operasi_Baris_Elementer(Matrix, MyMath):
    def __init__(self):
        super().__init__()
        self.__queue = []
        self.matrix : list = []
        self.k = 1
    
    def clearQueue(self):
        """Menghapus queue.
        
        Belum Di implementasikan
        """
        self.__queue = []
    
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
        """Mencari Matrix elementer
        
        #### Raise
        - ##### ZeroDivisionError
            dapat terjadi ketika memanggil method zero_interchange_diagonal sebelum
            melakukan operasi OBE, dan pembagian di dalamnya
        """
        self.matrix : list = super().getMatrix()
        self.zero_interchange_diagonal()
        for row in range(super().getRow()):
            self.zeroLeft(row)
        for row in range(super().getRow()):
            self.zeroRight(row)

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
        #### Return
            mengembalikan nilai determinan
        """
        self.Operasi_Baris_Elementer()
        determinan = self.k
        for i in range(super().getRow()):
            determinan *= self.matrix[i][i]
        return determinan
        


