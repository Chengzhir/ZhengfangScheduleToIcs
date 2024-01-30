import json
import ical.calendar
import ical.event
import datetime
import re
import utils


def convertClassSchduleToIcs(
    firstMonday, inputFilePath, outputFilePath, configFilePath
):
    classSchedule = ical.calendar.Calendar()
    with open(inputFilePath, "r", encoding="utf-8") as inputFile:
        classList = json.load(inputFile)["kbList"]
    with open(configFilePath, "r", encoding="utf-8") as configFile:
        configs = json.load(configFile)
    print(firstMonday)
    for class_ in classList:
        weeks = list(
            map(
                lambda s: list(
                    map(int, ([item for item in re.split("-|周", s) if item]))
                ),
                class_["zcd"].split(","),
            )
        )
        # print(weeks)
        startTime = utils.convertToDatetime(
            firstMonday,
            weeks[0][0],
            int(class_["xqj"]),
            configs["timetable"][class_["jcor"].split("-")[0]].split("-")[0],
        )
        endTime = utils.convertToDatetime(
            firstMonday,
            weeks[0][0],
            int(class_["xqj"]),
            configs["timetable"][class_["jcor"].split("-")[-1]].split("-")[-1],
        )

        classEvent = ical.event.Event(
            dtstart=startTime,
            dtend=endTime,
            summary=class_["kcmc"],
            description=class_["xm"],
            location=class_["xqmc"] + class_["cdmc"],
        )
