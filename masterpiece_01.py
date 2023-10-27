img = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

newImg = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

xLimit = 3
yLimit = 3

def getNewX(x):
    newX = x*2
    newX %= xLimit 
    return newX
def getNewY(y):
    newY = y*2
    newY %= yLimit 
    return newY



for y in range(3):
    for x in range(3):
        newX = getNewX(x)
        newY = getNewY(y)
        newImg[newY][newX] = img[y][x]
        print(str(x)+"|"+str(y) + " -> " + str(newX) + "|" + str(newY))

for row in newImg:
    print(row)
