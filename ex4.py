# 此节练习变量的设定与运算，变量通过“=”等号进行赋值
# 本节中设定了8个变量，前4个直接用数字进行赋值，后4个通过前面的变量进行了运算
cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven

# 通过逗号将字符与变量相连接，代码中的逗号在运行时显示为一个空格
print "There are",cars,"cars available."
print "There are only",drivers,"drivers available."
print "There will be",cars_not_driven,"empty cars today."
print "We can transport",carpool_capacity,"people today."
print "We have",passengers,"to carpool today."
print "We need to put about",average_passengers_per_car,"in each car."
