my_name = 'Zed A. Shaw'
my_age = 35 # not a lie
my_height = 74 # inches
my_weight = 180 # lbs
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Brown'

# 此节练习用 %s、%d、%r 等格式化字符，将变量嵌入字符中间
# 要注意行末引用变量的数量要与前面嵌入的 格式化字符 的数量相对应
print "Let's talk about %s." % my_name
print "He's %d inches tall." % my_height
print "He's %d pounds heavy." % my_weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (my_eyes, my_hair)
print "His teeth are usually %s depending on the coffee." % my_teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (my_age, my_height, my_weight, my_age + my_height + my_weight)


# Study Drills practise
name = 'Zed A. Shaw'
age = 35
height = 74 # inches
height_cm = round(height * 2.54)
weight = 180 # lbs
weight_kg = round(weight * 0.4536)
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print "Let's talk about %r." % name
print "He's %r centimeters tall." % height_cm
print "He's %r kilograms heavy." % weight_kg
print "Actually that's not too heavy."
print "He's got %r eyes and %r hair." % (eyes, hair)
print "His teeth are usually %r depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %r, %r, and %r I get %r." % (age, height_cm, weight_kg, age + height_cm + weight_kg)
