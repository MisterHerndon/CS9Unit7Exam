
# 1.
# How many orange lines will this function draw?

def draw_line():
    pendown()
    for i in range(20, 35, 5):
        if i == 25:
            color("orange")
        forward(i)
        left(90)
        forward()






# 2.
# What does the following code print?

if 50 == 45:
    print("Sweet Sauce")
if 7 < "10":
    print("Mild Sauce")
if 80 >= 27:
    print("Hot Sauce")





# 3.
# When you enter your age, what does this code print?

age = int(input("Enter your age: "))

if age < 30:
    print("You're an adult")
elif age < 18:
    print("You're a teenager")
elif age < 13:
    print("You're a kid")
else:
    print("You're a baby")





# 4. 
# What does a user need to enter into the input propmt to make a green circle?

circle_color = input("Enter a color: ")

if circle_color.startswith("R"):
    color("red")
elif circle_color.startswith("G"):
    color("green")
else:
    color("blue")
circle(50)






# 5.
# What will happen when the following program is run and the user enters “g”?

number = input("Enter a number: ")

while True:
    if not number.isnumeric():
        print("Not a valid number")
    else:
        break





# 6.
# Bucky the elf needs to save Christmas! 
# Santa is on his sleigh and running out of gifts and it is Bucky's job to refill the sack via the
# interdimensional portal from the north pole. He needs some lead time to prep the gifts and he
# also needs to know when to push them through.  He should probably prep the gifts when there
# are less than 10, and push them through when there are less than 5.

# Luckily for Bucky, the sleigh is equipped with an onboard computer that uses Python, and you
# have nearly completed Mr Herndon's 8th grade computer science!  Using the following
# functions, create a feedback system and get those presents to Santa to help Bucky save
# Christmas!  (don't forget a while loop in this!  oooh, and and if/elif/else!)

## this function gives back the current number of gifts left in the sack
# count_gifts()

## this function prepares the next load of gifts to send through the portal
# prep_gifts()

## this function sends the gifts through the portal
# launch_that_junk()
