#这是写入器
from time import sleep
from json import *
en_us_master={#en_us语言
       "master_1":"Welcome to use Ikunlauncher.",
       "master_input_command":"Please enter the command here (enter \"help\" for assistance)>"
      }
zh_cn={
       "master_1":"欢迎来到IKUNlauncher启动器。",
      }
config={
        "lang":"zh_cn",
        "jre":"none",
        "gamepath":"none",
        "memory_min":"1G",
        "memory_max":"2G",
        "Version_isolation":"close",
        "account":"no"
       }
with open(r"languages/en_us.json", 'w')as f:#写入en_us语言库
    dump(en_us_master,f)
with open("launcher_config.json",'w')as f2:
    dump(config,f2)
with open(r"languages/zh_cn.json",'w')as f3:
    dump(zh_cn,f3)
