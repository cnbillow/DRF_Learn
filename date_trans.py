import datetime

# 获取当前时间
now = datetime.datetime.now()
print(now, type(now))

format_time = now.strftime('%Y-%m-%d')
print(format_time, type(format_time))
