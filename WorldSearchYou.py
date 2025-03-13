import turtle
import time

# Define draw functions for each object

def draw_table():
    turtle.clear()
    turtle.penup()
    turtle.goto(-100, 0)  # Start position adjusted for bigger table
    turtle.pendown()
    turtle.fillcolor("brown")
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(200)  # Increased table width
        turtle.right(90)
        turtle.forward(100)  # Increased table height
        turtle.right(90)
    turtle.end_fill()

    # Table legs
    for x in [-80, 80]:  # Adjusted leg positions for larger table
        turtle.penup()
        turtle.goto(x, -100)  # Adjusted leg height
        turtle.pendown()
        turtle.begin_fill()
        for _ in range(2):
            turtle.forward(20)  # Increased leg width
            turtle.right(90)
            turtle.forward(50)  # Increased leg height
            turtle.right(90)
        turtle.end_fill()


def draw_eggplant():
    turtle.clear()

    # Draw the larger purple body
    turtle.penup()
    turtle.goto(0, -150)  # Start lower for a bigger eggplant
    turtle.pendown()
    turtle.fillcolor("purple")
    turtle.begin_fill()
    turtle.setheading(0)
    turtle.circle(80, steps=100)  # Create an oval for the body
    turtle.setheading(90)
    turtle.circle(120, steps=100)  # Create the top part
    turtle.end_fill()

    # Draw the larger green top
    turtle.penup()
    turtle.goto(0, 20)  # Position for the top
    turtle.pendown()
    turtle.fillcolor("green")
    turtle.begin_fill()
    turtle.setheading(0)
    for _ in range(5):  # Draw the green calyx with petals
        turtle.circle(30, steps=3)
        turtle.left(72)
    turtle.end_fill()

    # Draw the stem
    turtle.penup()
    turtle.goto(0, 20)  # Position for the stem
    turtle.setheading(90)
    turtle.pendown()
    turtle.fillcolor("green")
    turtle.begin_fill()
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(15)
    turtle.right(90)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(15)
    turtle.end_fill()


def draw_cat():
    turtle.clear()
    # Head
    turtle.penup()
    turtle.goto(0, 70)  # Moved the head lower for a bigger size
    turtle.pendown()
    turtle.fillcolor("pink")
    turtle.begin_fill()
    turtle.circle(100)  # Increased head size
    turtle.end_fill()

    # Ears
    for x in [-60, 50]:  # Adjusted ear positions
        turtle.penup()
        turtle.goto(x, 0)
        turtle.pendown()
        turtle.fillcolor("pink")
        turtle.begin_fill()
        turtle.goto(x - 30, 110)  # Increased ear height
        turtle.goto(x + 30, 0)  # Adjusted ear width
        turtle.end_fill()

    # Eyes
    for x in [-40, 40]:  # Adjusted eye positions
        turtle.penup()
        turtle.goto(x, -40)
        turtle.pendown()
        turtle.fillcolor("black")
        turtle.begin_fill()
        turtle.circle(10)  # Increased eye size
        turtle.end_fill()

    # Nose
    turtle.penup()
    turtle.goto(0, -60)  # Adjusted nose position
    turtle.pendown()
    turtle.fillcolor("red")
    turtle.begin_fill()
    turtle.circle(6)  # Increased nose size
    turtle.end_fill()

    # Mouth
    turtle.penup()
    turtle.goto(-20, -80)  # Adjusted mouth position
    turtle.setheading(-60)
    turtle.pendown()
    turtle.circle(20, 120)  # Increased mouth arc size

    # Whiskers
    for y in [-50, -60, -70]:  # Adjusted whisker positions
        for x in [-1, 1]:
            turtle.penup()
            turtle.goto(0, y)
            turtle.pendown()
            turtle.setheading(0 if x > 0 else 180)
            turtle.forward(80)  # Increased whisker length





def draw_meow_text_repeatedly(times):
    for _ in range(times):
        turtle.penup()
        turtle.goto(0, 10)  # Positioning above the mouth
        turtle.color("blue")
        turtle.write("Meow", align="center", font=("Comic Sans MS", 16, "bold"))
        time.sleep(0.5)  # Pause briefly between repetitions

def draw_hiss_text_repeatedly(times):
    for _ in range(times):
        turtle.penup()
        turtle.goto(0, -10)  # Position below the cat's mouth
        turtle.color("red")
        turtle.write("Hiss", align="center", font=("Comic Sans MS", 16, "bold"))
        time.sleep(0.5)
        turtle.undo()  # Remove the text without clearing the cat

def draw_dope(times):
    for _ in range(times):
        turtle.clear()
        turtle.penup()
        turtle.goto(0, 10)  # Positioning above the mouth
        turtle.color("pink")
        turtle.write("D-O-O-O-P-E", align="center", font=("Comic Sans MS", 48, "bold"))
        time.sleep(0.5)  # Pause briefly between repetitions
        turtle.undo()  # Remove the text without clearing the cat



def draw_steak():
    turtle.clear()
    # Draw the steak base
    turtle.penup()
    turtle.goto(-70, 0)
    turtle.pendown()
    turtle.fillcolor("brown")
    turtle.begin_fill()
    turtle.setheading(45)
    for _ in range(2):
        turtle.circle(70, 90)
        turtle.circle(30, 90)
    turtle.end_fill()

    # Draw the steak texture (inner area)
    turtle.penup()
    turtle.goto(-60, 10)
    turtle.pendown()
    turtle.fillcolor("darkred")
    turtle.begin_fill()
    turtle.circle(30)
    turtle.end_fill()

    # Add marbling (centered on steak)
    turtle.pensize(1)
    turtle.color("white")
    marbling_positions = [
        (-60, 10), (-50, 15), (-55, 5), (-65, -5), (-70, 15)
    ]
    for x, y in marbling_positions:
        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()
        turtle.circle(5, steps=3)

    # Draw the steak grill marks
    turtle.penup()
    turtle.goto(-60, 50)
    turtle.pendown()
    turtle.pensize(2)
    turtle.setheading(-45)
    for _ in range(4):
        turtle.forward(90)
        turtle.penup()
        turtle.backward(90)
        turtle.right(90)
        turtle.forward(15)
        turtle.left(90)
        turtle.pendown()
    turtle.pensize(1)



def draw_flower():
    turtle.clear()
    
    # Draw the stem
    turtle.penup()
    turtle.goto(0, -200)  # Start the stem further down
    turtle.pendown()
    turtle.pensize(5)
    turtle.pencolor("green")
    turtle.setheading(90)  # Point upwards
    turtle.forward(200)  # Lengthen the stem

    # Draw the center of the flower
    turtle.penup()
    turtle.goto(10, 0)
    turtle.pendown()
    turtle.fillcolor("yellow")
    turtle.begin_fill()
    turtle.circle(10)  # Small circle at the center
    turtle.end_fill()

    # Draw the petals
    num_petals = 6
    petal_radius = 30
    turtle.fillcolor("red")
    for i in range(num_petals):
        angle = 360 / num_petals * i
        turtle.penup()
        turtle.goto(0, 0)
        turtle.setheading(angle)
        turtle.forward(20)  # Position petal away from center
        turtle.pendown()
        turtle.begin_fill()
        turtle.circle(petal_radius, steps=5)  # Create petal as pentagon
        turtle.end_fill()


def draw_human():
    turtle.clear()
    turtle.pensize(3)

    
    # Draw head (larger)
    turtle.penup()
    turtle.goto(-30, 95)
    turtle.pendown()
    turtle.fillcolor("#f4c2c2")
    turtle.begin_fill()
    turtle.circle(40)
    turtle.end_fill()
    
    # Draw eyes
    turtle.penup()
    turtle.goto(-15, 140)
    turtle.pendown()
    turtle.fillcolor("black")
    turtle.begin_fill()
    turtle.circle(5)
    turtle.end_fill()
    
    turtle.penup()
    turtle.goto(15, 140)
    turtle.pendown()
    turtle.fillcolor("black")
    turtle.begin_fill()
    turtle.circle(5)
    turtle.end_fill()
    
    # Draw smile
    turtle.penup()
    turtle.goto(-10, 125)
    turtle.pendown()
    turtle.setheading(-60)
    turtle.circle(10, 120)
    
    # Draw body
    turtle.penup()
    turtle.goto(-30, 80)  # Titik awal tubuh di tengah
    turtle.setheading(0)  # Pastikan turtle menghadap kanan sebelum menggambar
    turtle.pendown()
    turtle.fillcolor("#f4a2a2")
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(60)  # Lebar (lebih kecil agar lebih tegak)
        turtle.right(90)
        turtle.forward(100)  # Tinggi (lebih besar agar lebih panjang)
        turtle.right(90)
    turtle.end_fill()
    
    # Draw left arm (larger)
    turtle.penup()
    turtle.goto(-40, 80)
    turtle.pendown()
    turtle.fillcolor("#f4c2a2")
    turtle.begin_fill()
    turtle.goto(-80, 60)
    turtle.goto(-40, 40)
    turtle.goto(-40, 80)
    turtle.end_fill()
    
    # Draw right arm (larger)
    turtle.penup()
    turtle.goto(40, 80)
    turtle.pendown()
    turtle.fillcolor("#f4c2a2")
    turtle.begin_fill()
    turtle.goto(80, 60)
    turtle.goto(40, 40)
    turtle.goto(40, 80)
    turtle.end_fill()
    
    # Draw left leg (larger)
    turtle.penup()
    turtle.goto(-20, -20)
    turtle.pendown()
    turtle.fillcolor("black")
    turtle.begin_fill()
    turtle.goto(-40, -70)
    turtle.goto(0, -70)
    turtle.goto(-20, -20)
    turtle.end_fill()
    
    # Draw right leg (larger)
    turtle.penup()
    turtle.goto(20, -20)
    turtle.pendown()
    turtle.fillcolor("black")
    turtle.begin_fill()
    turtle.goto(40, -70)
    turtle.goto(0, -70)
    turtle.goto(20, -20)
    turtle.end_fill()



def draw_heart():
    turtle.clear()
    turtle.penup()
    
    # Coordinates and sizes for multiple hearts
    heart_positions = [
        (-100, 100, 50), (100, 100, 50),
        (-70, -50, 40), (70, -50, 40),
        (-120, 0, 30), (120, 0, 30),
        (0, 150, 60), (0, -100, 50)
    ]
    
    for x, y, size in heart_positions[:8]:  # Adjust to 4-8 hearts as desired
        turtle.goto(x, y)
        turtle.pendown()
        turtle.fillcolor("red")
        turtle.begin_fill()
        
        turtle.setheading(0)
        turtle.left(50)
        turtle.forward(size)
        turtle.circle(size / 2, 200)
        turtle.right(140)
        turtle.circle(size / 2, 200)
        turtle.forward(size)
        
        turtle.end_fill()
        turtle.penup()

def draw_crosshair(x,y):
    turtle.clear()
    turtle.penup()
    turtle.goto(x - 20, y)
    turtle.pendown()
    turtle.pencolor("red")
    
    # Horizontal line
    turtle.goto(x + 20, y)
    
    # Reset position for vertical line
    turtle.penup()
    turtle.goto(x, y + 20)
    turtle.pendown()
    
    # Vertical line
    turtle.goto(x, y - 20)

    # Draw circle at the center
    turtle.penup()
    turtle.goto(x, y - 5)
    turtle.pendown()
    turtle.circle(5)

def draw_crosshair2():
    positions = [(0, 0), (-100, 100), (100, 100), (-100, -100), (100, -100)]
    
    for pos in positions:
        draw_crosshair(*pos)

def draw_crosshair3():
    """ Draws multiple crosshairs in a larger grid """
    positions = [
        (-200, 200), (0, 200), (200, 200),
        (-200, 0),   (0, 0),   (200, 0),
        (-200, -200), (0, -200), (200, -200),
        (-100, 100), (100, 100), (-100, -100), (100, -100)
    ]

    for pos in positions:
        draw_crosshair(*pos)

def clear_image():
    turtle.clear()

def draw_circle(x, y, radius, color):
    turtle.penup()
    turtle.goto(x, y - radius)
    turtle.pendown()
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()

def draw_rectangle(x, y, width, height, color):
    """Draws a filled rectangle starting from (x, y)"""
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.fillcolor(color)
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(width)
        turtle.right(90)
        turtle.forward(height)
        turtle.right(90)
    turtle.end_fill()

def draw_ear(x, y):
    """Draws an ear"""
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.fillcolor("brown")
    turtle.begin_fill()
    turtle.goto(x - 20, y + 40)
    turtle.goto(x + 20, y + 40)
    turtle.goto(x, y)
    turtle.end_fill()

def draw_tail(x, y):
    """Draws a tail"""
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.setheading(60)
    turtle.pensize(5)
    turtle.pencolor("brown")
    turtle.forward(50)
    turtle.pensize(1)

def draw_dog():
    turtle.clear()
    turtle.speed(0)

    # Body
    draw_rectangle(-50, -50, 100, 80, "brown")

    # Head
    draw_circle(-40, -20, 40, "brown")

    # Eyes
    draw_circle(-40, 0, 5, "black")
    draw_circle(-60, 0, 5, "black")

    # Nose
    draw_circle(-50, -20, 5, "black")

    # Ears
    draw_ear(-70, -10)
    draw_ear(-20, -10)

    # Legs
    draw_rectangle(-40, -130, 15, 40, "brown")
    draw_rectangle(20, -130, 15, 40, "brown")

    # Tail
    draw_tail(50,-50)
    turtle.end_fill()

def draw_circle(x, y, radius, color):
    """Draws a filled circle at (x, y) with the given radius and color"""
    turtle.penup()
    turtle.goto(x, y - radius)
    turtle.pendown()
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()

def draw_leaf(x, y, angle):
    """Draws a small leaf at (x, y) with a given rotation"""
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.setheading(angle)
    turtle.fillcolor("green")
    turtle.begin_fill()
    for _ in range(2):
        turtle.circle(10, 80)
        turtle.circle(10 // 2, 80)
    turtle.end_fill()

def draw_tomato():  # Disable animation for instant drawing
    turtle.clear()
    turtle.pensize(2)

    # Tomato body (Main red part)
    draw_circle(25, 25, 50, "red")

    # Leaves (Adding multiple leaves for a realistic effect)
    draw_leaf(-10, 50, 20)
    draw_leaf(10, 50, -20)
    draw_leaf(0, 55, 0)

    # Stem (A small green rectangle)
    turtle.penup()
    turtle.goto(-5, 65)
    turtle.pendown()
    turtle.pensize(4)
    turtle.pencolor("green")
    turtle.setheading(90)
    turtle.forward(10)

    turtle.update()  # Instantly render the drawing
    turtle.end_fill()
    turtle.done()


def display_lyrics_and_draw(previous_time, current_time, lyric, draw_function):
    time.sleep(current_time - previous_time)
    
    # Display each word one by one
    words = lyric.split()
    for word in words:
        print(word, end=" ", flush=True)
        time.sleep(0.3)  # Adjust delay between each word as needed
    print()  # Newline after the complete lyric
    
    draw_function()


def main():
    turtle.speed(0)
    screen = turtle.Screen()
    screen.title("World Search you")
    screen.setup(500,500)

    lyrics_with_timestamps = [
        (14, "Side by side, the lovelier goes up", lambda: None),
        (19, "Reach for the top 'til the bubble pops", lambda: None),
        (23, "Pick a memory, insert to the past", lambda: None),
        (28, "Which one is the sweetest? Save it for the last", lambda: None),
        (30, "If you turn into a table", draw_table),
        (32, "You must at the height of my elbows", lambda: None),
        (33, "Odd stubby leg makes you wobbly", lambda: None),
        (35, "You're the only perfect table for me", lambda: None),
        (36, "If you turn into an eggplant", draw_eggplant),
        (38, "You'll be my purple friend", lambda: None),
        (39, "Scratchy nail marks on your body", lambda: None),
        (41, "You're the only perfect eggplant for me", lambda: None),
        (42, "I'm searching", lambda: None),
        (55, "If you're a cat", draw_cat),
        (57, "A little kitten, you must be blue-point", lambda: None),
        (58, "Meowing a lot", lambda: draw_meow_text_repeatedly(3)),
        (59, "Hissing a lot but you never purr", lambda:draw_hiss_text_repeatedly(3)),
        (60, "If you're a steak", draw_steak),
        (61, "A filet Mignon covered in mushroom sauce", lambda: None),
        (62, "Browned on the outside", lambda: None),
        (63, "Medium rare inside", lambda: None),
        (65, "If you turn into a flower", draw_flower),
        (66, "You must be the most delicate ever", lambda: None),
        (67, "Even if you bloom just occasionally", lambda: None),
        (68, "You're the only perfect flower for me", lambda: None),
        (69, "If you turn into a human", draw_human),
        (71, "I'd like all the warmth coming from your hands", lambda: None),
        (72, "Bit of stinky breath, with hair that's unruly", lambda: None),
        (73, "You're the only perfect human for me", lambda: None),
        (74, "I'm searching", lambda: None),
        (88, "If you're a piece", lambda: None),
        (89, "A piece of shit", lambda: None),
        (90, "You must be, uhm", lambda: None),
        (92, "What, what's it called?", lambda: None),
        (93, "What's that word again?", lambda: None),
        (93, "Do-o-o-o-ope", lambda: draw_dope(4)),
        (94, "If you could stay", lambda: None),
        (95, "Stay the way you are", lambda: None),
        (96, "So I can uhmmm", lambda: None),
        (97, "Oh what, what's it called?", lambda: None),
        (98, "What's that word again?", lambda: None),
        (99, "Lo-o-o-ove", draw_heart),
        (100, "I'm searching for, searching for you everywhere", draw_crosshair2),
        (101, "I can see you in most everything", clear_image),
        (102, "I'm searching for, searching for you everywhere", draw_crosshair2),
        (103, "But somehow you can't stop transforming", lambda: None),
        (104, "I'm searching for, searching for, searching for", draw_crosshair3),
        (105, "Searching for, searching for, searching for, ah-ah", draw_crosshair3),
        (106, "I'm searching for, searching for, searching for", draw_crosshair3),
        (109, "My old self that's gone since you have left", lambda: None),
        (110, "Each one of us is a bucket of love", lambda: None),
        (112, "Some of us empty, some of us filled up", lambda: None),
        (116, "Cut us into pieces, break us down to the cell", lambda: None),
        (120, "Merge us back up, we have evolved now", lambda: None),
        (122, "If you turn into a flower", draw_flower),
        (124, "You must be the most delicate ever", lambda: None),
        (127, "Even if you bloom just occasionally", lambda: None),
        (128, "You're the only perfect flower for me", lambda: None),
        (129, "If you turn into a human", draw_human),
        (130, "I'd like all the warmth coming from your hands", lambda: None),
        (131, "Bit of stinky breath, with hair that's unruly", lambda: None),
        (132, "You're the only perfect human for me", lambda: None),
        (134, "I'm searching", lambda: None),
        (141, "If you're a dog", draw_dog),
        (142, "A little puppy going ruff, ruff, ruff", lambda: None),
        (143, "If you're a fruit", lambda: None),
        (144, "A tomato full of juice", draw_tomato)
    ]

    previous_time = 0
    for timestamp, lyric, draw_function in lyrics_with_timestamps:
        display_lyrics_and_draw(previous_time, timestamp, lyric, draw_function)
        previous_time = timestamp

    turtle.mainloop()

if __name__ == "__main__":
    main()
