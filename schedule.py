import json
import ical.calendar
import ical.event
import ical.types
from ical.calendar_stream import IcsCalendarStream
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

    for class_ in classList:
        weekRanges = list(
            map(
                lambda s: list(
                    map(int, ([item for item in re.split("-|周", s) if item]))
                ),
                class_["zcd"].split(","),
            )
        )
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

        weekNumbers = set()
        for weekRange in weekRanges:
            weekNumbers = weekNumbers.union(set(range(weekRange[0], weekRange[-1] + 1)))
        recurringRule = ical.types.Recur(
            freq=ical.types.Frequency.WEEKLY,
            count=weekRanges[-1][-1] - weekRanges[0][0] + 1,
            interval=1,
        )
        exceptionDates = []
        for weekNumber in range(weekRanges[0][0], weekRanges[-1][-1]):
            if weekNumber not in weekNumbers:
                exceptionDates.append(
                    utils.convertToDate(firstMonday, weekNumber, int(class_["xqj"]))
                )

        classEvent = ical.event.Event(
            dtstart=startTime,
            dtend=endTime,
            summary=class_["kcmc"],
            description=class_["xm"],
            location=class_["xqmc"] + " " + class_["cdmc"],
            rrule=recurringRule,
            exdate=exceptionDates,
        )
        classSchedule.events.append(classEvent)
    with open(outputFilePath, "w", encoding="utf-8") as outputFile:
        outputFile.write(IcsCalendarStream.calendar_to_ics(classSchedule))
    return


def convertExamSchduleToIcs(
    startDate: datetime.datetime,
    inputFilePath: str,
    outputFilePath: str,
    configFilePath: str,
):
    # todo
    return
