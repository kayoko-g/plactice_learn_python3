#これは少し奇妙に思えるかもしれない。正確に入力することを忘れずに。
#変数daysに文字列　月 火 水 木 金 土 日　を代入
days = '月 火 水 木 金 土 日'
#変数monthsに文字列　一月\n二月\n三月\n四月\n五月\n六月\n七月\n八月　を代入。
#この時、〇月の前に\nをいれるのは、改行のため。
months = '一月\n二月\n三月\n四月\n五月\n六月\n七月\n八月'

#printによって変数daysを表示
print('曜日:',days)
#printによって変数monthsを表示
print('月:',months)

#'''3つを使うことで、中の文章で改行できるようになっている。
print('''
ここでは新しいことをやっている。
二重引用符を三つ使うことで。
好きなだけ入力できる。
望むなら4行でも5行でも6行でも。
''')
