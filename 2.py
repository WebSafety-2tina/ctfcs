import subprocess
import time

# 要输出的命令列表
commands = [
    "git pull https://github.com/dlongx/ctfcs.git",
    # 可以添加更多命令...
]

# 每秒输出一条命令
while True:
    for command in commands:
        subprocess.run(command, shell=True)
        time.sleep(1)
