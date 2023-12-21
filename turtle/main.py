import turtle

# make a snowflake using stars and squares
# this is a function that makes a star

# colour it blue
turtle.color("teal")
# fill it blue
turtle.begin_fill()

# set bg to purple
turtle.bgcolor("purple")

def star():
    for _ in range(5):
        # make it large
        turtle.pensize(5)
        turtle.forward(50)
        turtle.right(144)

def snowflake():
    for _ in range(5):
        star()
        # fill it teal
        turtle.color("teal")
        turtle.begin_fill()
        turtle.right(144)

for _ in range(6):
    snowflake()
    turtle.right(60)