#printにて'君の年齢は？'を出力させ、end''にて答えが出るまで一旦待たせる。
print('君の年齢は?',end=" ")
#入力を促す。変数ageに入ってきた文字を代入する
age = input()
#printにて'君の身長は？'を出力させ、end''にて答えが出るまで一旦待たせる。
print('君の身長は?',end=" ")
#入力を促す。heightに入ってきた文字を代入する。
height = input()
#printにて'君の体重は？'を出力させ、end''にて答えが出るまで一旦待たせる。
print('君の体重は?',end=" ")
#入力を促す。weightに入ってきた文字を代入する。
weight = input()


print(f'君は{age}歳で、身長は{height}で、体重は{weight}だ。')


name = input("お名前を入力してください。")
#tanaka
print("あなたの名前は", name, "です。")
#あなたの名前はtanakaです

num = int(input("数値を入力してください。"))
#20
ans = num + 10
print(ans)
#30

num = float(input("数値を入力してください。"))
#20.5
ans = num + 10
print(ans)
#30.5


#end''に関して
#「end=''」を使って文字列の意味を変えてみましょう。
text = 'あなたはカレーが好きです'
 
#末尾に疑問形である「か？」という文字列を追加します。
print(text, end='か？')



#文字列変数を2つ作ります。
text_a = 'あなたはカレーが'
text_b = '好きです。'
 
#これを別々に出力すると改行されて表示されます。
print(text_a)
print(text_b)

#改行なしで出力したい時に「end=''」を使います。
print(text_a, end='')
print(text_b)

#print関数に出力したい文字列を複数入れると、間に半角スペースが入ります。
text_c = 'わたしは'
text_d = 'からいものが'
text_e = '苦手です。'
print(text_c, text_d, text_e)

#複数の文字列の間に空白を開けたくない場合にも使えます。
print(text_c, end='')
print(text_d, end='')
print(text_e)

#逆に複数の文字列の間に半角スペースを入れたい場合は、end=' ' で指定します。
print(text_c, end=' ') #半角スペースを指定しています。
print(text_d, end=' ')
print(text_e)

#なお文字列を「+演算子」で連結する方法でも空白を避けることができます。
print(text_c + text_d + text_e)

#文字列の連結のいちばん良い書き方はこれです。
text_c = 'わたしは'
text_d = 'からいものが'
text_e = '苦手です。'
print(f'{text_c}{text_d}{text_e}')

