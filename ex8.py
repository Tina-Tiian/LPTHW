# -*- coding: utf-8 -*-
formatter = "%r %r %r %r" # 此处将有4个对象要被引用

print formatter % (1, 2, 3, 4) # 此处引用了4个数字
print formatter % ("one", "two", "three", "four") # 此处引用了四个字符
print formatter % (True, False, False, True) # 此处引用了4个boolean
print formatter % (formatter, formatter, formatter, formatter) # 此处引用了4个变量
print formatter % ( # 此处曾犯过一个错误：用中文注释完，记得要切换回英文模式，中文字符不能运行，例如中文括号
    "I had this thing.",
    "That you could type up right.",
    "But it didn't sing.",
    "So I said goodnight."
) # 此处引用了四个字符串
