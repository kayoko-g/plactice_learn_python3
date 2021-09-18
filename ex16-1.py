from sys import argv

#scriptとfilenameをargvに代入
script, filename = argv

#filenameを開く
txt = open(filename,encoding='utf-8')

#内容を書き出す
print(txt.read())
