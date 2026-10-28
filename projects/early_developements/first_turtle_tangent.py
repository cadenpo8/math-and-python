"""
Making a circle and Tracy will draw a derivative on part of the circle
"""
def derivative():
    forward(70)
    backward(140)
    seth(0)

def goto_c():
    penup()
    goto(0, -100)


def goto_b():
    penup()
    goto(0, -150)
    
def derivative_b():
    forward(105)
    backward(210)
    seth(0)

def radius2():
    forward(200)
    backward(400)


speed(0)
pensize(2)
goto_c()
pendown()
circle(100)

# Drawing first derivative at the lowest point of the Circle (1st)
derivative()

# Next point of Derivative at far right of the circle (2nd)
goto_c()
circle(100, 90)
pendown()
seth(90)
derivative()

# Making the 3rd Derivative at peak circle height (3rd)
goto_c()
circle(100, 180)
pendown()
seth(0)
derivative()

# Making 4th Derivative and far left of the circle (4th)
goto_c()
circle(100, 270)
pendown()
seth(90)
derivative()



# Making Derivatives at 4 points where the degrees 45 in the circle (5-8)
goto_c()
circle(100, 45)
seth(45)
pendown()
derivative()



goto_c()
circle(100, 135)
seth(135)
pendown()
derivative()



goto_c()
circle(100, 225)
pendown()
seth(225)
derivative()



goto_c()
circle(100, 315)
seth(315)
pendown()
derivative()



# Making the LAST 8 derivatives
goto_c()
circle(100, 22.5)
pendown()
seth(30)
derivative()


goto_c()
circle(100, 67.5)
pendown()
seth(60)
derivative()


goto_c()
circle(100, 112.5)
pendown()
seth(120)
derivative()


goto_c()
circle(100, 157.5)
pendown()
seth(150)
derivative()


goto_c()
circle(100, 202.5)
pendown()
seth(210)
derivative()


goto_c()
circle(100, 247.5)
pendown()
seth(240)
derivative()


goto_c()
circle(100, 292.5)
pendown()
seth(300)
derivative()


goto_c()
circle(100, 337.5)
pendown()
seth(330)
derivative()







# making one quick thing
penup()
goto(0, -150)
seth(0)
pendown()
circle(150)



"""
This is the start of one more
"""


# Drawing first derivative at the lowest point of the Circle (1st)
derivative()

# Next point of Derivative at far right of the circle (2nd)
goto_b()
circle(150, 90)
pendown()
seth(90)
derivative_b()

# Making the 3rd Derivative at peak circle height (3rd)
goto_b()
circle(150, 180)
pendown()
seth(0)
derivative_b()

# Making 4th Derivative and far left of the circle (4th)
goto_b()
circle(150, 270)
pendown()
seth(90)
derivative_b()



# Making Derivatives at 4 points where the degrees 45 in the circle (5-8)
goto_b()
circle(150, 45)
seth(45)
pendown()
derivative_b()



goto_b()
circle(150, 135)
seth(135)
pendown()
derivative_b()



goto_b()
circle(150, 225)
pendown()
seth(225)
derivative_b()



goto_b()
circle(150, 315)
seth(315)
pendown()
derivative_b()



# Making the LAST 8 derivatives
goto_b()
circle(150, 22.5)
pendown()
seth(30)
derivative_b()


goto_b()
circle(150, 67.5)
pendown()
seth(60)
derivative_b()


goto_b()
circle(150, 112.5)
pendown()
seth(120)
derivative_b()


goto_b()
circle(150, 157.5)
pendown()
seth(150)
derivative_b()


goto_b()
circle(150, 202.5)
pendown()
seth(210)
derivative_b()


goto_b()
circle(150, 247.5)
pendown()
seth(240)
derivative_b()


goto_b()
circle(150, 292.5)
pendown()
seth(300)
derivative_b()


goto_b()
circle(150, 337.5)
pendown()
seth(330)
derivative_b()




# and making radius

penup()
goto(0, 0)
seth(0)
pendown()
radius2()
penup()
goto(0, 0)
seth(90)
pendown()
radius2()

goto(0, 0)
seth(45)
radius2()

goto(0, 0)
seth(135)
radius2()

goto(0,0)
seth(22.5)
radius2()

goto(0,0)
seth(67.5)
radius2()

goto(0,0)
seth(112.5)
radius2()

goto(0,0)
seth(157.5)
radius2()
