from collections import defaultdict
from pprint import pprint
from typing import List


def isValidSudoku(board: List[List[str]]) -> bool:

    def validate_row():
        """ Get the row """
        board_dict_row = dict()
        for index, row in enumerate(board, start=1):
            board_dict_row[index] = ''.join(row).replace('.', '')
        return all([len(set(v)) == len(v) for _, v in board_dict_row.items()])

    def validate_column():
        """ Get column """
        board_dict_column = dict()
        for i in range(9):
            value = ''
            for row in board:
                value += row[i]
            board_dict_column[i + 1] = ''.join(value).replace('.', '')
        return all([len(set(v)) == len(v) for k, v in board_dict_column.items()])

    def validate_3x3_box():
        """ Get 3x3 box """
        box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9 = '','','','','','','','',''
        result = []

        for i in range(0, 9, 3):
            for index, j in enumerate(board):
                if i == 0 and index in range(0, 3):
                    box_1 += ''.join(j[i:i + 3]).replace('.', '')
                if i == 0 and index in range(3, 6):
                    box_2 += ''.join(j[i:i + 3]).replace('.', '')
                if i == 0 and index in range(6, 9):
                    box_3 += ''.join(j[i:i + 3]).replace('.', '')

                if i == 3 and index in range(0, 3):
                    box_4 += ''.join(j[i:i + 3]).replace('.', '')
                if i == 3 and index in range(3, 6):
                    box_5 += ''.join(j[i:i + 3]).replace('.', '')
                if i == 3 and index in range(6, 9):
                    box_6 += ''.join(j[i:i + 3]).replace('.', '')

                if i == 6 and index in range(0, 3):
                    box_7 += ''.join(j[i:i + 3]).replace('.', '')
                if i == 6 and index in range(3, 6):
                    box_8 += ''.join(j[i:i + 3]).replace('.', '')
                if i == 6 and index in range(6, 9):
                    box_9 += ''.join(j[i:i + 3]).replace('.', '')
        result += [box_1, box_2, box_3, box_4, box_5, box_6, box_7, box_8, box_9]
        return all([len(set(k)) == len(k) for k in result])

    return validate_row() and validate_column() and validate_3x3_box()



board_1 = [["5","3",".",".","7",".",".",".","."]
            ,["6",".",".","1","9","5",".",".","."]
            ,[".","9","8",".",".",".",".","6","."]
            ,["8",".",".",".","6",".",".",".","3"]
            ,["4",".",".","8",".","3",".",".","1"]
            ,["7",".",".",".","2",".",".",".","6"]
            ,[".","6",".",".",".",".","2","8","."]
            ,[".",".",".","4","1","9",".",".","5"]
            ,[".",".",".",".","8",".",".","7","9"]]

board_2 = [["8","3",".",".","7",".",".",".","."]
            ,["6",".",".","1","9","5",".",".","."]
            ,[".","9","8",".",".",".",".","6","."]
            ,["8",".",".",".","6",".",".",".","3"]
            ,["4",".",".","8",".","3",".",".","1"]
            ,["7",".",".",".","2",".",".",".","6"]
            ,[".","6",".",".",".",".","2","8","."]
            ,[".",".",".","4","1","9",".",".","5"]
            ,[".",".",".",".","8",".",".","7","9"]]

board_3 = [[".",".",".",".","5",".",".","1","."]
            ,[".","4",".","3",".",".",".",".","."]
            ,[".",".",".",".",".","3",".",".","1"]
            ,["8",".",".",".",".",".",".","2","."]
            ,[".",".","2",".","7",".",".",".","."]
            ,[".","1","5",".",".",".",".",".","."]
            ,[".",".",".",".",".","2",".",".","."]
            ,[".","2",".","9",".",".",".",".","."]
            ,[".",".","4",".",".",".",".",".","."]]

print(isValidSudoku(board_1))
print(isValidSudoku(board_2))
print(isValidSudoku(board_3)) #false