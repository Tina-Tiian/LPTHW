from sys import argv
from os.path import exists # 此处打开新姿势 exists()，执行后对应True或False两种结果，有或无，存在或不存在
#（嗯。。。有点哲学意味，跟新朋友打好关系吧，以后还会常见）

script, from_file, to_file = argv

# print "Copying from %s to %s" % (from_file, to_file)
#
# # we could do these two on one line, how?
# in_file = open(from_file)
# indata = in_file.read()
# # 复习一下有关open()的内容：
# # 执行open()默认就是执行read功能
# # 执行open(filename, 'w')时，在打开对应file时，执行read功能并打开 write的权限，亦可打开其他姿(quan)势(xian)
# # 执行open(filename, 'w').write()时，在打开file后直接完成“写”的动作
#
# print "The input file is %d bytes long" % len(indata)
#
# print "Does the output file exists? %r" % exists(to_file)
# print "Ready, hit RETURN to continue, CTRL-C to abort."
# raw_input()
indata = open(from_file).read()


# out_file = open(to_file, 'w')
# out_file.write(indata)
out_file = open(to_file, 'w').write(indata)

# 此处复习一下昨天get到的逻辑技能，捋清楚每个括号内变量的逻辑关系，瘦身代码，”one line”搞定不是事儿～～～
# out_file = open(to_file,'w').write(open(from_file).read())

print "Alright, all done."

# out_file.close() # 当file单独被open()时，需要close(),等同于save
# in_file.close()  # 当file被open().read()或者open().write()时，暂时称之为”具有联合动作“时，已自动save，不用再单独执行close()
