from time import sleep
import json
print("Please create a JSON file to store the language")
print("Input values for packaging")
inp="a"
lang={}
key="a"
value="a"
while inp != "[-]":
    inp=input("Please enter the name of the key>")
    key=inp
    inp=input("Please enter the name of the value>")
    value=inp
    lang[key]=value
    print("created")
inp=input("Where your JSON file>")
with open(inp,'w')as f:
    json.dump(lang,f)
print("finished")
sleep(5)