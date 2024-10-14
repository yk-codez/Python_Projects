
from turtle import Turtle
import random

class Food(Turtle):

# allow Food class to inherit methods and functions from the Turtle class
    def __init__(self):
        super().__init__()

        self.shape('circle')
        self.penup()
        self.shapesize(stretch_len=.8, stretch_wid=.8)
        self.color('red')
        self.speed('fastest')
        self.refresh()

    def refresh(self):
        
        self.goto(x=random.randint(-280,280), y=random.randint(-280,280))
