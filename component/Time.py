from datetime import datetime


# 定义一个函数来将日期时间字符串转换为目标格式
def convert_datetime(input_datetime_str):
    input_datetime = datetime.strptime(input_datetime_str, '%a, %d %b %Y %H:%M:%S GMT')
    formatted_datetime_str = input_datetime.strftime('%Y-%m-%d %H:%M:%S')
    return formatted_datetime_str


def Da(lis, key):
    for item in lis:
        item["update_time"] = str(item[key])
        print(type(item["update_time"]))
        # print(item)
    #
    # return lis
