# -*- coding: utf-8 -*-
from sys import argv

script, filename = argv

print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

raw_input("?")

print "Opening the file..."
target = open(filename, 'w') # study drills
# 对于open()命令，默认执行的是read功能，打开并读取之后，可以附加动作的权限，例如 w 写，a 附加，以及w+、r+、a+等组合形式
# 需要注意区分的是‘’引号中代表的是赋予某种操作的权限，后续需要通过 write()等命令去具体执行相应的功能

# print "Truncating the file. Goodbye!"
# target.truncate() # 在open()中添加写功能后，不必再单独执行一次清空命令

print "Now I'm going to ask you for three lines."

line1 = raw_input("line1: ")
line2 = raw_input("line2: ")
line3 = raw_input("line3: ")
txt = "%s\n%s\n%s" % (line1, line2, line3)  # study drills 目标：给target.write瘦身
# 为了给t.w 瘦身，错误地尝试了很多种写法，好在基本思路是对的，运用转义字符将共性元素进行简化组合
# 此处如果用 %r，写入的内容会带‘’引号
print "I'm going to write these to the file."

# target.write(line1)
# target.write("\n")
# target.write(line2)
# target.write("\n")
# target.write(line3)
# target.write("\n")

# study drills  今天踩了n多的坑，在无数次跳坑出坑之后，终于豁然开朗，拨开云雾见天明，说得好像突破重重困难似的，其实就是一层窗户纸

target.write(txt)
# target.write("%s\n%s\n%s" % (line1, line2, line3))
# 此处是本练习走过的最大的弯路，从一开始写对了内容，但放错了位置，将 “%” 的部分放在了括号外面，然后绕了一大圈回到这里
# 这里暴露了关于编程最基本的逻辑习惯的问题，此行与上一行对比，其实逻辑非常简单，既然引用了txt，自然也就可以把“=”后面的部分作为替换
# 该在括号里还是在括号外，想通了逻辑，自然一目了然
# target.close() # 要想在写入内容后读取文档内容，必须先执行close，这个动作等同于 save，不做保存是无法把刚刚写入的内容读取出来的
# target = open(filename) # 相应的，执行colse 之后，相应文档也被关闭，要想read，还需要重新将文档open
# print target.read()

print "And finally, we close it."
target.close()

# 总的来说，本练习最大的收获在于，开始觉悟用最直接的逻辑关系去考虑代码的前后衔接关系，以后自己写代码时在实现功能上这是写出具有良好逻辑结构的代码的基础
