import datetime


def convertToDatetime(
    firstMonday: datetime.datetime, weekNumber: int, dayOfWeek: int, time: str
):
    return firstMonday + datetime.timedelta(
        weeks=weekNumber - 1,
        days=dayOfWeek - 1,
        hours=int(time.split(":")[0]),
        minutes=int(time.split(":")[1]),
    )


def convertToDate(firstMonday: datetime.datetime, weekNumber: int, dayOfWeek: int):
    return datetime.date(firstMonday)
