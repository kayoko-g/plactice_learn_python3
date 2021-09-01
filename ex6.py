#変数types_of_peopleに10を代入
types_of_people = 10
#xにf'世の中には{types_of_people}種類の人間がいる。'を代入
x = f'世の中には{types_of_people}種類の人間がいる。'　#3個目

#binaryに'バイナリ'を代入
binary = 'バイナリ'
#do_notに'そうでない'を代入
do_not = 'そうでない'
#yにf'{binary}を知っている人と、{do_not}人だ。'を代入
y = f'{binary}を知っている人と、{do_not}人だ。'　#4個目

#printにて、上記変数xとyを表示
print(x)
print(y)

#printにてf'私はいった:{x}'を表示
print(f'私はいった:{x}') #1個目
#printにてf'こうともいった:"{y}"'を表示
print(f'こうともいった:"{y}"')#2個目

#hilariousにFalseを代入
hilarious = False
#joke_evaluationに'このジョークは面白かったかな?!{}'を代入
joke_evaluation = 'このジョークは面白かったかな?!{}'

#joke_evaluation.format(hilarious)をprintにて表示
print(joke_evaluation.format(hilarious))


w = 'これは左側のテキストで…'
e = 'これは右側のテキストだ。'
print(w + e)
