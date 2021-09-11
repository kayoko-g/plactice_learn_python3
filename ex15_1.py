#argvモジュールを使えるようにする
from sys import argv
#script filename　を argv　に代入する。 
script, filename = argv
#txt に open(filename,encoding='utf-8')　を代入する。 open()はファイルを返す組み込み関数
txt = open(filename,encoding='utf-8')

#変数{filename}をフォーマットしたものをprintにて表示
print(f'{filename}の内容は次のとおり：')

#〇.read()にて〇のファイルを読みだしている
print(txt.read())

