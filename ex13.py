#モジュールをインポートする。
from sys import argv

#このコードを実行する方法は「実行結果」を参照すること。
#引数をargvに代入する。
#script, first, second, third = argv

#printにて'このスクリプトの名前は:'を表示させ、続けて引数のscript を表示させる。
#print('このスクリプトの名前は:', script)
#printにて'first変数の値は:'を表示させ、続て引数のfirst を表示させる。
#print('first変数の値は:', first)
#printにて'second変数の値は:'を表示させ、続けて引数のsecond を表示させる。
#print('second変数の値は:', second)
#printにて、'third変数の値は:'を表示させ、続けて引数のthird　を表示させる。
#print('third変数の値は:', third)

#引数をargvに代入する。
script, apple, orange, banana, grape = argv

#printにて'このスクリプトの名前は:'を表示させ、続けて引数のscript を表示させる。
print('このスクリプトの名前は:', script)
#printにて'first変数の値は:'を表示させ、続て引数のfirst を表示させる。
print('appeleの個数は:', apple)
#printにて'second変数の値は:'を表示させ、続けて引数のsecond を表示させる。
print('orangeの個数は:', orange)
#printにて、'third変数の値は:'を表示させ、続けて引数のthird　を表示させる。
print('grapeの個数は:', banana)
#printにて、'third変数の値は:'を表示させ、続けて引数のthird　を表示させる。
print('grapeの個数は:', grape)

# prompt に > を代入
prompt = '> '
#print で「何が食べたい?」を表示。
print('何が食べたい?')
#inputにて> 以降の答えをeatに代入
eat = input(prompt)
#print にて表示
print(f'君は{eat}が食べたいのだね。')
