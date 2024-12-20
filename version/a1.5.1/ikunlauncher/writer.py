#这是写入器
from time import sleep
from json import *
en_us_master={
# 定义一个名为en_us_master的字典，用于存储英文（美国英语）相关的文本内容，这里可以理解为是一
       "master_1":"Welcome to use Ikunlauncher.",
    # 键为"master_1"的文本内容，可能是启动器相关的欢迎语之类的提示信息，用英文表述
       "master_input_command":"Please enter the command here (enter \"help\" for assistance)>"
    # 键为"master_input_command"的文本内容，提示用户在此处输入命令，并告知输入"help"可获取帮助
      }
zh_cn={
       "master_1":"欢迎来到IKUNlauncher启动器。",
       "master_input_command":"请在这里输入指令(输入help获取帮助)>"
      }
config={
        "lang":"zh_cn",
# 配置语言，这里设置为"zh_cn"，表示中文（简体中文），是用来控制程序界面等显示语言的
        "jre":"none",
    # Java运行时环境相关配置，这里设置为"none"，后续会根据实际情况进行更新或修改
        "gamepath":"none",
# 游戏路径相关配置
        "memory_min":"1G",
# 最小内存配置，设置为"1G"，可能用于启动游戏等操作时分配内存的下限
        "memory_max":"2G",
 # 最大内存配置，设置为"2G"，用于限定启动游戏等操作时分配内存的上限
        "Version_isolation":"close",
# 版本隔离相关配置
        "account":"no"
# 账号相关配置
       }
with open(r"languages/en_us.json", 'w')as f:
    dump(en_us_master,f)
    # 以写入模式打开名为"languages/en_us.json"的文件（如果文件不存在会创建它），并将文件对象赋值给变量f
    # 这里的目的是将en_us_master字典中的内容以JSON格式写入到该文件中，实现创建或更新语言库文件的操作
with open("launcher_config.json",'w')as f2:
    dump(config,f2)
    # 以写入模式打开名为"launcher_config.json"的文件（如果文件不存在会创建它），并将文件对象赋值给变量f2
    # 作用是将config字典中的配置信息以JSON格式写入该文件，用于保存启动器的配置数据
with open(r"languages/zh_cn.json",'w')as f3:
    dump(zh_cn,f3)
# 以写入模式打开名为"languages/zh_cn.json"的文件（如果文件不存在会创建它），并将文件对象赋值给变量f3
# 目的是把zh_cn字典里的中文文本内容以JSON格式写入到这个文件中，完成中文语言库文件的创建或更新