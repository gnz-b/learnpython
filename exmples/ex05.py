my_name = 'zhubin'
my_age = 23
my_height = 173
my_weight = 70
my_eyes = 'Black'
my_teeth = 'White'
my_hair = 'Black'

my_float = round(1.77777)

print "Let's talk about %r." % my_name
print "He's %r centimeters tall." % my_height
print "He's %d kilos heavy." % my_weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (my_eyes, my_hair)
print "His teeth are usually %s depending on the coffee." % my_teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d" % (
	my_age, my_height, my_weight, my_age + my_height + my_weight
)	
print "my_float is", my_float