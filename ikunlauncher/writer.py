#这是写入器
from time import sleep
from json import *
en_us_master={#en_us语言的master
       "master_1":"Welcome to use Ikunlauncher.",
       "master_input_command":"Please enter the command here (enter \"help\" for assistance)>"
      }
with open(r"languages/master/en_us.json", 'w')as f:#写入en_us语言库
    dump(en_us_master,f)
sleep(1)
