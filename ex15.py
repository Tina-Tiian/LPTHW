# -*- coding: utf-8 -*-
from sys import argv # 从sys中调用 argv属性

script, filename = argv # 打开argv的变量包，包含两个变量，对应运行时需给予两个赋值

txt = open(filename) # 打开／调用 一个文档

print "Here's your file %r:" % filename
print txt.read() # 通过read命令／功能，将所打开／调用的文档内容 展现出来
txt.close()

# print "Type the filename again:"
# file_again = raw_input("> ") # 提示用户输入文件名

# txt_again = open(file_again) # 通过用户输入的关键词打开／调用 一个文档

# print txt_again.read() # 通过read命令，将所打开／调用的文档内容 展现出来


# 在terminal中运行python，可以通过 open("filename").read() 来直接打开并读取文档，注意文件名加引号
