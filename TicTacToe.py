"""
Tic Tac Toe Python Script
By Jason Lee
"""
import random
import time

board = """ --- --- --- 
|   |   |   |
 --- --- --- 
|   |   |   |
 --- --- --- 
|   |   |   |
 --- --- ---
 """

board_list = [ " --- --- --- ", "\n| ", " "," | ", " ", " | ", " ", " |",
               "\n --- --- --- ", "\n| ", " "," | ", " ", " | ", " ", " |"
               "\n --- --- --- ", "\n| ", " "," | ", " ", " | ", " ", " |"
               "\n --- --- --- ", ""]

# This Tracks Available Spots:
available = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def convertRowColumn(row, column)
    if row == 1:
        if column == 1:
            return 1
        if column == 2:
            return 2
        if column == 3:
            return 3
    if row == 2:
        if column == 1:
            return 4
        if column == 2:
            return 5
        if column == 3:
            return 6
    if row == 3:
        if column == 1:
            return 7
        if column == 2:
            return 8
        if column == 3:
            return 9

def newBoard(x, team=1):
    def Draw(x, team=1):
        listToStr = ''.join([str(elem) for elem in board_list])
        if team == 1:
            figure = 'X'
        if team == 2:
            figure = 'O'
        if x = 1
            board_list.pop(2)
            board_list.insert(2, figure)
            available.remove(1)
            return board_list
        if x = 2:
            board_list.pop(4)
            board_list.insert(4, figure)
            available.remove(2)
            return board_list
        if x = 3:
            board_list.pop(6)
            board_list.insert(6, figure)
            available.remove(3)
            return board_list
        if x = 4:
            board_list.pop(10)
            board_list.insert(10, figure)
            available.remove(4)
            return board_list
        if x = 5:
            board_list.pop(12)
            board_list.insert(12, figure)
            available.remove(5)
            return board_list
        if x =6:
            board_list.pop(14)
            board_list.insert(14, figure)
            available.remove(6)
            return board_list
        if x = 7:
            board_list.pop(17)
            board_list.insert(17, figure)
            available.remove(7)
            return board_list
        if x = 8:
            board_list.pop(19)
            board_list.insert(19, figure)
            available.remove(8)
            return board_list
        if x = 9:
            board_list.pop(21)
            board_list.insert(21, figure)
            available.remove(9)
            return board_list
    def listToStr(x):
        return ''.join([str(elem) for elem in x])
    return listToStr(Draw(row, column, team))

# Actual Script part:
moves = 0
print(board)
while moves <= 8:
    if moves % 2 == 0:
        team = 2
    else:
        team = 1
    print('Where would you to put your figure (x)?')
    row = int(input('Row Number: '))
    column = int(input('Column Number: '))
    time.sleep(1)
    print(newBoard(row, column, team))
    print(available)
    moves += 1
print('No more moves left. Sorry gamer.')
