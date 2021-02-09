import turtle

# Screen default swt up
screen = turtle.Screen()
screen.setup(width=600, height=800)
screen.title("Name the Countries in Africa")

# Add image as the background
image = "africa.gif"
screen.addshape(image)
turtle.shape(image)

# Keep the screen open until exited
screen.exitonclick()
