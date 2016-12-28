from sys import argv

# script, user_name = argv
# prompt = '> '

# print "Hi %s, I'm the %s script." % (user_name, script)
# print "I'd like to ask you a few questions."
# print "Do you like me %s?" % user_name
# likes = raw_input(prompt)

# print "Where do you live %s?" % user_name
# lives = raw_input(prompt)

# print "What kind of computer do you have?"
# computer = raw_input(prompt)

# print """
# Alright, so you said %r about liking me.
# You live in %r. Not sure where that is.
# And you have a %r computer. Nice.
# """ % (likes, lives, computer)


# study drills
script, hey_you, siri = argv
prompt = "Tell me here: "

print "Hi %s, I'm the %s script, have you talked with %s yet?" % (hey_you, script, siri)
talk = raw_input(prompt)
print "Good, then you have known her new song." # here is a PPAP fun
song_name = raw_input(prompt)

print """
Well, %s, you're so calm when you say %r.
When I knew %s could sing %r, I couldn't stop laughting.
hia~hia~hia~hia~hia~
""" % (hey_you, talk, siri, song_name)
