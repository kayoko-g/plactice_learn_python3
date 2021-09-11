
#inputのみで記述→コードが長くなる。実行するのも少々面倒。
from os import close, terminal_size


script = input('スクリプト名を入力してみよう:') 
filename = input('読みたいファイル名を入力してみよう:')

#txt に open(filename,encoding='utf-8')　を代入する。 open()はファイルを返す組み込み関数
txt = open(filename,encoding='utf-8')

#変数{filename}をフォーマットしたものをprintにて表示
print(f'{filename}の内容は次のとおり：')

#〇.read()にて〇のファイルを読みだしている
print(txt.read())

txt.close()

#printにて「もう一度ファイル名を入力しよう：」を表示
print('もう一度ファイル名を入力しよう：')
#file_againにinput('> ')を代入。>より後に入力された文字列がfile_againに代入される。
file_again = input('> ')
#txt_again にopen(file_again,encoding='utf-8')を代入。inputで入力された文字列(ファイル名)が組み込み関数open()によって開かれる
txt_again = open(file_again,encoding='utf-8')
#printにてtxt_again.read()を表示。ここでは、txt_againにて読みだしたファイルを表示させている。
print(txt_again.read())

txt_again.close