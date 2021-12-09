file = open('day2-input.txt', 'r')

horizontalPosition = 0
depth = 0

while True:
    currentLine = file.readline()

    if not currentLine:
        file.close()
        break

    currentLine = currentLine.split(' ')

    currentDirection = currentLine[0]
    currentDistance = int(currentLine[1])

    if currentDirection == 'forward':
        horizontalPosition = horizontalPosition + currentDistance
    elif currentDirection == 'down':
        depth = depth + currentDistance
    elif currentDirection == 'up':
        depth = depth - currentDistance

print("The product of the final depth and horizontal position is {}".format(depth * horizontalPosition))