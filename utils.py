import datetime


def convertToDatetime(firstMonday, weekNumber: int, dayOfWeek: int, time: str):
    return firstMonday + datetime.timedelta(
        weeks=weekNumber - 1,
        days=dayOfWeek - 1,
        hours=int(time.split(":")[0]),
        minutes=int(time.split(":")[1]),
    )
