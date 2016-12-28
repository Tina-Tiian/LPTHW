tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

# study drills
tabby_cat = "\aI'm tabbed in."
persian_cat = "I'm split\non a\b line."
backslash_cat = "\fI'm \\ a \\ cat."

fat_cat = '''
I'll do a list:
\v* Cat food
\v* Fishies
\v* Catnip\n\v* Grass
'''

print "%s\n%s" % (tabby_cat,backslash_cat)
print persian_cat
print fat_cat

# a little for fun(with dead ending, 2333333333333)
while True:
    for i in ["/","-","|","\\","|"]:
        print "%r\r" % i,
        print "%s\r" % i,
