# -*- coding: utf-8 -*-
x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not) # a string inside a string 01

print x
print y

print "I said: %r." % x # a string inside a string 02
print "I also said: '%s'." % y # a string inside a string 03

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r" # a string inside a string 04

# 此处的练习可以看到：在字符串中所引用的变量不是必须紧接着“”引号出现，
# 中间还可以间隔其他内容，直到运行到后面第一个‘%’所连接的变量时，执行引用
print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side."

# 此处练习‘+’可以起到字符串的连接作用，无缝衔接哟
print w + e
