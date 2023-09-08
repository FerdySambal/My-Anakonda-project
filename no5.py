import turtle as tt
import random

# Set up the Turtle screen
screen = tt.Screen()
screen.bgcolor("white")

# Create a Turtle object
artist = tt.Turtle()
artist.speed(0)  # Set the drawing speed (0 is the fastest)

# Function to draw a colorful spiral pattern
def draw_spiral(num_lines, line_length, angle_increment):
    colors = ["red", "orange", "yellow", "green", "blue", "purple"]
    for _ in range(num_lines):
        artist.color(random.choice(colors))
        artist.forward(line_length)
        artist.right(90)
        line_length += 5
        artist.right(angle_increment)

# Function to draw a random colorful star
def draw_random_star(size):
    colors = ["red", "orange", "yellow", "green", "blue", "purple"]
    artist.color(random.choice(colors))
    artist.begin_fill()
    for _ in range(5):
        artist.forward(size)
        artist.right(144)
    artist.end_fill()

# Function to draw a colorful circular pattern
def draw_circular_pattern(num_circles, circle_radius, angle_increment):
    colors = ["red", "orange", "yellow", "green", "blue", "purple"]
    for _ in range(num_circles):
        artist.color(random.choice(colors))
        artist.circle(circle_radius)
        artist.right(angle_increment)

# Draw a colorful spiral pattern
artist.penup()
artist.goto(0, 0)
artist.pendown()
draw_spiral(50, 10, 15)

# Draw random colorful stars
for _ in range(10):
    x = random.randint(-300, 300)
    y = random.randint(-300, 300) 
    artist.penup()
    artist.goto(x, y)
    artist.pendown()
    draw_random_star(random.randint(10, 50))

# Draw a colorful circular pattern
artist.penup()
artist.goto(0, 0)
artist.pendown()
draw_circular_pattern(12, 100, 30)

# Hide the Turtle
artist.hideturtle()

# Keep the window open
tt.done()