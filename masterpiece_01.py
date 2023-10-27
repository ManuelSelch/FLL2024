limit = 10

img = [[1 for x in range(limit)] for y in range(limit)] 

newImg = [[0 for x in range(limit)] for y in range(limit)] 

count = 1
for y in range(limit):
    for x in range(limit):
        count += 1
        img[y][x] = count


def getNewX(x):
    newX = x*3
    newX %= limit 
    return newX
def getNewY(y):
    newY = y*3
    newY %= limit 
    return newY



for y in range(limit):
    for x in range(limit):
        newX = getNewX(x)
        newY = getNewY(y)
        newImg[newY][newX] = img[y][x]
        print(str(x)+"|"+str(y) + " -> " + str(newX) + "|" + str(newY))

print("---")

for y in range(limit):
    row = ""
    for x in range(limit):
        row += "\033["+str(newImg[y][x])+"m" + str(newImg[y][x])
    print(row)
