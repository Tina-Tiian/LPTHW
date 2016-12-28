# -*- coding: utf-8 -*-
from sys import argv

# script, first, second, third = argv

# print "The script is called:", script
# print "Your first variable is:", first
# print "Your second variable is:", second
# print "Your third variable is:", third


# study drills
# 此处中了“想太多”的毒，但中毒越深越能体会到 给argv赋值 与 raw_input输入值 两者作用的差别
# 曾经试过 a，b在前的效果，然而对print结果来说并没有什么卵用，但可以帮助弄清楚在哪里 给argv赋值是有效的
script, a, b = argv
a = raw_input("What's the date today? ")
b = raw_input("How is the weather? ")

print "So, today is %s and it's a %s day." % (a, b)
