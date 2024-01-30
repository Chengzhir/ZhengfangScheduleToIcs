import class_schedule
import exam_schedule
import datetime
import tzlocal

if __name__ == "__main__":
    type = int(input("请选择需要转换成日历的内容类型编号（1. 课表 2. 考试）："))
    startDate = datetime.datetime.strptime(
        input("请输入该学期第一周周一的日期（格式为年-月-日）："), "%Y-%m-%d"
    )
    startDate = startDate.replace(tzinfo=tzlocal.get_localzone())
    inputFilePath = input("请输入待处理的JSON文件路径：")
    outputFilePath = input("请输入输出的ics文件路径：")
    configFilePath = r"./config.json"
    match type:
        case 1:
            class_schedule.convertClassSchduleToIcs(
                startDate, inputFilePath, outputFilePath, configFilePath
            )
        case 2:
            exam_schedule.convertExamSchduleToIcs(
                startDate, inputFilePath, outputFilePath, configFilePath
            )
