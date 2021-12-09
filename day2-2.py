file = open('day2-input.txt', 'r')

horizontalPosition = 0
depth = 0
aim = 0

while True:
    currentLine = file.readline()

    if not currentLine:
        file.close()
        break

    currentLine = currentLine.split(' ')

    currentDirection = currentLine[0]
    currentValue = int(currentLine[1])

    if currentDirection == 'forward':
        horizontalPosition = horizontalPosition + currentValue
        depth = depth + aim * currentValue
    elif currentDirection == 'down':
        aim = aim + currentValue
    elif currentDirection == 'up':
        aim = aim - currentValue

print("The product of the final depth and horizontal position is {}".format(depth * horizontalPosition))