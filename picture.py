"""
picture.py
Author: <your name here>
Credit: <list sources used, if any>

Assignment:

Use the ggame library to "paint" a graphical picture of something (e.g. a house, a face or landscape).

Use at least:
1. Three different Color objects.
2. Ten different Sprite objects.
3. One (or more) RectangleAsset objects.
4. One (or more) CircleAsset objects.
5. One (or more) EllipseAsset objects.
6. One (or more) PolygonAsset objects.

See:
https://github.com/HHS-IntroProgramming/Standards-and-Syllabus/wiki/Displaying-Graphics
for general information on how to use ggame.

See:
http://brythonserver.github.io/ggame/
for detailed information on ggame.

"""


# add your code here \/  \/  \/
from ggame import App
from time import time
import random
myapp = App()
myapp.run()

from ggame import App, Color, LineStyle, Sprite
from ggame import RectangleAsset, CircleAsset, EllipseAsset, PolygonAsset

# Three primary colors with no transparency (alpha = 1.0)
red = Color(0xff0000, 0.40)
green = Color(0x00ff00, 1.0)
blue = Color(0x0000ff, 0.50)
black = Color(0x000000, 0.30)

# Define a line style that is a thin (1 pixel) wide black line
thinline = LineStyle(1, black)
# A graphics asset that represents a rectangle
rrrectangle = EllipseAsset(20, 10, thinline, red)
rrectangle = EllipseAsset(40, 20, thinline, red)
bellipse = EllipseAsset(125,150,thinline, blue)
vrectangle = EllipseAsset(40, 20, thinline, red)
poly = PolygonAsset([(0,0), (50,50), (50,100), (0,0)], thinline, red)
blektrang = RectangleAsset(100, 15,thinline, red)
bleh = RectangleAsset(40, 700, thinline, red)
rurg = EllipseAsset(20, 10, thinline, green)
tooth = RectangleAsset( 20, 10, thinline, red)
tooth2 = RectangleAsset( 20, 10, thinline, red)
# Now display a rectangle
Sprite(rrectangle,(450,270))
Sprite(bellipse, (500,370))
Sprite(vrectangle, (550, 270))
Sprite(poly, (500, 300))
Sprite(blektrang, (450, 450))
Sprite(rrrectangle, (450,270))
Sprite(bleh, (475,515))
Sprite(rurg, (550, 270))
Sprite(tooth, (500,460))
Sprite(tooth2, (450,460))

# add your code here /\  /\  /\


myapp = App()
myapp.run()
