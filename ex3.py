# -*- coding: utf-8 -*-
print "I will now count my chickens:"

print "Hens", 25 + 30 /6 # 练习运算，此处将分别输出文本和数字，且输出的数字为运算的结果
print "Roosters", 100.0 - 25.0 * 3.0 % 4.0 # 用‘%’计算余数

print "Now I will count the eggs:"

print 3.0 + 2.0 + 1.0 - 5.0 + 4.0 % 2.0 - 1.0 / 4.0 + 6.0 # 继续练习运算

print "Is it true that 3 + 2 < 5 - 7?"

print 3.0 + 2.0 < 5.0 - 7.0 # 此种运算输出的是运算的判定结果，对应有‘True’和‘False’两种结果

print "What is 3 + 2?", 3.0 + 2.0
print "What is 5 - 7?", 5.0 - 7.0

print "Oh, that's why it's False."

print "How about some more."

print "Is it greater?", 5.0 > -2.0
print "Is it greater or equal?", 5.0 >= -2.0
print "Is it less or equal?", 5.0 <= -2.0

# 在进行数学运算时，输入的数字有一个采用了floating number，该行运算的结果也会以floating number显示
# 此节展现了三种数据形态，字符、数字和boolean
# 其中字符需要用引号“”或‘’扩起来，以区分变量；数字不用引号；boolean的两种形态都需要首字母大写，否则会作为字符数据
