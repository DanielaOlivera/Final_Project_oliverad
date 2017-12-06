######################################################################
# Author: Daniela Olivera
# Username: oliverad
#
# Assignment: Final Project
# Purpose: Introduces the use of functions with the turtle library
######################################################################
# Acknowledgements:
# Scott Heggen
#################################################################################
import turtle


class Flower:
    """
    A flower object
    """
    def __init__(self, pos, num=0, sz=0):
        """
        The robotic artist needs an inventory to be able to know what type of flower to draw for you
        """
        self.corner = pos          # A Point object to hold the bottom left corner of the rectangle
        self.petal_sides = num      # To save place to store the number of sides in each petal
        self.size = sz             # To save place to store the length of each side on petal
        self.turtle = turtle.Turtle()

    def user_set_size(self):
        self.size = int(input("Enter petal size: [2-20]"))

    def angle_calculator(self):
        """
        Calculates and returns angle based on number of sides
        :return: angle
        """
        angle = 360/self.petal_sides
        return angle

    def triangle_petals(self):
        """
        Make a multi-color triangle
        :return: None
        """
        self.petal_sides = 3
        for i in ["black", "silver", "blue"]:
            self.turtle.color(i)
            self.turtle.forward(self.size)
            self.turtle.left(self.angle_calculator())
            self.turtle.speed(10)

    def pentagon_petals(self):
        """
        Make a multi-color pentagon
        :return: None
        """
        self.petal_sides = 5
        for i in ["black", "white", "purple", "violet", "olive"]:
            self.turtle.color(i)
            self.turtle.forward(self.size)
            self.turtle.left(self.angle_calculator())
            self.turtle.speed(10)

    def grow_flower_a(self):
        """
        Draw a flower on the bottom right side of the screen
        :return: None
        """
        self.turtle.penup()
        self.turtle.goto(self.corner.x, self.corner.y)

        for i in range(8):          # Make ella draw 8 semi-circular sets of triangles creating a big circle
            self.turtle.penup()
            self.turtle.right(45)
            self.turtle.forward(70)
            self.turtle.pendown()
            for i in range(12):     # Make ella draw 12 triangles on each set of triangles
                self.triangle_petals()
                self.turtle.forward(5)
                self.turtle.right(15)

    def grow_flower_b(self):
        """
        Draw a flower on the upper left side of the screen
        :return: None
        """
        self.turtle.penup()
        self.turtle.goto(self.corner.x, self.corner.y)
        for i in range(9):          # Make dani draw 9 semi-circular sets of pentagons creating a big circle
            self.turtle.speed(10)
            self.turtle.penup()
            self.turtle.right(45)
            self.turtle.forward(70)
            self.turtle.pendown()
            for i in range(12):     # Make dani draw 12 pentagons on each set of polygons
                self.pentagon_petals()
                self.turtle.forward(3)
                self.turtle.right(13)

    def flower_center(self, x, y):
        """
        Make flower center
        :param x: x coordinate position
        :param y: y coordinate position
        :return: None
        """
        self.turtle.hideturtle()
        self.turtle.shape("circle")
        self.turtle.pensize(200)
        self.turtle.color("yellow")
        self.turtle.penup()
        self.turtle.goto(x, y)
        self.turtle.stamp()

    def grow_steams(self):
        """
        Make steams for flowers
        :param t: a turtle object
        :return: None
        """
        self.turtle.color('#DD6213')
        self.turtle.pensize(5)
        self.turtle.penup()
        self.turtle.setpos(-45, -165)
        self.turtle.right(90)
        self.turtle.pendown()
        for i in range(3):     # draw small steam
            self.turtle.forward(-33)
            self.turtle.right(30)
        self.turtle.penup()
        for i in range(2):     # go back to create an intersection point between the large and small steams
            self.turtle.right(-30)
            self.turtle.forward(35)
        self.turtle.right(135)
        self.turtle.pendown()
        for i in range(3):     # draw large steam
            self.turtle.forward(67)
            self.turtle.right(-23)

    # not part of flower class
    # def make_text(self, shape, txt):
    #     """
    #     writes text.
    #     :param shape: a turtle object
    #     :return: None
    #     """
    #     shape.penup()
    #     shape.color("#E93A63")
    #     shape.setpos(70,120)
    #     shape.pendown()
    #     shape.write(txt,move=False,align='center',font=("Arial", 30, ("bold","normal")))
# end class

# Things to do next:
# Add circles at center of flower by using even (onclick)
# make it interactive
# use point class for coordinate point or maybe onclick? OK
# use background picture of grass or something like that
# background could change on key
# add butterflies
# modify steams so that they have starting and ending position maybe?
# user draws steams himself?
