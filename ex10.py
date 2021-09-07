#変数　tabby_cat　に　\tこれはタブ。を代入。\t　はタブを表している
tabby_cat = '\tこれはタブ。'
#変数 persian_cat に これは行を\n分割。を代入。　\n は改行を表している。
persian_cat = 'これは行を\n分割。'
#変数 backslash_cat に これは\\一匹の\\猫。を代入。\\のうち一つが表示される。
backslash_cat = 'これは\\一匹の\\猫。'

#変数fat_cat に """'猫'用のリスト：\t* キャットフード\t* 魚\t* マタタビ\n\t* 猫草"""を代入している。"""により改行を、\tによりスペースを　\nにより改行を行っている。

fat_cat = """
'猫'用のリスト：
\t* キャットフード
\t* 魚
\t* マタタビ\n\t* 猫草
"""
#プリントにより上で作った変数を表示させている。
print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)

#演習2:"""は'''でも代用可能。ただし、文字列の中で''が使いたいのか、""が使いたいのかによって、考える必要がある。
fat_cat2 = '''
"猫"用のリスト：
\t* キャットフード
\t* 魚
\t* マタタビ\n\t* 猫草
'''

print(fat_cat2)

#演習3
persian_cat2 = 'これは行を\n分割。'
print('猫:',persian_cat2)
print('猫{}'.format('の家'))
print(f'猫{persian_cat2}')