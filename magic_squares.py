# DailyProgrammer [2016-04-04] Challenge #261 [Easy] verifying 3x3 magic squares
# @author Brian McEntee

# Class Definitions
class SquareMatrix(object) :

    def __init__(self, size, matrix) :
        self.size = size
        if self.is_square(matrix) :
            self.matrix = matrix
        else :
            print "Error: matrix must be a square, size x size"
            self.matrix = [[0]] # 1 x 1 default matrix

    def is_square(self, matrix) :
        is_square = True
        for row in matrix :
            if len(row) != len(matrix) :
                is_square = False
                break
        return is_square

    def is_magic(self) :
        if self.rows_magic() and self.cols_magic() and self.diags_magic() :
            return True
        else :
            return False

    def rows_magic(self) :
        is_magic = True
        i = 0
        for row in self.matrix :
            # print "Row", (i + 1), "\b:", sum(row)
            if sum(row) != 15 :
                is_magic = False
                break
            i += 1
        return is_magic

    def cols_magic(self) :
        is_magic = True
        for col in range(self.size) :
            col_sum = 0
            for row in self.matrix :
                col_sum+= row[col]
            # print "Column", (col + 1), "\b:", col_sum
            if col_sum != 15 :
                is_magic = False
                break
        return is_magic

    def diags_magic(self) :
        is_magic = True
        tlbr_sum = trbl_sum = 0
        tlbr_index = 0
        trbl_index = len(self.matrix) - 1
        for row in self.matrix :
            tlbr_sum += row[tlbr_index]
            trbl_sum += row[trbl_index]
            tlbr_index += 1
            trbl_index -= 1
        # print "Diag1 sum: ", tlbr_sum
        # print "Diag2 sum: ", trbl_sum
        if tlbr_sum != 15 or trbl_sum != 15 :
            is_magic = False
        return is_magic



    def print_mx(self) :
        """Print the contents of the matrix in rows and columns."""
        for row in self.matrix :
            for elem in row :
                print elem,
            print
# End Square Matrix

# Main currently for testing 
def main() :
    mx_1 = [['x00','x01','x02'],['x10','x11','x12'],['x20','x21','x22']]
    mx_2 = [['x00','x01','x02'],['x10','x11'],['x20','x21','x22']]
    sm_1 = SquareMatrix(3,mx_1)
    sm_2 = SquareMatrix(3,mx_2)
    sm_3 = SquareMatrix(3, [[8, 1, 6], [3, 5, 7], [4, 9, 2]] )
    sm_4 = SquareMatrix(3, [[2, 7, 6], [9, 5, 1], [4, 3, 8]] )
    sm_5 = SquareMatrix(3, [[3, 5, 7], [8, 1, 6], [4, 9, 2]] )
    sm_6 = SquareMatrix(3, [[8, 1, 6], [7, 5, 3], [4, 9, 2]] )

    print sm_3.is_magic()
    print sm_4.is_magic()
    print sm_5.is_magic()
    print sm_6.is_magic()

if __name__ == "__main__" :
    main()