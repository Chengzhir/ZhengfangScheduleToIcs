import json
import ical.calendar
import ical.event
import ical.types
from ical.calendar_stream import IcsCalendarStream
import datetime
import re
import utils
from pathlib import Path


def convertClassSchduleToIcs(
    firstMonday: datetime.datetime,
    inputFilePath: Path,
    outputFilePath: Path,
    configFilePath: Path,
):
    # 创建一个空的日历对象
    classSchedule = ical.calendar.Calendar()

    # 读取输入的JSON文件并解析课程列表
    with inputFilePath.open("r", encoding="utf-8") as inputFile:
        classList = json.load(inputFile)["kbList"]

    # 读取配置文件，获取相关配置信息
    with configFilePath.open("r", encoding="utf-8") as configFile:
        configs = json.load(configFile)

    # 遍历课程列表，将每个课程转换为日历事件
    for class_ in classList:
        # 解析周次范围
        weekNumbers = utils.parse_week_string(class_["zcd"])
        if not weekNumbers:
            continue

        sorted_weeks = sorted(list(weekNumbers))
        first_week = sorted_weeks[0]
        last_week = sorted_weeks[-1]

        # 计算课程开始时间和结束时间
        startTime = utils.convertToDatetime(
            firstMonday,
            first_week,
            int(class_["xqj"]),
            configs["timetable"][class_["jcor"].split("-")[0]].split("-")[0],
        )
        endTime = utils.convertToDatetime(
            firstMonday,
            first_week,
            int(class_["xqj"]),
            configs["timetable"][class_["jcor"].split("-")[-1]].split("-")[-1],
        )

        # 计算需要排除的日期，即非上课周次对应的日期
        recurringRule = ical.types.Recur(
            freq=ical.types.Frequency.WEEKLY,
            count=last_week - first_week + 1,
            interval=1,
        )
        exceptionDates = []
        for weekNumber in range(first_week, last_week + 1):
            if weekNumber not in weekNumbers:
                exceptionDates.append(
                    utils.convertToDate(firstMonday, weekNumber, int(class_["xqj"]))
                )

        # 创建课程事件，并添加到日历对象中
        classEvent = ical.event.Event(
            dtstart=startTime,
            dtend=endTime,
            summary=class_["kcmc"],
            description=class_["xm"],
            location=class_["xqmc"][:-2] + " " + class_["cdmc"],
            rrule=recurringRule,
            exdate=exceptionDates,
        )
        classSchedule.events.append(classEvent)

    # 将日历对象转换为ICS格式并写入输出文件
    with outputFilePath.open("w", encoding="utf-8") as outputFile:
        outputFile.write(IcsCalendarStream.calendar_to_ics(classSchedule))

    return


def convertExamSchduleToIcs(
    inputFilePath: Path,
    outputFilePath: Path,
    configFilePath: Path,
):
    examSchedule = ical.calendar.Calendar()
    with inputFilePath.open("r", encoding="utf-8") as inputFile:
        examList = json.load(inputFile)["items"]
    with configFilePath.open("r", encoding="utf-8") as configFile:
        configs = json.load(configFile)

    for exam in examList:
        startTime, endTime = utils.getTimeRange(exam["kssj"])

        examEvent = ical.event.Event(
            dtstart=startTime,
            dtend=endTime,
            summary=exam["kcmc"] + "：" + exam["ksmc"],
            location=exam["cdxqmc"][:-2] + " " + exam["cdmc"] + " " + exam["zwh"],
        )
        examSchedule.events.append(examEvent)

        with outputFilePath.open("w", encoding="utf-8") as outputFile:
            outputFile.write(IcsCalendarStream.calendar_to_ics(examSchedule))
