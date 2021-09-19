from sys import argv

#scriptとfilenameをargvに代入
script, filename = argv

#printにて「これから{filename}を消去する」を表示{filename}はフォーマット化されている。
print(f'これから{filename}を消去する。')
#printにて「消去したくないならCtrl-C(^C)を入力し」を表示。
print('消去したくないならCTRL-C (^C)を入力し、')
#printにて「消去してもよいなら、Enterキーを入力する」を表示。
print('消去してもよいならEnterキーを入力する。')

#inputにて?以降選んだ行為を実行する。
input('?')

#printにて「ではファイルを開こう」を表示させる。
print('ではファイルを開こう...')
#targetにopen関数を代入。ここではファイルを書き込みにて開かせている。
target = open(filename,'w',encoding='utf-8')

#printにて「ファイルを切り捨てる。グッバイ！」を表示させる。
print('ファイルを切り捨てる。グッバイ!')

#ファイルの中の文字を0にする。
target.truncate()

#printにて「3行分の内容を入力する」を表示させる。
print('3行分の内容を入力する。')

#1行目の後に入力した言葉をline1に代入する。
line1 = input('1行目:')
#2行目の後に入力した言葉をline2に代入する。
line2 = input('2行目:')
#3行目の後に入力した言葉をline3に代入する。
line3 = input('3行目:')

#printにて「これらをファイルに書き込む」を表示させる。
print('これらをファイルに書き込む。')

#line1をファイルに書き込む
target.write(line1)
#改行する
target.write('\n')
#line2をファイルに書き込む
target.write(line2)
#改行する
target.write('\n')
#line3をファイルに書き込む
target.write(line3)
#改行する
target.write('\n')

print('一度に記述させる。')

#line1～line3を一度に記述させる。
target.write(f'{line1}\n{line2}\n{line3}\n')

#「最後にファイルを閉じる」を表示させる
print('最後にファイルを閉じる。')
#ファイルを閉じる
target.close()

