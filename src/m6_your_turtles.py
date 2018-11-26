"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher,
         Aaron Wilkin, their colleagues, and Samuel VanDenburgh.
"""
########################################################################
# DONE: 1.
#   On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
########################################################################

########################################################################
# TODO: 2.
#   You should have RUN the  m5e_loopy_turtles  module and READ its code.
#   (Do so now if you have not already done so.)
#
#   Below this comment, add ANY CODE THAT YOU WANT, as long as:
#     1. You construct at least 2 rg.SimpleTurtle objects.
#     2. Each rg.SimpleTurtle object draws something
#          (by moving, using its rg.Pen).  ANYTHING is fine!
#     3. Each rg.SimpleTurtle moves inside a LOOP.
#
#   Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#   If you make syntax (notational) errors, no worries -- get help
#   fixing them at either this session OR at the NEXT session.
#
#   Don't forget to COMMIT-and-PUSH when you are done with this module.
#
########################################################################

import rosegraphics as  rg

window = rg.TurtleWindow()

leo = rg.SimpleTurtle('turtle')
leo.pen = rg.Pen('blue', 5)
leo.speed = 50

raph = rg.SimpleTurtle('turtle')
raph.pen = rg.Pen('red', 5)
raph.speed = 50

mike = Leo = rg.SimpleTurtle('turtle')
mike.pen = rg.Pen('orange', 5)
mike.speed = 50

size = 100

leo.left(180)
leo.forward(50)

for k in range(20):
    leo.draw_square(size)
    raph.draw_circle(size)
    size = size - 4.9