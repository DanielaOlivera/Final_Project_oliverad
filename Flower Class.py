######################################################################
# Author: Daniela Olivera
# Username: oliverad
#
# Assignment: A3: A Pair of Fully Functional Gitty Psychedelic  Robotic Turtles
# Purpose: Introduces the use of functions with the turtle library
######################################################################
# Acknowledgements:
# original from http://openbookproject.net/thinkcs/python/english3e/functions.html
#
# Modifications by Dr. Jan Pearce
# converted to Windows, removed def function, added Screen for clean close
# licensed under a Creative Commons
# Attribution-Noncommercial-Share Alike 3.0 United States License.
#################################################################################
import turtle


class Flower:
    """
    A flower object
    """
    def __init__(self, pos, num, sz):
        """
        The robotic artist needs an inventory to be able to know what type of flower to draw for you
        """
        self.corner = pos          # A Point object to hold the bottom left corner of the rectangle
        self.petals = num          # Number of petals
        self.size = sz             # Length of each side on petal
        self.turtle = turtle.Turtle()

    def triangle_petals(self, sz):
        """
        Make a multi-color triangle
        :param sz: size of a side of the triangle
        :return: None
        """
        for i in ["black", "silver", "blue"]:
            self.turtle.color(i)
            self.turtle.forward(sz)
            self.turtle.left(360/3)
            self.turtle.speed(10)

    def pentagon_petals(self, sz):
        """
        Make a multi-color pentagon
        :param sz: size of a side of the pentagon
        :return: None
        """
        for i in ["black", "white", "purple", "violet", "olive"]:
            self.turtle.color(i)
            self.turtle.forward(sz)
            self.turtle.left(360/5)
            self.turtle.speed(10)

    def grow_flower_a(self, size):
        """
        Draw a flower on the bottom right side of the screen
        :param size: size
        :return: None
        """
        self.turtle.penup()
        self.turtle.setpos(30, -47)

        for i in range(8):          # Make ella draw 8 semi-circular sets of triangles creating a big circle
            self.turtle.penup()
            self.turtle.right(45)
            self.turtle.forward(70)
            self.turtle.pendown()
            for i in range(12):     # Make ella draw 12 triangles on each set of triangles
                self.triangle_petals(size)
                self.turtle.forward(5)
                self.turtle.right(15)

    def grow_flower_b(self, size):
        """
        Draw a flower on the upper left side of the screen
        :param size: size
        :return: None
        """
        self.turtle.penup()
        self.turtle.setpos(-200, 100)
        for i in range(9):          # Make dani draw 9 semi-circular sets of pentagons creating a big circle
            self.turtle.speed(10)
            self.turtle.penup()
            self.turtle.right(45)
            self.turtle.forward(70)
            self.turtle.pendown()
            for i in range(12):     # Make dani draw 12 pentagons on each set of polygons
                self.pentagon_petals(size)
                self.turtle.forward(3)
                self.turtle.right(13)

    def grow_steams(self):
        """
        Make steams for flowers
        :param t: a turtle object
        :return: None
        """
        self.turtle.color('#DD6213')
        self.turtle.pensize(5)
        self.turtle.penup()
        self.turtle.setpos(-40, -165)
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


def main():
    """
    Makes two flowers with geometric patterns.
    :return: None
    """
    wn = turtle.Screen()            # Makes a new turtle screen
    wn.bgcolor("green")             # Set up screen color
    #wn.bgpic("giphy.gif")
    dani = Flower(pos=0, num=3, sz=4)
    size = 5
    dani.grow_flower_a(size)
    dani.grow_flower_b(size)
    dani.grow_steams()
    wn.exitonclick()

main()
# Things to do next:
# Add circles at center of flower by using even (onclick)
# make it interactive
# use point class for coordinate point or maybe onclick?
# use background picture of grass or something like that
# add butterflies
# modify steams so that they have starting and ending position maybe?
