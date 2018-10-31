import os
import sys
from PyQt5 import QtWidgets
from PyQt5.QtCore

Class Form(QtWidget):
	def __init__(self):
		super().__init__()
		self.initUI()
	def initUI(self):
		btn = QPushButton("")

dirname = "D:////" # 스팀 경로
filenames = os.listdir(dirname)
i = 0
arr = []

for filename in filenames:
	arr.append(filename)

f = open("D:\\\\sbinit.config",'w') # 모드 설정파일 경로
f.write( '  {\n  "assetDirectories" : [\n    "..\\\\assets\\\\",\n    "..\\\\mods\\\\",\n')

cnt = len(filenames)
while i < cnt:
	if(i == cnt-1):
		print("is it work?")
		data1 = '"'+"..\\\\steamapps\\\\workshop\\\\content\\\\211820\\\\"+arr[i]+"\\\\"+'"'+"\n"
		f.write(data1)
		print(i)
		print(data1)
		break
	data2 = '"'+"..\\\\steamapps\\\\workshop\\\\content\\\\211820\\\\"+arr[i]+"\\\\"+'"'+","+"\n"
	f.write(data2)
	print(i)
	print(data2)
	i+=1

f.write(' ],\n\n  "storageDirectory" : "..\\\\storage\\\\",\n\n  "defaultConfiguration" : {\n    "gameServerBind" : "*",\n    "queryServerBind" : "*",\n    "rconServerBind" : "*"\n  }\n}')
f.close()





