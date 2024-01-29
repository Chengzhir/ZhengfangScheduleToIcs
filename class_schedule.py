import json
import ics
import datetime


def convertClassSchduleToIcs(startDate, inputFilePath, outputFilePath, configFilePath):
    classSchedule = ics.Calendar()
    with open(inputFilePath, "r", encoding="utf-8") as inputFile:
        classList = json.load(inputFile)["kbList"]
    print(startDate)
    for class_ in classList:
        classEvent = ics.Event()
