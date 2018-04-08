#Branch 1 removing my_ from variable names.
name = 'Amigo'
age = 30
height = 170 #Cm
height_in_inches = height*0.393701
weight = 88 #KGs
weight_in_pounds = weight*2.20462
eyes = 'Brown'
teeth = 'White'
hair = 'Black'

print ("Let's talk about %s." % name)
print ("He's %r centimeters tall which is %f inches" % (height,height_in_inches))
print ("He's %d kilos weight which is %f pounds." % (weight,weight_in_pounds))
print ("Actually that's not too heavy.")
print ("He's got %s eyes and %s colored hair." % (eyes,hair))
print ("He's got %s teeth." % teeth)

#Tricky part
print ("If i add %d,%d,%d, I'd get %d" % (age,height,weight,age+height+weight))
