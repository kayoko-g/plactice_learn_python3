#argvをインポートする
from sys import argv
#existsをインポートする
from os.path import exists

#script,from_file,to_fileをargvに代入する
script, from_file, to_file = argv

#{from_file}と  {to_file}をフォーマットし、「{from_file}から{to_file}へコピーする」を出力する。
print(f'{from_file}から{to_file}へコピーする。')


##次の2行を1行で書くことができる。どうすればよいだろうか?
#from_file をバイナリファイルの読み込みモードで開く。
in_file = open(from_file,'rb')
#in_fileを読み込む
in_data = in_file.read()

#{len(in_data)}をフォーマットし、printにて「入力ファイルの大きさは、{len(in_data)}バイト」を出力する。len()は()内の文字数を返す関数。
print(f'入力ファイルの大きさは{len(in_data)}バイト。')

#exist(to_file)をファーマット化し、printにて「出力ファイルは存在するか？{exist(to_file)}」を表示させる
print(f'出力ファイルは存在するか?{exists(to_file)}')

#printにて「準備できた。続行するにはEnterキーを、中断するにはCTRL-Cを入力する。」を出力する
print('準備できた。続行するにはEnterキーを、中断するにはCTRL-Cを入力する。')

#操作者にEnterかCTRLを選択させる。
input()

#to_fileをバイナリモードの書き込み用で開く
out_file = open(to_file,'wb')

#out_file にin_data の内容を書き込む
out_file.write(in_data)

#printにて「すべて完了した。」を表示させる。
print('すべて完了した。')

#out_fileを閉じる
out_file.close()

#in_fileを閉じる
in_file.close()


