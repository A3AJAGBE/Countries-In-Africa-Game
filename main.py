import turtle
import pandas as pd

# Screen default swt up
screen = turtle.Screen()
screen.setup(width=600, height=800)
screen.title("Name the Countries in Africa")

# Add image as the background
image = "plain_map_of_africa.gif"
screen.addshape(image)
turtle.shape(image)

# Read the cvs file
data = pd.read_csv("countries_in_africa.csv")
countries_list = data.Country.to_list()
guessed_countries = []

# Keep iterating until the map is fully labeled
while len(guessed_countries) < 54:
    guess = screen.textinput(title="Label the Map", prompt="Guess a country in africa").title()
    print(guess)

    # Check the user guess with the data in the csv file
    if guess in countries_list:
        guessed_countries.append(guess)
        # Instantiate the turtle class
        sample = turtle.Turtle()
        sample.hideturtle()
        sample.penup()
        # Get the guess coordinates
        country_coordinates = data[data.Country == guess]
        # Get the go to the coordinates
        sample.goto(int(country_coordinates.X), int(country_coordinates.Y))
        # Label the map
        sample.write(country_coordinates.Country.item())


"""# Get the x and y coordinates
def mouse_click_coor(x, y):
    print(x, y)


turtle.onscreenclick(mouse_click_coor)
turtle.mainloop()"""

# Keep the screen open until exited
screen.exitonclick()
