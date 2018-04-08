#Branch 1 removing my_ from variable names.
name = 'Amigo'
age = 30
height = 170 #Cm
weight = 75 #KGs
eyes = 'Brown'
teeth = 'White'
hair = 'Black'

print ("Let's talk about %s." % name)
print ("He's %s centimeters tall." % height)
print ("He's %s kilos weight." % weight)
print ("Actually that's not too heavy.")
print ("He's got %s eyes and %s colored hair." % (eyes,hair))
print ("He's got %s teeth." % teeth)

#Tricky part
print ("If i add %d,%d,%d, I'd get %d" % (age,height,weight,age+height+weight))
