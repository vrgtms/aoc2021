file = open('day3-input.txt', 'r')

gammaRate = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

while True:
    currentLine = file.readline()

    if not currentLine:
        file.close()
        break

    currentLine = list(currentLine[:-1])

    for index, currentBit in enumerate(currentLine):
        gammaRate[index] = gammaRate[index] + (-1 if int(currentBit) == 0 else 1)

gammaRate = list(map(lambda x : '1' if x > 0 else '0', gammaRate))
epsilonRate = list(map(lambda x : '0' if x == '1' else '1', gammaRate))

gammaRate = ''.join(gammaRate)
epsilonRate = ''.join(epsilonRate)

gammaRate = int(gammaRate, 2)
epsilonRate = int(epsilonRate, 2)

print("The power consumption is: {}".format(gammaRate * epsilonRate))