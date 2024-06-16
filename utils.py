import datetime
import re


def convertToDatetime(
    firstMonday: datetime.datetime, weekNumber: int, dayOfWeek: int, time: str
):
    """
    将学期第一周的周一日期、周次、星期几和时间转换为具体的日期和时间。

    Args:
        firstMonday (datetime.datetime): 学期第一周的周一日期。
        weekNumber (int): 周次。
        dayOfWeek (int): 星期几（1表示星期一，2表示星期二，依次类推）。
        time (str): 时间，格式为"时:分"。

    Returns:
        datetime.datetime: 转换后的日期时间对象。
    """
    return firstMonday + datetime.timedelta(
        weeks=weekNumber - 1,
        days=dayOfWeek - 1,
        hours=int(time.split(":")[0]),
        minutes=int(time.split(":")[1]),
    )


def convertToDate(firstMonday: datetime.datetime, weekNumber: int, dayOfWeek: int):
    """
    将学期第一周的周一日期、周次和星期几转换为具体的日期。

    Args:
        firstMonday (datetime.datetime): 学期第一周的周一日期。
        weekNumber (int): 周次。
        dayOfWeek (int): 星期几（1表示星期一，2表示星期二，依次类推）。

    Returns:
        datetime.date: 转换后的日期对象。
    """
    return firstMonday.date() + datetime.timedelta(
        weeks=weekNumber - 1, days=dayOfWeek - 1
    )


def getTimeRange(dateRangeStr: str) -> list[datetime.datetime]:
    dateStr, timeRangeStr = list(filter(None, re.split("\(|\)", dateRangeStr)))
    timeRangeStr = timeRangeStr.split("-")
    startTime = datetime.datetime.strptime(
        dateStr + " " + timeRangeStr[0], "%Y-%m-%d %H:%M"
    )
    endTime = datetime.datetime.strptime(
        dateStr + " " + timeRangeStr[1], "%Y-%m-%d %H:%M"
    )

    return [startTime, endTime]
