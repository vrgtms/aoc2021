file = open('day1-input.txt', 'r')

measurementLargerCount = 0

lastMeasurement = int(file.readline())

while True:
    currentMeasurement = file.readline()

    if not currentMeasurement:
        break

    currentMeasurement = int(currentMeasurement)

    if currentMeasurement > lastMeasurement:
        measurementLargerCount = measurementLargerCount + 1

    lastMeasurement = currentMeasurement

print("{} measurement was higher then the previous".format(measurementLargerCount))