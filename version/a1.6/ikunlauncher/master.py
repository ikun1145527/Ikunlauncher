from time import sleep
import json
import os
#print("lang pack is loading")(语言文件加载
# with open("launcher_config.json",'r')as f1:
#    temp1=json.load(f1)
#    #print(temp1)
# lang=temp1["lang"]
# temp2=r"languages/"+lang+".json"
# with open(temp2,'r')as f2:
#     words=json.load(f2)
#     print(words)
print("欢迎来到Ikunlauncher启动器")#对应master_1
sleep(2)
a="鸡"
while a != "quit":
    a=input("请在这里输入指令(输入help获取帮助,输入quit退出程序)>")#对应master_2
    sleep(1)
    if a == "LSC":
        os.startfile("LSC.py")
    if a == "setup":
        os.startfile("setup.py")
    if a == "help":
        with open("helpdoc.json",'r')as f3:
            helpdoc=json.load(f3)
        print(helpdoc)