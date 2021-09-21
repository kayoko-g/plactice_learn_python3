#cheese_and_crackers関数の引数をcheese_countとboxes_of_crackersを定義している。
def cheese_and_crackers(cheese_count, boxes_of_crackers):
#以下にcheese_and_crackers関数が行う操作が書いてある。
#printにて「チーズが{cheese_count}個!」を表示させる。fによって{cheese_count}はフォーマット化済。
    
    print(f'チーズが{cheese_count}個!')
    #pruntにて「クラッカーが{boxes_of_crackers}箱」を表示させる。fによって{boxes_of_crakers}はフォーマット化済み。
    print(f'クラッカーが{boxes_of_crackers}箱!')
    #printにて「パーティーには十分な量だ!」を表示させる。
    print('パーティーには十分な量だ!')
    #printにて「ブランケットをもって出かけよう」を表示させる。\nは改行。その後ろに文字が続かないので、ここでは段落を作る仕組みとなっている。
    print('ブランケットをもって出かけよう。\n')

#printにて「関数にそのまま数値を渡すことができる：」を表示させる。
print('関数にそのまま数値を渡すことができる:')
#上で定義した関数の因数部分に数字を直接入力し、関数を実行させている。
cheese_and_crackers(20, 30)

#printにて「スクリプトの変数を使うこともできる:」を表示させる。
print('スクリプトの変数を使うこともできる:')
#amout_of_cheeseに10を代入
amount_of_cheese = 10
#amout_of_crackersに50を代入
amount_of_crackers = 50
#上で定義した関数の引数として、変数amouto_of_cheese、amout_of_crackersを使っている。
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

#printにて「計算結果も渡すこともできる:」を表示
print('計算結果も渡すこともできる:')
#引数に直接数字を使っているがここでは引数を書く欄に計算式をいれている。
cheese_and_crackers(10 + 20, 5 + 6)

#printにて「もちろん、変数と計算を組み合わせることもできる:」を表示。
print('もちろん、変数と計算を組み合わせることもできる:')
#引数に上で定義した変数amout_of_cheeseとamout_of_crackersにそれぞれ100と1000を足した数を引数として使っている。
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
