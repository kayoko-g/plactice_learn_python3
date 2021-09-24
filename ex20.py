#argvをインポートする。
from sys import argv

#script, input_file をargvに代入する。
script, input_file = argv

#以降3つが関数。
#①print_all関数は、引数ｆで受け取ったファイルを.read()部分で読みだしている。
def print_all(f):
    print(f.read())
#②rewind関数は、fで受け取ったファイルの先頭にカーソルを移動
def rewind(f):
    f.seek(0)
#③
def print_a_line(line_count, f):
    print(line_count, f.readline())


current_file = open(input_file, encoding = 'utf-8')

print('まずファイル全体を出力する:')

print_all(current_file)

print('最初に巻き戻して、')

rewind(current_file)

print('先頭の3行を出力する:')

current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)
current_line = current_line + 1
print_a_line(current_line, current_file)

print_a_line(current_line, current_file)
print_a_line(current_line, current_file)
print_a_line(current_line, current_file)