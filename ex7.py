# -*- coding: utf-8 -*-
print "Mary had a little lamb."
print "Its fleece was white as %s." % 'snow'
print "And everywhere that Mary went."
print "." * 10 # what'd that do? 此处练习：字符*数字，可以让该字符重复出现相应次数

end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

# watch that comma at the end. try removing it to see what happens
print end1 + end2 + end3 + end4 + end5 + end6,
print end7 + end8 + end9 + end10 + end11 + end12

# 上面的练习中，逗号起到连接的作用，没有逗号，会分开两行显示，即默认情况下，不同行的代码会分段显示；
# 加上逗号，会让两行代码连续显示，即不再自动分段，代码中逗号的位置运行后显示为空格,
# 可以区分 ex6 中用 “+” 连接的方式，是连续的，没有空格的
print end1 + end2 + end3 + end4 + end5 + end6
print end7 + end8 + end9 + end10 + end11 + end12
