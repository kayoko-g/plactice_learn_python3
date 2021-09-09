########ここ確実に分かってない#######################################
#formatter に{} {} {} {}を代入する
formatter = "{} {} {} {}"
#printにて、
print(formatter.format(1,2,3,4))
#printにて 
print(formatter.format('一','二','三','四'))
#printにて
print(formatter.format(True,False,False,True))
#printにて
print(formatter.format(formatter,formatter,formatter,formatter))
#printにて
print(formatter.format(    
    '好きな文を',
    'ここに書いてみよう',
    'たとえば詩や',
    '歌なんかもよいだろう'
))
