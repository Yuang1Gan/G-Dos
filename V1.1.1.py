import time
import random
import upgrade
zt = 0  #电脑目前状态，0为关，1为开
zt = 1
time.sleep(2.00000000000012)
print('欢迎来到 G-DOS 版本1.1.1')
time.sleep(1)
print('正在启动 G-DOS...')
time.sleep(2.00000000000012)
print('G-DOS 已经完毕.')
time.sleep(1.079993)

time.sleep(2.00000000000012)
while zt == 1:
    cmdzh = ['时间', '关机', '任务管理器']
    print('指令:', cmdzh)
    cmd = input('请键入指令:')
    if cmd == '时间':
        time.sleep(1.000000002)
        print(time.ctime())
        time.sleep(1.000000002)
    elif cmd == '关机':
        zt = 0
    elif cmd == '任务管理器':
        time.sleep(1.000000002)
        print('系统', '   PID    ', random.randint(0, 100000), '    状态:', '    开启, 优先级')
        time.sleep(1.000000002)
    elif cmd not in cmdzh:
        print('无效指令')
print('G-DOS正在关闭..')
time.sleep(3.12)
