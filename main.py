# !usr/bin/python3

# Pong Game
"""
documentation
"""

# Modules
import turtle as tur

# Creating main screen
wn = tur.Screen()


# Basic game structures
class Window:
    """
    In this class I did all the objects as well as window settings.
    (all objects in this class are made statically)
    """

    @staticmethod
    def window():
        """
        In this function, the initial settings of the game window are made
        """
        wn.title("Pong By V.road")
        wn.bgcolor("black")
        wn.setup(width=950, height=650)
        wn.tracer(0)

    @staticmethod
    def create():
        """
        All functions are called and executed here, and create objects
        """
        # WindowAndObjects.game_objects()
        Window.window()


class ObjectsAndMovement:
    """
    bla bla
    """

    @staticmethod
    def paddle_1():
        """
        All game objects, paddle one and paddle two, as well as the ball,
        are made and adjusted in this function
        """
        # Paddle 1

        paddle_1 = tur.Turtle()
        global paddle_1
        paddle_1.speed(0)
        paddle_1.shape("square")
        paddle_1.color("white")
        paddle_1.shapesize(stretch_wid=5, stretch_len=0.8)
        paddle_1.penup()
        paddle_1.goto(-453, 0)
        # return paddle_1


    @staticmethod
    def paddle_2():
        # Paddle 2
        paddle_2 = tur.Turtle()
        paddle_2.speed(0)
        paddle_2.shape("square")
        paddle_2.color("white")
        paddle_2.shapesize(stretch_wid=5, stretch_len=0.9)
        paddle_2.penup()
        paddle_2.goto(445, 0)
        return paddle_2

    @staticmethod
    def ball():
        # Ball
        ball = tur.Turtle()
        ball.speed(0)
        ball.shape("square")
        ball.color("white")
        ball.penup()
        ball.goto(0, 0)

        return ball

    @staticmethod
    def paddle_1_up():
        paddle = ObjectsAndMovement.paddle_1()
        y = paddle.ycor()
        y += 20
        paddle.sety(y)

    @staticmethod
    def paddle_1_down():
        paddle = ObjectsAndMovement.paddle_1()
        y = paddle.ycor()
        y -= 20
        paddle.sety(y)

    @staticmethod
    def paddle_2_up():
        paddle = ObjectsAndMovement.paddle_2()
        y = paddle.ycor()
        y += 20
        paddle.sety(y)

    @staticmethod
    def paddle_2_down():
        paddle = ObjectsAndMovement.paddle_2()
        y = paddle.ycor()
        y -= 20
        paddle.sety(y)

    @staticmethod
    def Create():
        ObjectsAndMovement.paddle_1()
        ObjectsAndMovement.paddle_2()
        ObjectsAndMovement.ball()


class Control:
    """
    this is for control
    """

    # def __init__(self, paddle_1_up, paddle_1_down, paddle_2_up, paddle_2_down):
    #     self.paddle_1_up = paddle_1_up
    #     self.paddle_1_down = paddle_1_down
    #     self.paddle_2_up = paddle_2_up
    #     self.paddle_2_down = paddle_2_down

    @staticmethod
    def keyboardBinding():
        wn.listen()
        wn.onkeypress(ObjectsAndMovement.paddle_1_up, "w")
        wn.onkeypress(ObjectsAndMovement.paddle_1_down, "s")
        wn.onkeypress(ObjectsAndMovement.paddle_2_up, "p")
        wn.onkeypress(ObjectsAndMovement.paddle_2_down, ";")

if __name__ == '__main__':
    ObjectsAndMovement.Create()
    Window.create()
    Control.keyboardBinding()
    wn.mainloop()
