import datetime
import re


def parse_week_string(zcd: str) -> set[int]:
    """
    解析周次字符串，支持单双周。

    Args:
        zcd (str): 周次字符串, e.g., "4-5周,7-17周(单)".

    Returns:
        set[int]: 包含所有上课周次的集合。
    """
    week_numbers = set()
    parts = zcd.split(",")
    for part in parts:
        part = part.strip()
        is_odd = "(单)" in part
        is_even = "(双)" in part

        # 移除周、(单)、(双)等非数字部分
        part_digits_str = re.sub(r"周|\(单\)|\(双\)", "", part)

        # 解析范围或单个数字
        if "-" in part_digits_str:
            try:
                start, end = map(int, part_digits_str.split("-"))
                for i in range(start, end + 1):
                    if is_odd and i % 2 != 0:
                        week_numbers.add(i)
                    elif is_even and i % 2 == 0:
                        week_numbers.add(i)
                    elif not is_odd and not is_even:
                        week_numbers.add(i)
            except ValueError:
                # 处理像 "7-" 这样的无效范围
                print(f"周长度(zcd={zcd})无效")
                continue
        elif part_digits_str:
            try:
                week_numbers.add(int(part_digits_str))
            except ValueError:
                print(f"周长度(zcd={zcd})无效")
                continue

    return week_numbers


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
