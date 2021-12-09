file = open('day1-input.txt', 'r')

measurementSumLargerCount = 0

slidingWindow = []

for i in range(0, 3):
    slidingWindow.append(int(file.readline()))

lastMeasurementSum = sum(slidingWindow)

while True:
    currentMeasurement = file.readline()

    if not currentMeasurement:
        file.close()
        break

    currentMeasurement = int(currentMeasurement)

    slidingWindow.pop(0)
    slidingWindow.append(currentMeasurement)

    currentMeasurementSum = sum(slidingWindow)

    if currentMeasurementSum > lastMeasurementSum:
        measurementSumLargerCount = measurementSumLargerCount + 1

    lastMeasurementSum = currentMeasurementSum

print("{} measurements were higher then the previous".format(measurementSumLargerCount))