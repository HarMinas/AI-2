
'''
    The program Reqs
    >Officers cannot be on the same row, column with each other
    >Officers cannot move
    >Act points are collected when officer and scooter are on the same location
    >grid is indexed starting from upper left corner with rows being the y coord

    Formatting of the input file
    First line: 32 bit int n the side of the city area = nxn
    Second line : p - the number of police officers
    Third line: The number of scooters s
    Next:: s*12 lines the list of scooter x,y coords over time, separated with end of line (LF). 
            With s scooters and 12 timesteps in a day, this results in 12 coords per scooter
'''
'''
    there are squares that are always mutually exclusive
'''


class Block:
    x = 0
    y = 0
    value = 0
    def __init__(self, x, y, value):
        self.x = x
        self.y = y
        self.value = value

#openning the input file
file = open("input.txt", "r")

#parsing the input file
gridSide = int(file.readline()) 
numOfficers = int(file.readline())
numScooters = int(file.readline())
numOfTimes = 12
scootersLeft = numScooters
totalPosForScooters = numOfTimes * numScooters

#initializing the board with n rows and n cols with 0 scores for each block
board = [[0] * gridSide for i in range(gridSide)]
validBoard = [[True] * gridSide for i in range(gridSide)]


#iterating over the file to add the scores to the board. The score of the block is incremented if
#the a scooter will be on that block
for i in range(totalPosForScooters):
    line = file.readline()
    sepLine = line.split(",")
    x = int(sepLine[0])
    y = int(sepLine[1].split("\r\n")[0])
    board[x][y] = board[x][y] + 1

#closing the file
file.close  


#Creating a list to store the block objects in
sortedList = []
for i in range(gridSide):
    for j in range(gridSide):
        sortedList.append(Block(i, j, board[i][j]))
        


#Sorting the List
sortedList.sort(key = lambda x: x.value, reverse = True)



def getValidMoves(array, b):
    newArr = []
    for i in array:

        if i.x != b.x and i.y != b.y and (abs(b.y - i.y) != abs(b.x - i.x)) :
            newArr.append(i)

    return newArr



#This functon takes an array














def getMax2(offCount, tot, array, totalSum):

    if offCount == 0:
        return tot

    for block in array:
        maximum = tot + block.value
        validMoves = getValidMoves(array, block)
        validMovesLen = len(validMoves)
        
        #This is the case if there are more officers than valid moves
        if validMovesLen < offCount:
            return -1
        #This is the case if there are still valid moves left  and available officers
        if validMovesLen > 0:
            maximum = getMax2(offCount - 1, maximum, validMoves, totalSum)
            if maximum == -1:
                maximum = 0
                continue
            elif maximum > totalSum:
                totalSum = maximum
                maximum = 0
                continue
            elif maximum < totalSum: 
                break
        maximum = 0
    return totalSum



totalSum = 0
offLeft = numOfficers
tempSum = 0
output = getMax2(offLeft,tempSum, sortedList, totalSum)



outputf = open('output.txt', 'w+')
outputf.write(str(output))
outputf.close
