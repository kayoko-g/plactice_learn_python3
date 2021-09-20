#argvをインポートする
from sys import argv
#existsをインポートする
from os.path import exists

#script,from_file,to_fileをargvに代入する
script, from_file, to_file = argv

##次の2行を1行で書くことができる。どうすればよいだろうか?
#from_file をバイナリファイルの読み込みモードで開く。
in_file = open(from_file,'rb')
#in_fileを読み込む
#in_data = in_file.read()

#操作者にEnterかCTRLを選択させる。
input()

#to_fileをバイナリモードの書き込み用で開く
out_file = open(to_file,'wb')

#out_file にin_data の内容を書き込む
out_file.write(in_file)

#printにて「すべて完了した。」を表示させる。
print('すべて完了した。')

#out_fileを閉じる
out_file.close()

#in_fileを閉じる
in_file.close()