import schedule
import datetime
import tzlocal
import argparse
from pathlib import Path

if __name__ == "__main__":
    # type = int(input("请选择需要转换成日历的内容类型编号（1. 课表 2. 考试（未完成））："))
    # firstMonday = datetime.datetime.strptime(
    #     input("请输入该学期第一周周一的日期（格式为年-月-日）："), "%Y-%m-%d"
    # )
    # firstMonday = firstMonday.replace(tzinfo=tzlocal.get_localzone())
    # inputFilePath = input("请输入待处理的JSON文件路径：")
    # outputFilePath = input("请输入输出的ics文件路径：")
    # configFilePath = r".\config.json"

    parser = argparse.ArgumentParser(description="帮助")

    parser.add_argument(
        "-t",
        "--type",
        choices=["class", "exam"],
        required=True,
        help="需要转换的事件类别（class或exam）",
    )   
    parser.add_argument(
        "-f",
        "--first-Monday",
        required=True,
        type=lambda s: datetime.datetime.strptime(s, "%Y-%m-%d").replace(
            tzinfo=tzlocal.get_localzone()
        ),
        help="该学期第一周周一的日期（格式为年-月-日）",
    )
    parser.add_argument(
        "-i",
        "--input",
        type=Path,
        help="输入文件路径",
    )
    parser.add_argument(
        "-o",
        "--output",
        required=True,
        type=Path,
        help="输出文件路径",
    )
    parser.add_argument(
        "-c",
        "--config",
        default=Path(r".\config.json"),
        type=Path,
        help="配置文件路径",
    )

    args = parser.parse_args()

    match args.type:
        case "class":
            schedule.convertClassSchduleToIcs(
                args.first_Monday, args.input, args.output, args.config
            )
        case "exam":
            schedule.convertExamSchduleToIcs(
                args.first_Monday, args.input, args.output, args.config
            )
