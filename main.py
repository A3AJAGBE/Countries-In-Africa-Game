import turtle

# Screen default swt up
screen = turtle.Screen()
screen.setup(width=600, height=800)
screen.title("Name the Countries in Africa")

# Add image as the background
image = "plain_map_of_africa.gif"
screen.addshape(image)
turtle.shape(image)


# Get the x and y coordinates
def mouse_click_coor(x, y):
    print(x, y)


turtle.onscreenclick(mouse_click_coor)
turtle.mainloop()

# Keep the screen open until exited
# screen.exitonclick()