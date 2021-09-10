from sys import argv

#2つの引数にargv を代入
script, user_name = argv
#prompt に> を代入
prompt = '> '

#変数{user_name} {scriput}をフォーマットしprintを使って表示。
print(f'やぁ、{user_name}。私は{script}スクリプトです。')
#printにて質問を表示
print('私は君にいくつかの質問をしたいと思います。')
#変数{user_name}をフォーマットし、print にて表示
print(f'{user_name}、君は私のことが好きですか?')
#likes に答えを代入
likes = input(prompt)

#変数{user_name}をフォーマットし、printで表示
print(f'{user_name}、君はどこに住んでいますか?')
#lives に答えを代入
lives = input(prompt)
#printにて質問を表示
print('君はどんな種類のコンピュータをもっていますか?')
#computerに答えを代入
computer = input(prompt)

#変数likes lives computer をフォーマットしprint で表示
print(f"""
いいね。私のことが好きですかと聞いたら、君は「{likes}」といった。
君は{lives}に住んでいる。私にはどこかわからないけどね。
それに、君は{computer}コンピュータをもっている。すごいね。
""")