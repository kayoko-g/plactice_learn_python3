#carsに100を代入
cars = 100
#1台当たりの乗車人数4人をspace_in_a_carに代入
space_in_a_car = 4.0
#運転手30人をdriversに代入
drivers = 30
# 乗組員90人をpassengersに代入
passengers = 90
#使われていない車の台数をcars_not_drivenに代入
cars_not_driven = cars - drivers
#使われている車の数をcars_drivenに代入
cars_driven = drivers
#車の最大収容人数をcarpool_capacityに代入
carpool_capacity = cars_driven * space_in_a_car
#平均乗車人数をaaverage_passengers_par_car 　に代入
average_passengers_per_car = passengers / cars_driven

print('今日は', cars ,'台の車が利用可能。')
print('今日は',drivers,'人しかドライバーがいない。')
print('だから',cars_not_driven,'人の乗客を運べる。')
print('今日は',carpool_capacity,'人の乗客を運べる。')
print('今日は',passengers,'人の乗客がいる。')
print('一台の車に',average_passengers_per_car,'人を乗せる必要がある。')