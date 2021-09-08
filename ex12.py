#inputにて'君の年齢は？'の質問をださせる。ageにその回答を代入する。
age = input('君の年齢は?')
#inputにて'君の身長は？'の質問を出させる。heightにその回答を代入する。
height = input('君の身長は?')
#input にて'君の体重は？'の質問を出させる。weightにてその回答を代入する。
weight = input('君の体重は?')

#printにて上記変数を用いて'君は○○歳で、身長は○○で、体重はは○○だ。'を出力させる。
print(f'君は{age}歳で、身長は{height}で、体重は{weight}だ。')

#プロンプト：動作を促すもの'

#Pydocは、Pythonのヘルプ/ドキュメントモジュールです。
#Windows端末でこれを使用して、pythonの関数が何をするかを理解します。
#python -m pydoc open
#python -m pydoc file
#python -m pydoc os
#python -m pydoc sys