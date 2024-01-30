import json
import ical.calendar
import ical.event
import datetime
import re
import utils


def convertClassSchduleToIcs(
    firstMonday: datetime.datetime,
    inputFilePath: str,
    outputFilePath: str,
    configFilePath: str,
):
    classSchedule = ical.calendar.Calendar()
    with open(inputFilePath, "r", encoding="utf-8") as inputFile:
        classList = json.load(inputFile)["kbList"]
    with open(configFilePath, "r", encoding="utf-8") as configFile:
        configs = json.load(configFile)
    print(firstMonday)
    for class_ in classList:
        weekRanges = list(
            map(
                lambda s: list(
                    map(int, ([item for item in re.split("-|周", s) if item]))
                ),
                class_["zcd"].split(","),
            )
        )
        # print(weekRanges)
        startTime = utils.convertToDatetime(
            firstMonday,
            weekRanges[0][0],
            int(class_["xqj"]),
            configs["timetable"][class_["jcor"].split("-")[0]].split("-")[0],
        )
        endTime = utils.convertToDatetime(
            firstMonday,
            weekRanges[0][0],
            int(class_["xqj"]),
            configs["timetable"][class_["jcor"].split("-")[-1]].split("-")[-1],
        )

        recurringDates = []
        for weekRange in weekRanges:
            if len(weekRange) == 1:
                recurringDates.append(
                    utils.convertToDate(
                        firstMonday,
                        weekRange[0],
                        int(class_["xqj"]),
                    )
                )
            elif len(weekRange) == 2:
                for week in range(weekRange[0], weekRange[1] + 1):
                    recurringDates.append(
                        utils.convertToDate(
                            firstMonday,
                            weekRange[0],
                            int(class_["xqj"]),
                        )
                    )
            else:
                print("weekRange异常")
                exit(1)

        classEvent = ical.event.Event(
            dtstart=startTime,
            dtend=endTime,
            summary=class_["kcmc"],
            description=class_["xm"],
            location=class_["xqmc"] + class_["cdmc"],
            rdate=recurringDates,
        )
        classSchedule.events.append(classEvent)
