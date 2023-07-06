import time

def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1

    print("时间到！")

focus_time = int(input("请输入专注时长（分钟）："))
break_time = int(input("请输入休息时长（分钟）："))

while True:
    print("专注时间开始！")
    countdown(focus_time * 60)

    print("休息时间开始！")
    countdown(break_time * 60)

    choice = input("是否继续专注？（是/否）")
    if choice.lower() != "是":
        break

print("感谢使用专注时钟！")
