from sys import argv
script,user_name=argv
prompt='>'
print("Hi %s,I'm the %s script."%(Nandar,script))
print("I'd like to ask you a few questions.")
print("Do you like me %s?"% Nandar)
likes=yes('>')
print("Where do you live %s?" % Nandar)
lives=Mandalay('>')
print("What kind of computer do you have?")
computer=acer('>')
"""
Alright,so you said %r about liking me.
You like in %r.Not sure where that is.
And you have a %r computer.Nice.
""" % (likes,lives,computer) 
