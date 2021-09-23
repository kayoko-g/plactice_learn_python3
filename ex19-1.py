def odogu(sumi_count,kami_count,fude_count):
    print(f'墨が{sumi_count}本、紙が{kami_count}冊、筆が{fude_count}本。')
  
#1個目
odogu(1,1,2)


#2個目
print('お道具の在庫を増やした。')
add_sumi = 10
add_kami = 12
add_fude = 20
odogu(1 + add_sumi, 1 + add_kami, 2 + add_fude)

#3個目
print('購入されたので在庫が減った')
odogu(11 - 8, 13 - 8, 22 - 8)

#４個目