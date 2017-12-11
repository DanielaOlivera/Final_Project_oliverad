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
        Creates flowers at a starting position
        """
        self.initial_position = pos  # A Point object to hold the starting position
        self.petal_sides = num       # To save place to store the number of sides in each petal
        self.size = sz               # To save place to store the length of each side on petal
        self.turtle = None           # To save space we only create a turtle if and when grow_flower() is used

    def user_set_size(self):
        """
        Asks user for the size of internal shape in each petal
        :return: None
        """
        self.size = int(input("Enter petal size: [2-10] \n"))

    def user_set_shape_petals(self):
        """
        Asks user for number of sides in each petal
        :return: None
        """
        self.petal_sides = int(input("Enter number of sides in each petal: [3/5] \n"))

    def angle_calculator(self):
        """
        Calculates and returns angle based on number of sides
        :return: angle
        """
        if type(self.petal_sides) == int:
            angle = 360/self.petal_sides
            return angle    # if number of sides is an integer calculate the angle and return it
        else:
            return "Error"    # if number of sides is not an integer, it returns Error

    def triangle_petals(self):
        """
        Make a multi-color triangle
        :return: None
        """
        for i in ["black", "turquoise", "blue"]:
            self.turtle.color(i)  # i is one of three elements
            self.turtle.pensize(3)
            self.turtle.forward(self.size)  # turtle travels the distance given by the user
            self.turtle.left(self.angle_calculator())   # turtle turns the angle calculated from number of sides
            self.turtle.speed(0)        # fastest speed

    def pentagon_petals(self):
        """
        Make a multi-color pentagon
        :return: None
        """
        for i in ["crimson", "white", "salmon", "purple", "deeppink"]:
            self.turtle.color(i)   # i is one of five elements
            self.turtle.pensize(3)
            self.turtle.forward(self.size)  # turtle travels the distance given by the user
            self.turtle.left(self.angle_calculator())   # turtle turns the angle calculated from number of sides
            self.turtle.speed(0)    # fastest speed

    def grow_steams(self):
        """
        Make steams for flowers
        :return: None
        """
        self.turtle.color('#8B4513')
        self.turtle.pensize(7)
        self.turtle.penup()
        self.turtle.goto(self.initial_position.x + 30, self.initial_position.y - 90)
        self.turtle.right(90)
        self.turtle.pendown()

        for i in range(3):     # draw large part of steam
            self.turtle.forward(50)
            self.turtle.right(-20)
        # draw small part of steam
        for i in range(2):
            self.turtle.right(20)
            self.turtle.forward(-50)
        self.turtle.right(135)
        self.turtle.forward(20)
        # stamp a little leaf
        self.turtle.shapesize(2)
        self.turtle.color("green")
        self.turtle.stamp()

    def grow_flower_a(self):
        """
        Draw a flower with triangular petals
        :return: None
        """
        self.turtle = turtle.Turtle()
        self.turtle.penup()
        self.turtle.goto(self.initial_position.x, self.initial_position.y)
        self.turtle.begin_fill()
        for i in range(8):          # Make ella draw 8 semi-circular sets of triangles creating a flower
            self.turtle.penup()
            self.turtle.right(45)
            self.turtle.forward(70)
            self.turtle.pendown()
            for t in range(12):     # Make ella draw 12 triangles on each set of triangles
                self.triangle_petals()
                self.turtle.forward(5)
                self.turtle.right(15)
        self.turtle.color("lightblue")
        self.turtle.end_fill()
        self.grow_steams()

    def grow_flower_b(self):
        """
        Draw a flower whose petals are pentagons
        :return: None
        """
        self.turtle = turtle.Turtle()
        self.turtle.penup()
        self.turtle.goto(self.initial_position.x, self.initial_position.y)
        self.turtle.begin_fill()
        for i in range(9):          # Make dani draw 9 semi-circular sets of pentagons creating a flower
            self.turtle.penup()
            self.turtle.right(45)
            self.turtle.forward(70)
            self.turtle.pendown()
            for t in range(12):     # Make dani draw 12 pentagons on each set of polygons
                self.pentagon_petals()
                self.turtle.forward(3)
                self.turtle.right(13)
        self.turtle.color("plum")
        self.turtle.end_fill()
        self.grow_steams()

    def flower_center(self, x, y):
        """
        Stamp a flower center
        :param x: x coordinate position
        :param y: y coordinate position
        :return: None
        """
        self.turtle.hideturtle()
        self.turtle.shape("circle")
        self.turtle.shapesize(2)
        self.turtle.color("yellow")
        self.turtle.penup()
        self.turtle.goto(x, y)
        self.turtle.stamp()

# end class
