#ELI PRUSHANSKY 121019
import turtle
import math

angle=input("what angle")
angle=int(angle)
mass=input("what mass")
mass=int(mass)
hypotenuse=100/math.cos(angle*(math.pi)/180)

#The first turtle in the program draws a hill with an angle input by the user
hill=turtle.Turtle()
hill.ht()
hill.forward(100)
hill.left(90)
hill.forward(hypotenuse*math.sin(angle*(math.pi)/180))
hill.left(180-(90-angle))
hill.forward(hypotenuse)

#The second turtle in the program draws a box parallel to the hill using measurements input by the user
box=turtle.Turtle()
box.ht()
box.left(angle)
box.forward((hypotenuse/2)+17.5)
box.left(90)
box.forward(27)
box.left(90)
box.forward(35)
box.left(90)
box.forward(27)

#The third turtle in the program draws a vector perpendicular to the hill from the center of the box to indicate normal force
nforce=turtle.Turtle()
nforce.ht()
nforce.up()
nforce.left(angle)
nforce.forward(hypotenuse/2)
nforce.left(90)
nforce.forward(13.5)
nforce.color("blue","blue")
nforce.down()
nforce.st()
nforce.forward(80)

#The fourth turtle in the program writes the measured normal force of a box on a hill using user input for the mass of the box and angle of the hill
nforce2=turtle.Turtle()
nforce2.ht()
nforce2.up()
nforce2.left(angle)
nforce2.forward(hypotenuse/2)
nforce2.left(90)
nforce2.forward(93.5)
nforce2.left(90-angle)
nforce2.forward(80)
nforce2.down()
nforce2.write("n = "+str(round((mass*9.8*math.cos(angle*math.pi/180)),3)), font=("Garamond", 16, "normal"))

#The fifth turtle in the program draws a vector due south of the box to indicate the weight of the box
weight=turtle.Turtle()
weight.ht()
weight.up()
weight.left(angle)
weight.forward(hypotenuse/2)
weight.left(90)
weight.forward(13.5)
weight.right(angle+180)
weight.color("red","red")
weight.down()
weight.st()
weight.forward(hypotenuse/1.5)

#The sixth turtle in the program writes the measured weight of the box using user input for the mass of the box
weight2=turtle.Turtle()
weight2.ht()
weight2.up()
weight2.left(angle)
weight2.forward(hypotenuse/2)
weight2.left(90)
weight2.forward(13.5)
weight2.right(angle+180)
weight2.forward(hypotenuse/1.5)
weight2.left(90)
weight2.forward(10)
weight2.down()
weight2.write("n = "+str(round((mass*9.8),3)), font=("Garamond", 16, "normal"))
