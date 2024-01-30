import schedule
import datetime
import tzlocal

if __name__ == "__main__":
    type = int(input("请选择需要转换成日历的内容类型编号（1. 课表 2. 考试）："))
    firstMonday = datetime.datetime.strptime(
        input("请输入该学期第一周周一的日期（格式为年-月-日）："), "%Y-%m-%d"
    )
    firstMonday = firstMonday.replace(tzinfo=tzlocal.get_localzone())
    inputFilePath = input("请输入待处理的JSON文件路径：")
    outputFilePath = input("请输入输出的ics文件路径：")
    configFilePath = r".\config.json"
    match type:
        case 1:
            schedule.convertClassSchduleToIcs(
                firstMonday, inputFilePath, outputFilePath, configFilePath
            )
        case 2:
            schedule.convertExamSchduleToIcs(
                firstMonday, inputFilePath, outputFilePath, configFilePath
            )
